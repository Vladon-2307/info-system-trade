from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView, QMainWindow
from database import getData
from .ui_main import Ui_MainWindow
from .info import Info
from .edit import Edit


class App(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.inf = None
        self.set()

    def set(self):
        self.lSearch.editingFinished.connect(self.search)
        self.isSort.stateChanged.connect(self.search)
        self.btnAdd.clicked.connect(self.openAdd)
        self.show()
        self.initTable()


    def initTable(self, search: str = '', sort: bool = False):
        data = getData(search, sort)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(data))
        headers = ['name', 'phone', 'email', 'last_call_date']
        headersRU = ['название', 'телефон', 'почта', 'дата звонка']

        self.tableWidget.setHorizontalHeaderLabels(headersRU)
        self.tableWidget.itemDoubleClicked.connect(self.doubleClikRow)


        for row in range(0, len(data)):
            for key in data[row].keys():
                if key == "id": continue
                item = ''
                if data[row][key] is not None:
                    item = str(data[row][key])

                self.tableWidget.setItem(row, headers.index(key), QTableWidgetItem(item))

            self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(str(data[row]["id"])))



        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)


    def search(self):
        search = self.lSearch.text()
        sort = False
        if self.isSort.checkState() == 2 : sort = True
        self.initTable(search, sort)



    def doubleClikRow(self, item):
        id = int(self.tableWidget.verticalHeaderItem(item.row()).text())
        if self.inf != None:
            self.inf.close()

        self.inf = Info(id, parent=self)

    def openAdd(self):
        if self.inf != None:
            self.inf.close()

        self.inf = Edit(id=-1, parent=self)
