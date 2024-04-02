from PyQt5.QtWidgets import QWidget, QMessageBox

from .ui_edit import Ui_Form
from database import getById, create, update


class Edit(QWidget, Ui_Form):
    def __init__(self, id: int = -1, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.id = id
        self.set()

    def set(self):
        self.name.editingFinished.connect(self.errorName)
        if self.id == -1:
            self.btnSave.clicked.connect(self.add)
            self.nameError.setVisible(True)
            self.btnSave.setDisabled(True)
        else:
            self.btnSave.clicked.connect(self.edit)
            self.nameError.setVisible(False)
            self.btnSave.setDisabled(False)
            self.initData()
        self.show()

    def initData(self):
        self.data = getById(self.id)
        self.title.setText("обновление контрагента")
        self.name.setText(str(self.data["name"]))
        self.account_number.setText(self.data["account_number"])
        self.bank_name.setText(str(self.data["bank_name"]))
        self.code_bank.setText(str(self.data["code_bank"]))
        self.legal_address.setText(str(self.data["legal_address"]))
        self.mailing_address.setText(str(self.data["mailing_address"]))
        self.phone.setText(str(self.data["phone"]))
        self.email.setText(str(self.data["email"]))
        self.unn.setText(str(self.data["unn"]))
        self.okpo.setText(str(self.data["okpo"]))

    def add(self):
        isOk, message = create(name=self.name.text(), account_number=self.account_number.text(), bank_name=self.bank_name.text(),
               code_bank=self.code_bank.text(), legal_address=self.legal_address.text(),
               mailing_address=self.mailing_address.text(), phone=self.phone.text(),
               email=self.email.text(), unn= self.unn.text(), okpo=self.okpo.text())

        if isOk == False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(message)
            msg.setWindowTitle("Error")
            msg.exec_()

        if isOk == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Контрагент успешно сохранён")
            msg.setWindowTitle("Success")
            msg.exec_()
            self.parent.search()
            self.close()

    def edit(self):
        isOk, message = update(id=self.id, name=self.name.text(), account_number=self.account_number.text(),
                               bank_name=self.bank_name.text(),
                               code_bank=self.code_bank.text(), legal_address=self.legal_address.text(),
                               mailing_address=self.mailing_address.text(), phone=self.phone.text(),
                               email=self.email.text(), unn=self.unn.text(), okpo=self.okpo.text())

        if isOk == False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(message)
            msg.setWindowTitle("Error")
            msg.exec_()

        if isOk == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Контрагент успешно сохранён")
            msg.setWindowTitle("Success")
            msg.exec_()
            self.parent.reload()
            self.parent.parent.search()
            self.close()

    def errorName(self):
        name = self.name.text()
        if name == '' or name is None:
            self.nameError.setVisible(True)
            self.btnSave.setDisabled(True)
        else:
            self.nameError.setVisible(False)
            self.btnSave.setDisabled(False)
