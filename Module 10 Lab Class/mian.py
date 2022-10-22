""" My Camera Application
author: Ariful
"""

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QTimer
import cv2
import datetime


class Window(QWidget):
    """ Main app window """

    def __init__(self):
        super().__init__()

        # variable for app window
        self.window_width = 640
        self.window_height = 400

        #image variable
        self.img_width = 640
        self.img_height = 400

        #other variable
        self.dt = '0-0-0'
        self.record_flag = False

        #load icon
        self.camera_icon = QIcon(cam_icon_path)
        self.rec_icon = QIcon(cam_recd_path)
        self.stop_icon = QIcon(stop_icon_path)

        #to save the video
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        #setup the window
        self.setWindowTitle("My Camera App")
        self.setGeometry(100,100,self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        #setup timer

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()

    def ui(self):
        """ contain all ui things """
        #layout
        grid = QGridLayout()
        self.setLayout(grid)

        #image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.img_width, self.img_height)

        #capture button
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        self.capture_btn.setStyleSheet("border-radius: 30; border: 2px solid black; border-width: 3px")
        self.capture_btn.setFixedSize(60, 60)
        self.capture_btn.clicked.connect(self.save_image)

        #record button
        self.rec_btn = QPushButton(self)
        # self.rec_btn.setIcon(self.rec_icon)
        self.rec_btn.setStyleSheet("border-radius: 30; border: 2px solid black; border-width: 3px")
        self.rec_btn.setFixedSize(60, 60)
        self.rec_btn.clicked.connect(self.record)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        #add things to the layout
        grid.addWidget(self.capture_btn, 0, 0)
        grid.addWidget(self.image_label, 0, 1, 2, 3)
        grid.addWidget(self.rec_btn, 1, 0)

        self.show()

    def update(self):
        """ update frame """
        _, self.frame = self.cap.read()

        if self.record_flag ==  True:
            print("Recording.....")
            self.rec_btn.setIcon(self.stop_icon)
            self.frame = cv2.circle(self.frame, (20,70),5, (0,0,255), 10)
        else:
            self.rec_btn.setIcon(self.rec_icon)


        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) # Blue, green, Red
        height, width, channel = frame.shape
        step = channel * width

        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_frame))

    def save_image(self):
        """ save image from camera """
        # print("He call me")
        self.get_time()
        cv2.imwrite(f"{self.dt}.jpg", self.frame)

    def record(self):
        """ record the video """
        print(self.record_flag)

        if self.record_flag == True:
            self.record_flag = False
            print("Stopping the record")
        else:
            self.record_flag = True
            print("Starting the record")
            self.get_time()

            self.out = cv2.VideoWriter(f"{self.dt}.avi", self.fourcc, 20.0, (self.image_width, self.image_height))

    def get_time(self):
        now = datetime.datetime.now()
        self.dt = now.strftime("%m-%d-%y, %H-%M-%S")
        print(self.dt)

#run
cam_icon_path = 'assets/photo-camera-interface-symbol-for-button.png'
cam_recd_path = 'assets/video-camera.png'
stop_icon_path = 'assets/video-camera.png'

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())


