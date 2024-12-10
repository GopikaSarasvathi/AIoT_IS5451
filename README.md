# AIoT_IS5451
This project demonstrates the potential of AIoT to transform traditional waste management into a smarter, eco-friendly system.


## Table of Contents  
- [Overview](#overview)  
- [Features](#features)  
- [System Architecture](#system-architecture)  
- [Running Instructions](#running-instructions)  
- [Dependencies](#dependencies)  
- [Contributors](#contributors)  

---

## Overview  
Traditional waste management systems often face challenges such as inefficiency in bin monitoring, improper waste segregation, and limited real-time tracking. This project addresses these issues by leveraging AIoT to create a smarter, eco-friendly system.  

The system features:  
1. Real-time bin-level monitoring using ultrasonic sensors.  
2. Automated waste classification through computer vision.  
3. Fall detection using machine learning models.  
4. Integration with a mobile application for real-time data visualization and notifications.  

---

## Features  
- **Bin-Level Monitoring**:  
  Microbits equipped with ultrasonic sensors detect and monitor bin fill levels.  

- **Waste Classification via Computer Vision**:  
  A TensorFlow Lite model processes input from a camera module on the Raspberry Pi 4 to classify waste.  

- **Fall Detection using Machine Learning**:  
  A trained ML model (`fallDetectTree.pkl`) detects falls, enhancing the safety and usability of the system in operational environments.  

- **Android Application**:  
  Real-time updates on bin levels, waste classification results, and fall detection alerts are displayed on a user-friendly mobile interface.  

---

## System Architecture  
The system consists of the following components:  
1. **Microbits with Grove Shields**:  
   - For ultrasonic sensors to monitor bin levels.  
   - Servo motor control via a separate Microbit.  

2. **Raspberry Pi 4**:  
   - Hosts the main `wasteHub.py` script.  
   - Processes waste classification via computer vision using a TensorFlow Lite model.  
   - Executes fall detection using a pre-trained ML model (`fallDetectTree.pkl`).  

3. **Android Application**:  
   - Displays bin levels, waste classification results, and fall detection alerts.  
   - Syncs with the database for real-time data updates.  

---

## Running Instructions  
### Hardware Setup  
1. **Bin-Level Monitoring**:  
   - Load `sources\Bin level Monitoring` code onto two separate Microbits.  
   - Connect the Microbits to Grove shields and ultrasonic sensors.  

2. **Node Controller**:  
   - Load `sources\nodeController.js` onto a separate Microbit.  
   - Connect the servo motor to this Microbit.  

3. **Main Controller**:  
   - Load `sources\wasteHub.py` onto a Raspberry Pi 4.  
   - Connect the camera module to the RPi4.  

### Software Setup  
1. **Mobile Application**:  
   - Choose an APK that matches your phone's architecture from the `bin` directory.  
   - Install the APK on your Android phone.  

2. **Database Setup**:  
   - Ensure `serviceAccountKey.json` for database access is placed in the same folder as `wasteHub.py`.  

### Execution  
1. Assemble all components inside the provided prototype box.  
2. Connect the controller Microbit to the RPi4 using USB.  
3. Execute `wasteHub.py` on the Raspberry Pi 4. Ensure the following files are in the same directory:  
   - `sources\Falldetection\fallDetectTree.pkl` (ML model for fall detection)  
   - `sources\Waste Classification\model.tflite` (TensorFlow Lite model for waste classification)  
4. Verify successful data updates in the database.  
5. View the results on the Android application.  

---

## Dependencies  
- **Hardware**:  
  - Microbits with Grove Shields  
  - Ultrasonic Sensors  
  - Servo Motor  
  - Raspberry Pi 4  
  - Camera Module  

- **Software**:  
  - Python 3.x  
  - Node.js  
  - TensorFlow Lite (for `model.tflite`)  
  - Pre-trained ML Model: `fallDetectTree.pkl`  

---

## Contributors  
- **Gopika Sarasvathi Kothandaraman** (Group Leader):  
  A0274980R, e1124726@u.nus.edu  

- **Li Wei Ting**:  
  A0274987A, e1124733@u.nus.edu  

- **Sylviya Alexander**:  
  A0276584M, e1132317@u.nus.edu  

- **Yusril Izza**:  
  A0264323L, e1023875@u.nus.edu  

---

