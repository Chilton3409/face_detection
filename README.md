# face_detection
A simple PyQt application that demonstrates facial detection using OpenCV and dlib. This app allows users to open an image file and detect faces with facial landmarks.


Features

Open image files using a file dialog
Detect faces in images using dlib's facial detection model
Draw rectangles around detected faces
Detect facial landmarks using dlib's landmark prediction model
Display detected faces and landmarks in the image



Requirements

Python 3.x
PyQt5
OpenCV
dlib



Installation

Clone the repository
Install required packages: pip install pyqt5 opencv-python dlib
Download the shape_predictor_68_face_landmarks.dat model file from the dlib repository



Usage

Run the application: python facial_detection_app.py
Click "Open Image" to select an image file
Click "Detect Faces" to detect faces and facial landmarks in the image



Notes

Make sure to update the path to the shape_predictor_68_face_landmarks.dat model file in the code.
This application uses dlib's facial detection and landmark prediction models.



Future Work

Improve face detection accuracy and speed
Add more features, such as face recognition or emotion detection
