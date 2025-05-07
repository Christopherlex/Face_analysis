Real-Time Facial Analysis
This project performs real-time facial analysis, estimating age, race, and distance from the camera.

Features
Age Estimation (+- 5 years)

Race/Ethnicity Classification

Distance Estimation from the camera

Requirements
Install dependencies:

bash
Copy
pip install opencv-python mediapipe tensorflow
Clone the repository:

bash
Copy
git clone https://github.com/your-username/face-analysis.git
cd face-analysis
How to Run
To start the facial analysis, run:

bash
Copy
python face_analysis.py
How It Works
The program captures video from your camera.

It detects faces using MediaPipe.

It estimates the age and race of the detected face using deep learning models.

It calculates the distance from the camera based on the face’s size.
