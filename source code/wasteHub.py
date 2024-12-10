import serial
import numpy as np
import cv2
from picamera2 import Picamera2
import tflite_runtime.interpreter as tflite
import firebase_admin
from firebase_admin import credentials, db
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import time

model_path = "model.tflite"
tree = open("fallDetectTree.pkl","rb")
clf = pickle.load(tree)
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_func(img_path):
    img = cv2.imread(img_path)  
    img_resized = cv2.resize(img, (224, 224))  # Resize image to model's expected size
    img_normalized = img_resized.astype(np.float32) / 255.0  
    img_expanded = np.expand_dims(img_normalized, axis=0)  

    interpreter.set_tensor(input_details[0]['index'], img_expanded)
    interpreter.invoke()  # Run model inference
    output_data = interpreter.get_tensor(output_details[0]['index'])
    result = np.argmax(output_data)
    
    if result == 0:
        print("This image -> Recyclable")
        ser.write(b'recyclable\n')
    elif result == 1:
        print("This image -> Organic")
        ser.write(b'organic\n')

def append_data_to_firebase(data, prediction):
    ref = db.reference('/')  # Adjust the reference as needed
    custom_key = str(int(time.time()))
    # Since you only want to store the label, you do not need to copy all data
    label_to_store = int(prediction[0])  # Ensuring the prediction is converted to an integer
    fall = 7
    not_fall = 8
    if label_to_store == 1 :
        ref.child("fall").set(fall)
    if label_to_store == 0 :
        ref.child("fall").set(not_fall)
        
# Setup serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()

# Setup Firebase
cred = credentials.Certificate('serviceAccountKey.json')  
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-management-waste-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Initialize Camera
picamera2 = Picamera2()
config = picamera2.create_still_configuration()
picamera2.configure(config)

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if line == "takephoto":
                picamera2.start()
                picamera2.capture_file("target.jpg")
                picamera2.stop()
                # Use image for classification
                predict_func('target.jpg')
            elif ',' in line:
                x, y, z = line.split(',')
                data_dict = {'x': [float(x)], 'y': [float(y)], 'z': [float(z)]}  # Create a dictionary for DataFrame
                df = pd.DataFrame(data_dict)
                new_predictions = clf.predict(df)
                print("New Data Predictions:", new_predictions)
                append_data_to_firebase(data_dict, new_predictions)
            else:
                data_value=int(line)
                print(data_value)
                ref = db.reference('/')
                if data_value in (1, 2, 3): 
                    ref.update({
                        'organic': data_value,
                    })
                else:
                    i=0
                    if data_value==4:
                        i=1
                    elif data_value==5:
                        i=2
                    else:
                        i=3
                    ref.update({
                        'recycle': i,
                    })
finally:
    picamera2.stop()
    if ser.is_open:
        ser.close()

