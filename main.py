__author__ = 'Luka Marjanović'

import sys, pyperclip
from generator import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QGuiApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def pass_button(self):
        global x
        x = make_pass()
        self.label.setText(x)
        self.label.move(163, 75)
        self.update()

    def copy_pass(self):
        try:
            pyperclip.copy(x)
            spam = pyperclip.paste()
        except:
            pass

    def initUI(self):
        #Creating the Window
        self.setStyleSheet('background-color: #5D6D7E')
        self.setGeometry(500, 200, 400, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle('Password generator')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label = QtWidgets.QLabel(self)
        self.label.move(50, 50)

        #Make Password button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setStyleSheet('background-color: #D0D3D4')
        self.b1.resize(140, 40)
        self.b1.setText('Make password')
        self.b1.move(125, 25)
        self.b1.clicked.connect(self.pass_button)

        #Make Copy to Clipboard button
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setStyleSheet('background-color: #D0D3D4')
        self.b2.resize(100, 40)
        self.b2.setText('Copy')
        self.b2.move(145, 100)
        self.b2.clicked.connect(self.copy_pass)

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
