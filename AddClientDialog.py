import sys

from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout)


class AddClientDialog(QDialog):

    NumGridRows = 7
    NumButtons = 4

    def __init__(self):
        super(AddClientDialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)
        self.setWindowTitle("Добавить клиента")
        self.show()

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Данные клиета")
        layout = QFormLayout()

        self.input_name = QLineEdit()
        self.input_name.setObjectName("input_name")
        self.input_address = QLineEdit()
        self.input_address.setObjectName("input_address")
        self.input_brand = QLineEdit()
        self.input_brand.setObjectName("input_brand")
        self.input_model = QLineEdit()
        self.input_model.setObjectName("input_model")
        self.input_year = QLineEdit()
        self.input_year.setObjectName("input_year")
        self.input_cond = QLineEdit()
        self.input_cond.setObjectName("input_cond")
        self.input_price = QLineEdit()
        self.input_price.setObjectName("input_price")

        layout.addRow(QLabel("Имя"), self.input_name)
        layout.addRow(QLabel("Адрес"), self.input_address)
        layout.addRow(QLabel("Марка"), self.input_brand)
        layout.addRow(QLabel("Медель"), self.input_model)
        layout.addRow(QLabel("Год"), self.input_year)
        layout.addRow(QLabel("Состояние"), self.input_cond)
        layout.addRow(QLabel("Бюджет"), self.input_price)

        self.formGroupBox.setLayout(layout)

    @pyqtSlot()
    def accept(self):
        Clients.create(
            name=self.input_name.text(),
            address=self.input_address.text(),
            brand=self.input_brand.text(),
            model=self.input_model.text(),
            year=self.input_year.text(),
            condition=self.input_cond.text(),
            price=self.input_price.text())
        self.close()
