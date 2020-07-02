import sys
from peewee import *

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QMessageBox

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from DB import Cars, Clients
from AddClientDialog import AddClientDialog


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'CarStore'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('button', self)
        button.setToolTip('don\'t push')
        button.move(100, 70)
        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        dialog = AddClientDialog()
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
