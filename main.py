from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from editor import *
import filedialog

class mainwin(QMainWindow):
    def __init__(self, parent = ..., flags = ...):
        super().__init__()

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

        self.newaction = QAction("New", self)
        self.filemenu.addAction(self.newaction)

        self.openaction = QAction("Open", self)
        self.filemenu.addAction(self.openaction)
        self.openaction.triggered.connect(self.opendialog)

        self.saveaction = QAction("Save", self)
        self.filemenu.addAction(self.saveaction)

        self.filemenu.addSeparator()

        self.exitaction = QAction("Exit", self)
        self.filemenu.addAction(self.exitaction)
        self.exitaction.triggered.connect(self.exitdialog)

    def exitdialog(self):
        if self.editor.isSaved == False:
            confirmation = QMessageBox.question(self, "", "Do you want to save the file?")
            if confirmation == QMessageBox.y:
                pass
            else:
                QCoreApplication.instance().quit()

    def opendialog(self):
        textfile = filedialog.openfile(self)
        self.editor.text.setPlainText(textfile)



if __name__ == "__main__":
    app = QApplication([])

    form = mainwin()
    form.show()

    app.exec_()

        