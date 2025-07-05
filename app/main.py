from os import path
from sys import argv
from PyQt6 import QtCore, QtGui, QtWidgets



class XPad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('X-Pad')
        self.setWindowIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/icon.png'))
        self.showMaximized()



application = QtWidgets.QApplication(argv)
window = XPad()
window.show()
application.exec()