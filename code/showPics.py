import time
from PyQt5 import QtGui
from threading import Thread
import os

class ShowImages(Thread):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        
    
    def run(self):
        folder = './analysis_pics/'
        index=0
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            map = QtGui.QPixmap(file_path)
            self.ui.captureFaces[index].setPixmap(map)  
            index+=1
            