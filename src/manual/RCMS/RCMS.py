import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./src/manual/RCMS/RCMS.ui")[0]

class RCMS(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_W:
            print('forward')
        if e.key() == Qt.Key_S:
            print('backward')
        if e.key() == Qt.Key_A:
            print('lefttrun')
        if e.key() == Qt.Key_D:
            print('righttrun')

    def keyReleaseEvent(self, e):
        print('stop')
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_RCMS = RCMS()
    app_RCMS.show()
    app.exec_()
