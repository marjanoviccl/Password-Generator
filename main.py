__author__ = 'Luka Marjanović'

import sys, pyperclip
import random, string
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QAction, QLineEdit, QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QGuiApplication

def make_pass(number):
    characters = string.ascii_letters + string.punctuation  + string.digits
    try:
        password =  "".join(random.choice(characters) for i in range(number))

        return password
    except TypeError:
        pass

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def pass_button(self):
        global FINAL

        try:
            value = self.textbox.text()
            value = int(value)
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Only numbers are accepted!")
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Ok)

            popup = msg.exec_()

        FINAL = make_pass(value)
        self.label.setText(FINAL)
        self.label.move(165, 200)
        self.update()

    def copy_pass(self):
        try:
            pyperclip.copy(FINAL)
            spam = pyperclip.paste()
        except:
            pass

    def initUI(self):
        #Creating the Window
        self.setStyleSheet('background-color: #5D6D7E')
        self.setGeometry(500, 200, 400, 300)
        self.setFixedSize(self.size())
        self.setWindowTitle('Password Generator')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label = QtWidgets.QLabel(self)
        self.label.move(50, 50)

        #Textbox to enter Desired Password length
        self.textbox = QLineEdit(self)
        self.textbox.resize(140, 40)
        self.textbox.move(125, 70)

        #Make Password button
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setStyleSheet('background-color: #D0D3D4')
        self.b2.resize(140, 40)
        self.b2.setText('Create Password')
        self.b2.move(125, 150)
        self.b2.clicked.connect(self.pass_button)

        #Make Copy to Clipboard button
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setStyleSheet('background-color: #D0D3D4')
        self.b3.resize(100, 40)
        self.b3.setText('Copy')
        self.b3.move(145, 230)
        self.b3.clicked.connect(self.copy_pass)

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()