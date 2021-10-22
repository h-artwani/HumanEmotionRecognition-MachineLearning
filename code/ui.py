from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2
from PIL import Image
import pandas as pd
import numpy as np
import os
from .CaptureVideo import CaptureFace
from .showPics import ShowImages
from .Classification import Classification

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()     
        self.mainWindow = None
        self.captureFaces = []
        self.emotions = []
        self.defaultmap = QtGui.QPixmap("./pics/default.png")
        self.labelfont = QtGui.QFont('Times',12) 
        self.classify = Classification(self)

    def closeEvent(self,event):
        buttonReply = QMessageBox.question(self.mainWindow, 'Closing Message', "Are You Sure To Exit ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:            
            print('Yes clicked.')           
            self.app.exit()
            event.accept()
        else:
            print('No clicked.')
            event.ignore()

    def setupVideoFrame(self):
        self.videoFrame = QtWidgets.QFrame(self.centralwidget)
        self.videoFrame.setGeometry(QtCore.QRect(5, 10, 650, 400))
        self.videoFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.videoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoFrame.setMidLineWidth(2)
        self.videoFrame.setObjectName("videoFrame")
        self.videoLabel = QtWidgets.QLabel(self.videoFrame)          
        self.videoLabel.setGeometry(4, 5, 650, 400);  
        self.captureButton = QtWidgets.QPushButton(self.videoFrame)
        self.captureButton.setGeometry(QtCore.QRect(50, 50, 150, 30))
        self.captureButton.setObjectName("captureButton") 
        _translate = QtCore.QCoreApplication.translate
        self.mainWindow.setWindowTitle(_translate("MainWindow", "Emotion App"))
        self.captureButton.setText(_translate("MainWindow", "Start Capture")) 
        self.captureButton.clicked.connect(self.startCapturing) 


    def setupCaptureFaces(self):         
        self.emotlbl = QtWidgets.QLabel(self.centralwidget)
        self.emotlbl.setText('Your Capture Faces ')
        self.emotlbl.setFont(self.labelfont)
        self.emotlbl.setGeometry(QtCore.QRect(10, 380, 600, 100))

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(5, 450, 1200, 200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setMidLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        
        self.grid = QGridLayout(self.frame_2)
        self.frame_2.setLayout(self.grid)

        self.img1 = QtWidgets.QLabel()
        self.grid.addWidget(self.img1,0,0)
        self.img1.setPixmap(self.defaultmap)  

        self.img2 = QtWidgets.QLabel()
        self.grid.addWidget(self.img2,0,1)
        self.img2.setPixmap(self.defaultmap)  

        self.img3 = QtWidgets.QLabel()
        self.grid.addWidget(self.img3,0,2)
        self.img3.setPixmap(self.defaultmap)  

        self.img4 = QtWidgets.QLabel()
        self.grid.addWidget(self.img4,0,3)
        self.img4.setPixmap(self.defaultmap)  

        self.img5 = QtWidgets.QLabel()
        self.grid.addWidget(self.img5,0,4)
        self.img5.setPixmap(self.defaultmap)  

        self.em1 = QtWidgets.QLabel()
        self.em1.setFont(self.labelfont)
        self.grid.addWidget(self.em1,1,0)
        self.em2 = QtWidgets.QLabel()
        self.em2.setFont(self.labelfont)
        self.grid.addWidget(self.em2,1,1)
        self.em3 = QtWidgets.QLabel()
        self.em3.setFont(self.labelfont)
        self.grid.addWidget(self.em3,1,2)
        self.em4 = QtWidgets.QLabel()
        self.em4.setFont(self.labelfont)
        self.grid.addWidget(self.em4,1,3)
        self.em5 = QtWidgets.QLabel()
        self.em5.setFont(self.labelfont)
        self.grid.addWidget(self.em5,1,4)        
        
        self.emotions.append(self.em1)
        self.emotions.append(self.em2)
        self.emotions.append(self.em3)
        self.emotions.append(self.em4)
        self.emotions.append(self.em5)

        self.captureFaces.append(self.img1)
        self.captureFaces.append(self.img2)
        self.captureFaces.append(self.img3)
        self.captureFaces.append(self.img4)
        self.captureFaces.append(self.img5)  


    def deleteOldFiles(self):
        folder = './analysis_pics/'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)


    def startCapturing(self):
        self.deleteOldFiles()        
        faces = self.capture.imgs   
        #print(faces)           
        for i in range(len(faces)):
            face = faces[i]
            imgbox = self.captureFaces[i]
            cv2.imwrite("./analysis_pics/img"+ str(i) + ".jpg", face)
        show = ShowImages(self)
        show.start() 
        self.classify.faces = faces
        if not self.classify.is_alive():
            self.classify.start()

    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)       
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.closeEvent  = self.closeEvent

        self.setupCaptureFaces()

        self.setupVideoFrame()
        self.capture  = CaptureFace(self)
        self.capture.start() 
