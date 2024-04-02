import os

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox
from .ui_info import Ui_Form
from .edit import Edit
from .initdir import InitDir
from database import getFiles, getById, delete, updateCallDate, basePath

class Info(QWidget, Ui_Form):
    def __init__(self, id: int, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.id = id
        self.inf = None
        self.set()

    def set(self):
        self.data = getById(self.id)
        self.initData()
        self.btnReload.clicked.connect(self.reload)
        self.btnDelete.clicked.connect(self.delete)
        self.btnEdit.clicked.connect(self.openEdit)
        self.btnCall.clicked.connect(self.updateDateCall)
        self.show()

    def initData(self):
        if self.data is None:
            return
        for key in self.data.keys():
            if key == "id" or key == "dir_name":
                continue
            getattr(self, key).setText(str(self.data[key]))

        if self.data["dir_name"] != None:
            self.btnInitDir.setText('открыть католог')
            self.btnInitDir.disconnect()
            self.btnInitDir.clicked.connect(self.openDir)
            self.tableFiles.setColumnCount(1)
            files = getFiles(self.data["dir_name"])
            self.tableFiles.setRowCount(len(files))
            for row in range(0, len(files)):
                self.tableFiles.setItem(row, 0, QTableWidgetItem(str(files[row])))
            self.tableFiles.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableFiles.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableFiles.setSelectionMode(QAbstractItemView.SingleSelection)

        else:
            self.btnInitDir.disconnect()
            self.btnInitDir.clicked.connect(self.initDir)

    def reload(self):
        self.data = getById(self.id)
        self.initData()

    def delete(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Вы дествительно хотите удалить?")
        msg.setWindowTitle("Delete")
        msg.addButton('Да', QMessageBox.YesRole)
        msg.addButton('Нет', QMessageBox.NoRole)
        res = msg.exec_()
        if res == 0:
            res2 = delete(self.id)
            if res2 == True:
                msg2 = QMessageBox()
                msg2.setIcon(QMessageBox.Information)
                msg2.setText("Контрагент успешно удалён")
                msg2.setWindowTitle("Success")
                msg2.exec_()
                self.parent.search()
                self.close()


    def openDir(self):
        os.system("explorer.exe " + basePath + str(self.data["dir_name"]))

    def initDir(self):
        if self.inf != None:
            self.inf.close()

        self.inf = InitDir(id=self.id, parent=self)

    def openEdit(self):
        if self.inf != None:
            self.inf.close()

        self.inf = Edit(id=self.id, parent=self)

    def updateDateCall(self):
        res = updateCallDate(self.id)
        if res == True:
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Information)
            msg2.setText("Дата посленднего звонка обновлена")
            msg2.setWindowTitle("Success")
            msg2.exec_()
            self.reload()
            self.parent.search()
