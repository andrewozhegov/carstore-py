import sys
from peewee import *

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QMessageBox, QAction,  QTabWidget,QVBoxLayout, QTreeView, QHBoxLayout, QInputDialog, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from DB import Cars, Clients
from AddClientDialog import AddClientDialog
from ResultTable import ResultTable

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

        self.tabs_widget.updCarsTable()
        self.tabs_widget.updClientsTable()

    def __init__(self):
        super().__init__()
        self.title = 'CarStore'
        self.left = 10
        self.top = 10
        self.width = 720
        self.height = 480
        self.initUI()

    def initMenu(self):
        mainMenu = self.menuBar()

        '''
        carsMenu = mainMenu.addMenu('Авто')

        addCarButton = QAction(QIcon(), 'Добавить', self)
        addCarButton.triggered.connect(self.on_addCar)
        carsMenu.addAction(addCarButton)

        remCarButton = QAction(QIcon(), 'Удалить', self)
        remCarButton.triggered.connect(self.on_remCar)
        carsMenu.addAction(remCarButton)
        '''

        clientsMenu = mainMenu.addMenu('Клиенты')

        addClientButton = QAction(QIcon(), 'Добавить', self)
        addClientButton.triggered.connect(self.on_addClient)
        clientsMenu.addAction(addClientButton)

        remClientButton = QAction(QIcon(), 'Удалить', self)
        remClientButton.triggered.connect(self.on_remClient)
        clientsMenu.addAction(remClientButton)


        additMenu = mainMenu.addMenu('Дополнительно')

        updButton = QAction(QIcon(), 'Обновить', self)
        updButton.triggered.connect(self.update)
        additMenu.addAction(updButton)

        fndButton = QAction(QIcon(), 'Найти покупателя', self)
        fndButton.triggered.connect(self.findClient)
        additMenu.addAction(fndButton)

        exitButton = QAction(QIcon(), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        additMenu.addAction(exitButton)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initMenu()

        self.tabs_widget = TabsWidget(self)
        self.setCentralWidget(self.tabs_widget)

        self.update()
        self.show()

    @pyqtSlot()
    def on_addClient(self):
        dialog = AddClientDialog()
        dialog.exec_()
        self.update()

    def on_remClient(self):
        _id, okPressed = QInputDialog.getInt(self, "Удалить клиента", "Введите ID клиента: ")
        if okPressed:
            cl = Clients.select().where(Clients.id == _id).get()
            cl.delete_instance()
        self.update()

    def findClient(self):
        _id, okPressed = QInputDialog.getInt(self, "Поиск покупателей", "Введите ID авто: ")
        if okPressed:
            car = Cars.select().where(Cars.id == _id).get()
            find_clients = Clients.select().where(
                (Clients.brand == car.brand) &
                (Clients.model == car.model) &
                (Clients.year <= car.year) &
                (Clients.condition >= car.condition) &
                (Clients.price >= car.price)
            )
            res = ResultTable()
            res.showClientsResult(find_clients)
            res.exec_()


class TabsWidget(QWidget):

    ID, BRAND, MODEL, YEAR, POWER, GEARBOX, COND, FEAT, PRICE = range(9)
    C_ID, C_NAME, C_ADDR, C_BRAND, C_MODEL, C_YEAR, C_COND, C_PRICE = range(8)

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tabCars = QWidget()
        self.tabClients = QWidget()

        self.tabs.addTab(self.tabCars,"Авто")
        self.tabs.addTab(self.tabClients,"Клиенты")

        self.initCarsTable()
        self.initClientsTable()

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def initCarsTable(self):
        self.tabCars.layout = QVBoxLayout(self)

        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)

        self.tabCars.layout.addWidget(self.dataView)
        self.tabCars.setLayout(self.tabCars.layout)

    def updCarsTable(self):
        self.dataView.setModel(None)
        model = self.createModel(self)
        self.dataView.setModel(model)
        for car in Cars.select():
            self.addCarEntry(model, car.id, car.brand, car.model, car.year, car.engine_power, car.auto_gearbox, car.condition, car.features, car.price)

    def createModel(self, parent):
        model = QStandardItemModel(0, 9, parent)
        model.setHeaderData(self.ID, Qt.Horizontal, "id")
        model.setHeaderData(self.BRAND, Qt.Horizontal, "Марка")
        model.setHeaderData(self.MODEL, Qt.Horizontal, "Модель")
        model.setHeaderData(self.YEAR, Qt.Horizontal, "Год")
        model.setHeaderData(self.POWER, Qt.Horizontal, "Мощность")
        model.setHeaderData(self.GEARBOX, Qt.Horizontal, "Коробка")
        model.setHeaderData(self.COND, Qt.Horizontal, "Пробег")
        model.setHeaderData(self.FEAT, Qt.Horizontal, "Информ")
        model.setHeaderData(self.PRICE, Qt.Horizontal, "Цена")
        return model

    def addCarEntry(self, model, _id, brand, _model, year, power, gear, cond, feat, price):
        model.insertRow(0)
        model.setData(model.index(0, self.ID), _id)
        model.setData(model.index(0, self.BRAND), brand)
        model.setData(model.index(0, self.MODEL), _model)
        model.setData(model.index(0, self.YEAR), year)
        model.setData(model.index(0, self.POWER), power)
        model.setData(model.index(0, self.GEARBOX), gear)
        model.setData(model.index(0, self.COND), cond)
        model.setData(model.index(0, self.FEAT), feat)
        model.setData(model.index(0, self.PRICE), price)


    def initClientsTable(self):
        self.tabClients.layout = QVBoxLayout(self)

        self.dataViewCl = QTreeView()
        self.dataViewCl.setRootIsDecorated(False)
        self.dataViewCl.setAlternatingRowColors(True)

        self.tabClients.layout.addWidget(self.dataViewCl)
        self.tabClients.setLayout(self.tabClients.layout)

    def updClientsTable(self):
        self.dataViewCl.setModel(None)
        modelCl = self.createModelCl(self)
        self.dataViewCl.setModel(modelCl)
        for cl in Clients.select():
            self.addClEntry(modelCl, cl.id, cl.name, cl.address, cl.brand, cl.model, cl.year, cl.condition, cl.price)

    def createModelCl(self,parent):
        model = QStandardItemModel(0, 8, parent)
        model.setHeaderData(self.C_ID, Qt.Horizontal, "id")
        model.setHeaderData(self.C_NAME, Qt.Horizontal, "ФИО")
        model.setHeaderData(self.C_ADDR, Qt.Horizontal, "Адрес")
        model.setHeaderData(self.C_BRAND, Qt.Horizontal, "Марка")
        model.setHeaderData(self.C_MODEL, Qt.Horizontal, "Модель")
        model.setHeaderData(self.C_COND, Qt.Horizontal, "Пробег")
        model.setHeaderData(self.C_PRICE, Qt.Horizontal, "Цена")
        return model

    def addClEntry(self, model, _id, name, addr, brand, _model, year, cond, price):
        model.insertRow(0)
        model.setData(model.index(0, self.C_ID), _id)
        model.setData(model.index(0, self.C_NAME), name)
        model.setData(model.index(0, self.C_ADDR), addr)
        model.setData(model.index(0, self.C_BRAND), brand)
        model.setData(model.index(0, self.C_MODEL), _model)
        model.setData(model.index(0, self.C_YEAR), year)
        model.setData(model.index(0, self.C_COND), cond)
        model.setData(model.index(0, self.C_PRICE), price)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
