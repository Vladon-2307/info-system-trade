# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 399)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(130, 0))
        self.label.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name = QtWidgets.QLabel(Form)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(130, 0))
        self.label_2.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.account_number = QtWidgets.QLabel(Form)
        self.account_number.setObjectName("account_number")
        self.horizontalLayout_2.addWidget(self.account_number)
        self.bank_name = QtWidgets.QLabel(Form)
        self.bank_name.setObjectName("bank_name")
        self.horizontalLayout_2.addWidget(self.bank_name)
        self.code_bank = QtWidgets.QLabel(Form)
        self.code_bank.setObjectName("code_bank")
        self.horizontalLayout_2.addWidget(self.code_bank)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(130, 0))
        self.label_3.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.legal_address = QtWidgets.QLabel(Form)
        self.legal_address.setObjectName("legal_address")
        self.horizontalLayout_3.addWidget(self.legal_address)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(130, 0))
        self.label_4.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.mailing_address = QtWidgets.QLabel(Form)
        self.mailing_address.setObjectName("mailing_address")
        self.horizontalLayout_4.addWidget(self.mailing_address)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(130, 0))
        self.label_5.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.phone = QtWidgets.QLabel(Form)
        self.phone.setObjectName("phone")
        self.horizontalLayout_5.addWidget(self.phone)
        self.last_call_date = QtWidgets.QLabel(Form)
        self.last_call_date.setObjectName("last_call_date")
        self.horizontalLayout_5.addWidget(self.last_call_date)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(130, 0))
        self.label_6.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.email = QtWidgets.QLabel(Form)
        self.email.setObjectName("email")
        self.horizontalLayout_6.addWidget(self.email)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(130, 0))
        self.label_7.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.unn = QtWidgets.QLabel(Form)
        self.unn.setObjectName("unn")
        self.horizontalLayout_7.addWidget(self.unn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setMinimumSize(QtCore.QSize(130, 0))
        self.label_8.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.okpo = QtWidgets.QLabel(Form)
        self.okpo.setObjectName("okpo")
        self.horizontalLayout_8.addWidget(self.okpo)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnCall = QtWidgets.QPushButton(Form)
        self.btnCall.setObjectName("btnCall")
        self.horizontalLayout_10.addWidget(self.btnCall)
        self.btnReload = QtWidgets.QPushButton(Form)
        self.btnReload.setObjectName("btnReload")
        self.horizontalLayout_10.addWidget(self.btnReload)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btnEdit = QtWidgets.QPushButton(Form)
        self.btnEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.btnEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnEdit.setObjectName("btnEdit")
        self.horizontalLayout_9.addWidget(self.btnEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.btnInitDir = QtWidgets.QPushButton(Form)
        self.btnInitDir.setMinimumSize(QtCore.QSize(100, 0))
        self.btnInitDir.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnInitDir.setObjectName("btnInitDir")
        self.horizontalLayout_9.addWidget(self.btnInitDir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.btnDelete = QtWidgets.QPushButton(Form)
        self.btnDelete.setMinimumSize(QtCore.QSize(80, 0))
        self.btnDelete.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnDelete.setStyleSheet("background: red;\n"
"color: #fff;")
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_9.addWidget(self.btnDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.tableFiles = QtWidgets.QTableWidget(Form)
        self.tableFiles.setShowGrid(True)
        self.tableFiles.setObjectName("tableFiles")
        self.tableFiles.setColumnCount(0)
        self.tableFiles.setRowCount(0)
        self.tableFiles.horizontalHeader().setVisible(False)
        self.tableFiles.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableFiles)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "info system trade - counterparty"))
        self.label.setText(_translate("Form", "Название"))
        self.name.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "Банк"))
        self.account_number.setText(_translate("Form", "TextLabel"))
        self.bank_name.setText(_translate("Form", "TextLabel"))
        self.code_bank.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "Юридический адрес"))
        self.legal_address.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "Почтовый адрес"))
        self.mailing_address.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "Телефон"))
        self.phone.setText(_translate("Form", "TextLabel"))
        self.last_call_date.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "Почта"))
        self.email.setText(_translate("Form", "TextLabel"))
        self.label_7.setText(_translate("Form", "УНН"))
        self.unn.setText(_translate("Form", "TextLabel"))
        self.label_8.setText(_translate("Form", "ОКПО"))
        self.okpo.setText(_translate("Form", "TextLabel"))
        self.btnCall.setText(_translate("Form", "установить новую дату звонка"))
        self.btnReload.setText(_translate("Form", "обновить"))
        self.btnEdit.setText(_translate("Form", "Редактировать"))
        self.btnInitDir.setText(_translate("Form", "создать католог"))
        self.btnDelete.setText(_translate("Form", "Удалить"))
