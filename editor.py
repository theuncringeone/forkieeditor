from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import subprocess
import time

class editorwidget(QWidget):
    def __init__(self, parent = ..., flags = ...):
        super().__init__()
        
        self.isSaved = False
        
        self.defaultfont = QFont("Arial", 18)

        self.text = QTextEdit()
        self.text.setFont(self.defaultfont)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.text)
        
        self.setLayout(self.vbox)