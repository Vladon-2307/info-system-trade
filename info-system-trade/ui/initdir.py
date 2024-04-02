import re

from PyQt5.QtWidgets import QWidget, QMessageBox
from .ui_initdir import Ui_Form
from database import initDir


class InitDir(QWidget, Ui_Form):
    def __init__(self, id: int = -1, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.id = id
        self.set()

    def set(self):
        self.dir_name.editingFinished.connect(self.dir_nameValidtor)
        self.btnSave.clicked.connect(self.save)
        self.dir_nameError.setText('')
        self.show()

    def dir_nameValidtor(self):
        reg = "^[.*?:<>\"\\\\|/]+$"
        pattern = re.compile(reg)
        value = self.dir_name.text()
        if value == '' or value == None:
            self.dir_nameError.setText('Название директории не может быть пустым')
        elif pattern.search(value) is not None:
            self.dir_nameError.setText('Не коректное название директории')
        else:
            self.dir_nameError.setText('')

    def save(self):
        self.dir_nameValidtor()
        value = self.dir_name.text()
        if value != '' and value != None:
            isOk, message = initDir(self.id, value)

            if isOk == False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(message)
                msg.setWindowTitle("Error")
                msg.exec_()

            if isOk == True:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Коталог успешно создан")
                msg.setWindowTitle("Success")
                msg.exec_()
                self.parent.reload()
                self.close()

