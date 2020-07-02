import sys
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
QWidget, QDialog)

class ResultTable(QDialog):

    FROM, SUBJECT, DATE = range(3)

    ID, BRAND, MODEL, YEAR, POWER, GEARBOX, COND, FEAT, PRICE = range(9)
    C_ID, C_NAME, C_ADDR, C_BRAND, C_MODEL, C_YEAR, C_COND, C_PRICE = range(8)


    def __init__(self):
        super(ResultTable, self).__init__()
        self.title = 'Результаты поиска'
        self.left = 10
        self.top = 10
        self.width = 720
        self.height = 480

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.dataGroupBox = QGroupBox()
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)

        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)
        self.show()

    def showClientsResult(self, _list):
        self.dataView.setModel(None)
        modelCl = self.createModelCl(self)
        self.dataView.setModel(modelCl)
        for cl in _list:
            self.addClEntry(modelCl, cl.id, cl.name, cl.address, cl.brand, cl.model, cl.year, cl.condition, cl.price)

    def showCarsResult(self, _list):
        self.dataView.setModel(None)
        model = self.createModel(self)
        self.dataView.setModel(model)
        for car in _list:
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


