from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os

def openfile(self):

    file = QFileDialog.getOpenFileName(self, 'Select file', os.curdir, "Text Files (*.txt);; All Files(*.*)")
    if not file[0]: return
    
    filehandle = QFile(file[0])
    if not filehandle.open(QIODevice.ReadOnly): return

    stream = QTextStream(filehandle)
    
    text = stream.readAll()
    name = file[0]

    return text, name

def savefile(self, text):
    file = QFileDialog.getSaveFileName(self, 'Select file', os.curdir, "Text Files (*.txt);; All Files(*.*)")
    if not file[0]:
        return None
    
    filehandle = QFile(file[0])
    if not filehandle.open(QIODevice.WriteOnly):
        return None

    stream = QTextStream(filehandle)
    stream << text
    stream.flush()

    return file[0]
    

