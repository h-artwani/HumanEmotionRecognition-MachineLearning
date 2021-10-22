import cv2
from PyQt5 import *
from threading import Thread

class CaptureFace(Thread):    
        def __init__(self,uiobj):
            super().__init__()
            self.uiobj = uiobj
            self.cap = cv2.VideoCapture(0)

        def run(self):
            while True: 
                ret, image_np = self.cap.read()
                gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
                haar_cascade_face = cv2.CascadeClassifier('./cascadefiles/haarcascades/haarcascade_frontalface_alt.xml')
                
                faces_rects = haar_cascade_face.detectMultiScale(gray_image, scaleFactor = 1.2, minNeighbors = 5)
                self.imgs = []                
                for (x,y,w,h) in faces_rects:
                    cv2.rectangle(image_np, (x, y), (x+w, y+h), (255, 0, 0), 1)
                    self.imgs.append(image_np[y:y + h, x:x + w])

                # *********************** Video Show ****************************
                gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
                height, width, channel = image_np.shape
                img = QtGui.QImage(image_np.data, width, height ,QtGui.QImage.Format_RGB888)
                convertToQtFormat = QtGui.QPixmap.fromImage(img)
                pixmap = QtGui.QPixmap(convertToQtFormat)
                resizeImage = pixmap.scaled(640, 480, QtCore.Qt.KeepAspectRatio)               
                self.uiobj.videoLabel.setPixmap(resizeImage)
            print("Record Thread End")  
        
