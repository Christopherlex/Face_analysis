# Real-Time Facial Analysis
This project performs real-time facial analysis, estimating age, race, and distance from the camera.

## Features
1. Age Estimation (+- 5 years)
2. Race/Ethnicity Classification
3. Distance Estimation from the camera

## Required Modules
1. OpenCV for image and video processing
2. MediaPipe for real-time face detection
3. Deepface for deep learning models used for age and race estimation

## How It Works
1. The program captures video from your camera.
2. It detects faces using MediaPipe.
3. It estimates the age and race of the detected face using deep learning models.
4. It calculates the distance from the camera based on the face’s size.

## How to run 
1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the pip install command.
3. Run the face recognition.py script.
4. Make sure your webcam is working and give the script access to it.
