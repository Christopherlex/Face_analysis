import cv2
from deepface import DeepFace
import numpy as np

# Initialize OpenCV face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Camera focal length (you might need to calibrate this value)
focal_length = 500  # In pixels, this is an estimated value for simplicity
real_face_width = 14  # In cm, average adult face width

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Crop the face region from the frame
        face_roi = frame[y:y+h, x:x+w]
        
        try:
            # Use DeepFace to estimate age and race for multiple faces
            result = DeepFace.analyze(face_roi, actions=['age', 'race'])
            
            # result should be a list of dictionaries, so iterate through each detected face
            for res in result:
                age = res['age']
                race = res['dominant_race']
                
                # Display the age and race
                cv2.putText(frame, f"Age: {age}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                cv2.putText(frame, f"Race: {race}", (x, y + h + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                # Calculate the distance (using face width in pixels and known real face width)
                face_width_in_pixels = w
                distance = (focal_length * real_face_width) / face_width_in_pixels

                # Display the estimated distance
                cv2.putText(frame, f"Distance: {int(distance)} cm", (x, y + h + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        except Exception as e:
            print(f"Error in age/race detection: {e}")
        
    # Show the frame with face, age, race, and distance information
    cv2.imshow('Face Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
