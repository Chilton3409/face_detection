#!/usr/bin/env python3
#New file created
Here's a comprehensive example of a PyQt app that demonstrates a simple image viewer with facial detection using OpenCV and dlib. This example showcases how to design the UI, implement functionality, and use signal-slot mechanisms.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
import dlib

class FacialDetectionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.image_path = None
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        button = QPushButton("Open Image")
        button.clicked.connect(self.open_image)
        layout.addWidget(button)

        detect_button = QPushButton("Detect Faces")
        detect_button.clicked.connect(self.detect_faces)
        layout.addWidget(detect_button)

        self.setLayout(layout)

    def open_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File")
        if self.image_path:
            self.display_image(self.image_path)

    def display_image(self, image_path):
        image = cv2.imread(image_path)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        qimg = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.image_label.setPixmap(QPixmap.fromImage(qimg).scaled(400, 400, Qt.KeepAspectRatio))

    def detect_faces(self):
        if self.image_path:
            image = cv2.imread(self.image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.detector(gray)

            for face in faces:
                cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

                landmarks = self.predictor(gray, face)
                for n in range(0, 68):
                    x = landmarks.part(n).x
                    y = landmarks.part(n).y
                    cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

            height, width, channel = image.shape
            bytes_per_line = 3 * width
            qimg = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.image_label.setPixmap(QPixmap.fromImage(qimg).scaled(400, 400, Qt.KeepAspectRatio))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FacialDetectionApp()
    ex.show()
    sys.exit(app.exec_())
Detailed Explanation
This code creates a simple PyQt app that allows users to open an image file and detect faces using dlib's facial detection and landmark prediction models. The app's UI consists of a label to display the image, a button to open the image file, and a button to detect faces.
When the user clicks the "Open Image" button, the app opens a file dialog for the user to select an image file. The selected image is then displayed in the label.
When the user clicks the "Detect Faces" button, the app uses dlib's facial detection model to detect faces in the image. For each detected face, the app draws a rectangle around the face and detects facial landmarks using dlib's landmark prediction model. The detected faces and landmarks are then displayed in the label.
The app uses PyQt's signal-slot mechanism to connect the buttons' clicked signals to the corresponding slots (i.e., the open_image and detect_faces methods). The display_image method is used to display the image in the label.
Overall, this code demonstrates how to create a comprehensive PyQt app with facial detection functionality using OpenCV and dlib.
