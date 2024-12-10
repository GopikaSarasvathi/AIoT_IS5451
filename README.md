# AIoT_IS5451
This project demonstrates the potential of AIoT to transform traditional waste management into a smarter, eco-friendly system.

Group 07

Members:
Gopika Sarasvathi Kothandaraman, A0274980R, e1124726@u.nus.edu (Group Leader) 

Li Wei Ting, A0274987A, e1124733@u.nus.edu

Sylviya Alexander, A0276584M, e1132317@u.nus.edu

Yusril Izza, A0264323L, e1023875@u.nus.edu

Running instructions:
1. Load the two codes from sources\Bin level Monitoring onto two separate Microbits, connect these Microbits to Grove shields and ultrasonic sensors.
2. Load sources\nodeController.js onto a separate Microbit and connect the servo motor to it.
3. Load sources\wasteHub.py onto an RPi4 and also connect the camera module to it.
4. Choose an APK that matches your phone's architecture from the bin directory and load it onto your Android phone.
5. Run the prototype by connecting all components together in the box (connect the controller Microbit to the RPi4 using USB) and execute wasteHub.py on the RPi4 (make sure sources\Falldetection\fallDetectTree.pkl, sources\Waste Classification\model.tflite, and sources\serviceAccountKey.json are in the same folder as wasteHub.py). Ensure it runs successfully and check the database to see if the data is updated properly. If the data updates correctly, check the results on the Android application.
