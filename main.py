import sys
from peewee import *

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QMessageBox

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from DB import Cars, Clients
from AddClientDialog import AddClientDialog


class App(QMainWindow):

    def update(self):
        sum_client=0
        for client in Clients.select():
            sum_client += client.price
        sum_cars=0
        for car in Cars.select():
            sum_cars += car.price
        msg = 'Покупательская способность: ' + str(round(sum_client/sum_cars, 4))
        self.statusBar().showMessage(msg)

    def __init__(self):
        super().__init__()
        self.title = 'CarStore'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initMenu(self):
        mainMenu = self.menuBar()

        carsMenu = mainMenu.addMenu('Авто')

        addCarButton = QAction(QIcon(), 'Добавить', self)
        #addCarButton.setShortcut('Ctrl+N')
        addCarButton.setStatusTip('Add client')
        addCarButton.triggered.connect(self.on_addCar)
        carsMenu.addAction(addCarButton)

        remCarButton = QAction(QIcon(), 'Удалить', self)
        #remCarButton.setShortcut('Ctrl+N')
        remCarButton.setStatusTip('Add client')
        remCarButton.triggered.connect(self.on_remCar)
        carsMenu.addAction(remCarButton)


        clientsMenu = mainMenu.addMenu('Клиенты')

        addClientButton = QAction(QIcon(), 'Добавить', self)
        #addClientButton.setShortcut('Ctrl+N')
        addClientButton.setStatusTip('Add client')
        addClientButton.triggered.connect(self.on_addClient)
        clientsMenu.addAction(addClientButton)

        remClientButton = QAction(QIcon(), 'Удалить', self)
        #remClientButton.setShortcut('Ctrl+N')
        remClientButton.setStatusTip('Add client')
        remClientButton.triggered.connect(self.on_remClient)
        clientsMenu.addAction(remClientButton)


        additMenu = mainMenu.addMenu('Дополнительно')

        updButton = QAction(QIcon(), 'Обновить', self)
        #updButton.setShortcut('Ctrl+N')
        updButton.setStatusTip('Add client')
        updButton.triggered.connect(self.update)
        additMenu.addAction(updButton)

        exitButton = QAction(QIcon(), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        additMenu.addAction(exitButton)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initMenu()

        self.update()
        self.show()

    @pyqtSlot()
    def on_addClient(self):
        dialog = AddClientDialog()
        dialog.exec_()
        self.update()

    def on_remClient(self):
        print("test1")

    def on_addCar(self):
        print("test2")

    def on_remCar(self):
        print("test3")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
