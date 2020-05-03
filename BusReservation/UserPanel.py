import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QModelIndex,QDateTime
from util import *

class UserWindow(QtWidgets.QWidget):

    def __init__(self, userId):
        QtWidgets.QWidget.__init__(self)
        self.userId = userId

        self.setupUi()
        self.initPlanTable()

        self.planReserveTable.itemSelectionChanged.connect(self.initSeats)
        self.reserveBtn.clicked.connect(self.reservePlan)

    def setupUi(self):
        self.setObjectName("User")
        self.resize(489, 397)
        self.planReserveGB = QtWidgets.QGroupBox(self)
        self.planReserveGB.setGeometry(QtCore.QRect(10, 10, 471, 381))
        self.planReserveGB.setObjectName("planReserveGB")
        self.splitter_2 = QtWidgets.QSplitter(self.planReserveGB)
        self.splitter_2.setGeometry(QtCore.QRect(10, 20, 451, 351))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")

        #Plan Reservation Table
        self.planReserveTable = QtWidgets.QTableWidget(0,7,self.splitter_2)
        self.planReserveTable.setObjectName("planReserveTable")
        self.planReserveTable.setHorizontalHeaderLabels(['Plan Id','Bus Id' , 'Origin' , 'Destination' , 'Departure' , 'Arrival' , 'Remained Seats'])
        self.planReserveTable.setAlternatingRowColors(True)
        self.planReserveTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.planReserveTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.planReserveTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)

        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.seatLabel = QtWidgets.QLabel(self.splitter)
        self.seatLabel.setObjectName("seatLabel")
        self.seatCombo = QtWidgets.QComboBox(self.splitter)
        self.seatCombo.setObjectName("seatCombo")
        self.reserveBtn = QtWidgets.QPushButton(self.splitter_2)
        self.reserveBtn.setEnabled(False)
        self.reserveBtn.setObjectName("reserveBtn")
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("User", "User Panel"))
        self.planReserveGB.setTitle(_translate("User", "Plan Reservation"))
        self.seatLabel.setText(_translate("User", "Empty Seats:"))
        self.reserveBtn.setText(_translate("User", "Reserve"))

    def initPlanTable(self):
        index = 0
        query = QSqlQuery()
        query.exec_("""select * from(select *,
(select (capacity - (select count(*) as ReservedSeats from Reservation where planId = tbt.planId)) as Remained from Bus as b where b.id = tbt.busId) as RemainedSeats
from (select id as planId,busId,(select c.name from City as c where c.id == p.originId) as Origin , (select c.name from City as c where c.id == p.destId) as Destination , dptDate , arvDate from Plan as p)
as tbt)as tbt2 where tbt2.RemainedSeats > 0""")

        self.planReserveTable.clear()
        self.planReserveTable.setHorizontalHeaderLabels(['Plan Id','Bus Id' , 'Origin' , 'Destination' , 'Departure' , 'Arrival' , 'Remained Seats'])
        
        while query.next():
            self.planReserveTable.setRowCount(index + 1)
            for i in range(7):
                self.planReserveTable.setItem(index, i, QTableWidgetItem(str(query.value(i))))

            index += 1

    def initSeats(self):
        self.seatCombo.clear()
        self.reserveBtn.setEnabled(True)

        selected = self.planReserveTable.currentIndex()
        if not selected.isValid() or len(self.planReserveTable.selectedItems()) < 1:
            return

        self.planId = int(self.planReserveTable.selectedItems()[0].text())
        
        query = QSqlQuery()
        query.exec_(f"select seatNumber from Reservation where planId = {self.planId}")

        reserved_seats = []
        while query.next():
            reserved_seats.append(query.value(0))

        query = QSqlQuery()
        query.exec_(f"select capacity from Bus as b inner join Plan as p on b.id = p.busId where p.id = {self.planId}")
        query.next()

        capacity = query.value(0)

        self.seatCombo.addItems([str(i) for i in range(1,capacity+1) if i not in reserved_seats])

    def reservePlan(self):
        query = QSqlQuery()
        query.prepare("insert into Reservation(userId,planId,seatNumber) values(:userId,:planId,:seatNumber)")
        query.bindValue(":userId" , self.userId)
        query.bindValue(":planId" , self.planId)
        query.bindValue(":seatNumber" , int(self.seatCombo.currentText()))
        if query.exec_() == False:
            criticalMessage("Reservation failed!")
        else:
            self.seatCombo.clear()
            self.initPlanTable()
            self.reserveBtn.setEnabled(False)
