from threading import Thread
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import cv2


class Classification(Thread):
    
    def __init__(self,ui):
        super().__init__()
        self.loadEmotionDataset()
        self.faces = None
        self.ui = ui
        
    def loadEmotionDataset(self):
        print("Read Emotion CSV")
        self.emotionsDF = pd.read_csv('./dataset/emotion_140X140.csv')
        self.emotionsDF = self.emotionsDF.drop('Unnamed: 0',axis=1)
        self.data = self.emotionsDF.iloc[:, 0:19600].values
        self.emot = self.emotionsDF['19600'].values
        print("Reading END") 

    def run(self):
        if self.faces is not None:
            print("Faces Found : ", len(self.faces))
            index=0
            for face in self.faces:
                gray_image = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                gray_image = cv2.resize(gray_image, (140, 140))
                flat_np = gray_image.flatten()
                #emot = self.knn(flat_np)
                emot = self.svm(flat_np)
                print(emot)
                self.ui.emotions[index].setText(emot)
                index+=1



    def knn(self,flat_np):
        clf = KNeighborsClassifier(n_neighbors=25)
        clf = clf.fit(self.data, self.emot)
        y_pred = clf.predict(flat_np.reshape(1,-1))
        Y = y_pred[0]
        emotion = ""
        if Y==0:
            emotion = "angry"
        elif Y==1:
            emotion = "disgust"
        elif Y==2:
            emotion = "fear"
        elif Y==3:
            emotion = "happy"
        elif Y==4:
           emotion = "sad"
        elif Y==5:
            emotion = "surprise"
        elif Y==6:
            emotion = "normal"
        return emotion.capitalize()


    def svm(self,flat_np):
        clf = SVC(kernel='linear')
        clf = clf.fit(self.data, self.emot)
        y_pred = clf.predict(flat_np.reshape(1,-1))
        Y = y_pred[0]
        emotion = ""
        if Y==1:
            emotion = "happy"
        elif Y==3:
            emotion = "sadness"
        elif Y==2:
            emotion = "surprise"
        elif Y==4:
            emotion = "disgust"
        else:
            emotion = "not recognized"
        return emotion.capitalize()
