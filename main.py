from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from editor import *
import filedialog

class mainwin(QMainWindow):
    def __init__(self, parent = ..., flags = ...):
        super().__init__()

        self.currentFile = None

        desktop = QDesktopWidget()
        screenx = desktop.width()
        screeny = desktop.height()

        self.setWindowTitle("Forkie Editor")
        self.setGeometry(screenx // 2, screeny // 2, 800, 600)

        self.editor = editorwidget()

        self.setCentralWidget(self.editor)
        self.setupMenuBar()

    def setupMenuBar(self):
        self.filemenu = self.menuBar().addMenu("&File")
        self.editmenu = self.menuBar().addMenu("&Edit")
        self.editmenu.setDisabled(True)

        self.newaction = QAction("New", self)
        self.filemenu.addAction(self.newaction)
        self.newaction.triggered.connect(self.newdialog)

        self.openaction = QAction("Open", self)
        self.filemenu.addAction(self.openaction)
        self.openaction.triggered.connect(self.opendialog)

        self.saveaction = QAction("Save", self)
        self.filemenu.addAction(self.saveaction)
        self.saveaction.triggered.connect(self.savedialog)

        self.saveasaction = QAction("Save As", self)
        self.filemenu.addAction(self.saveasaction)
        self.saveasaction.triggered.connect(self.saveasdialog)

        self.filemenu.addSeparator()

        self.exitaction = QAction("Exit", self)
        self.filemenu.addAction(self.exitaction)
        self.exitaction.triggered.connect(self.exitdialog)

    def exitdialog(self):
        if self.editor.isSaved == False:
            confirmation = QMessageBox.question(self, "", "Do you want to save the file?")
            if confirmation == QMessageBox.Yes:
                self.savedialog()
            else:
                QCoreApplication.instance().quit()

    def newdialog(self):
        self.editor.text.setPlainText("")
        form.setWindowTitle("Untitled - Forkie Editor")
        self.editor.isSaved = True

    def savedialog(self):
        if not self.currentFile:  # Save As
            try:
                filePath = filedialog.savefile(self, self.editor.text.toPlainText())
                if filePath:
                    self.currentFile = filePath
                    self.setWindowTitle(filePath + " - Forkie Editor")
                    self.editor.isSaved = True
            except TypeError:
                pass
        else:  # Overwrite existing file
            file = QFile(self.currentFile)
            if not file.open(QIODevice.WriteOnly):
                return
            stream = QTextStream(file)
            stream << self.editor.text.toPlainText()
            stream.flush()
            self.editor.isSaved = True

    def saveasdialog(self):
        try:
            filePath = filedialog.savefile(self, self.editor.text.toPlainText())
            if filePath:
                self.currentFile = filePath
                self.setWindowTitle(filePath + " - Forkie Editor")
                self.editor.isSaved = True
        except TypeError:
                pass

    def opendialog(self):
        try:
            text, filePath = filedialog.openfile(self)
            if filePath:
                self.editor.text.setPlainText(text)
                self.currentFile = filePath
                self.setWindowTitle(filePath + " - Forkie Editor")
                self.editor.isSaved = True
        except TypeError:
            pass



if __name__ == "__main__":
    app = QApplication([])

    form = mainwin()
    form.show()

    form.setWindowTitle("Untitled - Forkie Editor")

    app.exec_()

        