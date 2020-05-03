import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QModelIndex,QDateTime
from util import *

class AdminWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUI()

        

        #init
        self.cities = dict()
        self.buses = []
        self.initCityTable()
        self.initBusTable()
        self.initReservationForm()
        self.initPlanTable()
        self.initReservationTable()



        #connect
        self.addCityBtn.clicked.connect(lambda : self.insertCity(self.cityNameLineEdit.text()))
        self.deleteCityBtn.clicked.connect(self.deleteCity)
        self.addBusBtn.clicked.connect(lambda: self.insertBus(self.capacitySpin.value(),self.driverNameLineEdit.text()))
        self.deleteBusBtn.clicked.connect(self.deleteBus)
        self.addPlanBtn.clicked.connect(self.insertPlan)
        self.deletePlanBtn.clicked.connect(self.deletePlan)
        self.deleteReservationBtn.clicked.connect(self.deleteReservation)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setupUI(self):
        self.setWindowTitle('Admin Panel')
        self.setObjectName('Admin')
        self.resize(711, 787)
        self.addPlanGB = QtWidgets.QGroupBox(self)
        self.addPlanGB.setGeometry(QtCore.QRect(20, 10, 391, 321))
        self.addPlanGB.setObjectName("addPlanGB")
        self.splitter_6 = QtWidgets.QSplitter(self.addPlanGB)
        self.splitter_6.setGeometry(QtCore.QRect(10, 20, 371, 291))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter = QtWidgets.QSplitter(self.splitter_6)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.originLabel = QtWidgets.QLabel(self.splitter)
        self.originLabel.setObjectName("originLabel")
        self.originCombo = QtWidgets.QComboBox(self.splitter)
        self.originCombo.setObjectName("originCombo")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.destinationLabel = QtWidgets.QLabel(self.splitter_2)
        self.destinationLabel.setObjectName("destinationLabel")
        self.destCombo = QtWidgets.QComboBox(self.splitter_2)
        self.destCombo.setObjectName("destCombo")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.busLabel = QtWidgets.QLabel(self.splitter_3)
        self.busLabel.setObjectName("busLabel")
        self.busCombo = QtWidgets.QComboBox(self.splitter_3)
        self.busCombo.setObjectName("busCombo")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.dptLabel = QtWidgets.QLabel(self.splitter_4)
        self.dptLabel.setObjectName("dptLabel")
        self.dptDatePicker = QtWidgets.QDateTimeEdit(self.splitter_4)
        self.dptDatePicker.setObjectName("dptDatePicker")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.arvLabel = QtWidgets.QLabel(self.splitter_5)
        self.arvLabel.setObjectName("arvLabel")
        self.arvDatePicker = QtWidgets.QDateTimeEdit(self.splitter_5)
        self.arvDatePicker.setObjectName("arvDatePicker")
        self.addPlanBtn = QtWidgets.QPushButton(self.splitter_6)
        self.addPlanBtn.setObjectName("addPlanBtn")
        self.addCityGB = QtWidgets.QGroupBox(self)
        self.addCityGB.setGeometry(QtCore.QRect(420, 10, 281, 101))
        self.addCityGB.setObjectName("addCityGB")
        self.splitter_8 = QtWidgets.QSplitter(self.addCityGB)
        self.splitter_8.setGeometry(QtCore.QRect(10, 20, 251, 71))
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.cityNameLabel = QtWidgets.QLabel(self.splitter_7)
        self.cityNameLabel.setObjectName("cityNameLabel")
        self.cityNameLineEdit = QtWidgets.QLineEdit(self.splitter_7)
        self.cityNameLineEdit.setObjectName("cityNameLineEdit")
        self.addCityBtn = QtWidgets.QPushButton(self.splitter_8)
        self.addCityBtn.setObjectName("addCityBtn")
        self.addBusGB = QtWidgets.QGroupBox(self)
        self.addBusGB.setGeometry(QtCore.QRect(420, 110, 281, 141))
        self.addBusGB.setObjectName("addBusGB")
        self.splitter_11 = QtWidgets.QSplitter(self.addBusGB)
        self.splitter_11.setGeometry(QtCore.QRect(10, 20, 261, 111))
        self.splitter_11.setOrientation(QtCore.Qt.Vertical)
        self.splitter_11.setObjectName("splitter_11")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.driverNameLabel = QtWidgets.QLabel(self.splitter_9)
        self.driverNameLabel.setObjectName("driverNameLabel")
        self.driverNameLineEdit = QtWidgets.QLineEdit(self.splitter_9)
        self.driverNameLineEdit.setObjectName("driverNameLineEdit")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.capacityLabel = QtWidgets.QLabel(self.splitter_10)
        self.capacityLabel.setObjectName("capacityLabel")
        self.capacitySpin = QtWidgets.QSpinBox(self.splitter_10)
        self.capacitySpin.setMinimum(20)
        self.capacitySpin.setMaximum(50)
        self.capacitySpin.setSingleStep(5)
        self.capacitySpin.setObjectName("capacitySpin")
        self.addBusBtn = QtWidgets.QPushButton(self.splitter_11)
        self.addBusBtn.setObjectName("addBusBtn")
        self.planGB = QtWidgets.QGroupBox(self)
        self.planGB.setGeometry(QtCore.QRect(20, 600, 681, 181))
        self.planGB.setObjectName("planGB")
        self.splitter_12 = QtWidgets.QSplitter(self.planGB)
        self.splitter_12.setGeometry(QtCore.QRect(10, 20, 661, 151))
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")

        #Table Plans
        self.planTable = QtWidgets.QTableWidget(0,7,self.splitter_12)
        self.planTable.setObjectName("planTable")
        self.planTable.setHorizontalHeaderLabels(['Plan Id','Bus Id' , 'Origin' , 'Destination' , 'Departure' , 'Arrival' , 'Remained Seats'])
        self.planTable.setAlternatingRowColors(True)
        self.planTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.planTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.planTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)

        self.deletePlanBtn = QtWidgets.QPushButton(self.splitter_12)
        self.deletePlanBtn.setObjectName("deletePlanBtn")
        self.cityGB = QtWidgets.QGroupBox(self)
        self.cityGB.setGeometry(QtCore.QRect(420, 260, 281, 161))
        self.cityGB.setObjectName("cityGB")
        self.splitter_13 = QtWidgets.QSplitter(self.cityGB)
        self.splitter_13.setGeometry(QtCore.QRect(10, 20, 256, 131))
        self.splitter_13.setOrientation(QtCore.Qt.Vertical)
        self.splitter_13.setObjectName("splitter_13")

        #Table of Cities
        self.cityTable = QtWidgets.QTableWidget(0,1,self.splitter_13)
        self.cityTable.setObjectName("cityTable")
        self.cityTable.setHorizontalHeaderLabels(['Name'])
        self.cityTable.setAlternatingRowColors(True)
        self.cityTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.cityTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.cityTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)


        self.deleteCityBtn = QtWidgets.QPushButton(self.splitter_13)
        self.deleteCityBtn.setObjectName("deleteCityBtn")
        self.busGB = QtWidgets.QGroupBox(self)
        self.busGB.setGeometry(QtCore.QRect(420, 430, 281, 171))
        self.busGB.setObjectName("busGB")
        self.splitter_14 = QtWidgets.QSplitter(self.busGB)
        self.splitter_14.setGeometry(QtCore.QRect(10, 20, 256, 141))
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName("splitter_14")

        #Table of Buses
        self.busTable = QtWidgets.QTableWidget(0,3,self.splitter_14)
        self.busTable.setObjectName("busTable")
        self.busTable.setHorizontalHeaderLabels(['Bus Id' , 'Capacity' , 'Driver Name'])
        self.busTable.setAlternatingRowColors(True)
        self.busTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.busTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.busTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)


        self.deleteBusBtn = QtWidgets.QPushButton(self.splitter_14)
        self.deleteBusBtn.setObjectName("deleteBusBtn")
        self.reserveGB = QtWidgets.QGroupBox(self)
        self.reserveGB.setGeometry(QtCore.QRect(20, 340, 391, 261))
        self.reserveGB.setObjectName("reserveGB")
        self.splitter_15 = QtWidgets.QSplitter(self.reserveGB)
        self.splitter_15.setGeometry(QtCore.QRect(10, 20, 371, 231))
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName("splitter_15")

        #Table of Reservations
        self.reserveTable = QtWidgets.QTableWidget(0,5,self.splitter_15)
        self.reserveTable.setObjectName("reserveTable")
        self.reserveTable.setHorizontalHeaderLabels(['Reservation Id' , 'User Id' , 'Plan Id' , 'Ticket Owner Name' , 'Reserved Seat Number'])
        self.reserveTable.setAlternatingRowColors(True)
        self.reserveTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.reserveTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.reserveTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)

        self.deleteReservationBtn = QtWidgets.QPushButton(self.splitter_15)
        self.deleteReservationBtn.setObjectName("deleteReservationBtn")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Admin", "Admin Panel"))
        self.addPlanGB.setTitle(_translate("Admin", "Add Plan"))
        self.originLabel.setText(_translate("Admin", "Origin:"))
        self.destinationLabel.setText(_translate("Admin", "Destination:"))
        self.busLabel.setText(_translate("Admin", "Available Bus:"))
        self.dptLabel.setText(_translate("Admin", "Departure:"))
        self.arvLabel.setText(_translate("Admin", "Arrival:"))
        self.addPlanBtn.setText(_translate("Admin", "Add Plan"))
        self.addCityGB.setTitle(_translate("Admin", "Add City"))
        self.cityNameLabel.setText(_translate("Admin", "Name:"))
        self.addCityBtn.setText(_translate("Admin", "Add City"))
        self.addBusGB.setTitle(_translate("Admin", "Add Bus"))
        self.driverNameLabel.setText(_translate("Admin", "Driver Name:"))
        self.capacityLabel.setText(_translate("Admin", "Capacity:"))
        self.addBusBtn.setText(_translate("Admin", "Add Bus"))
        self.planGB.setTitle(_translate("Admin", "Plans List"))
        self.deletePlanBtn.setText(_translate("Admin", "Delete Plan"))
        self.cityGB.setTitle(_translate("Admin", "City List"))
        self.deleteCityBtn.setText(_translate("Admin", "Delete City"))
        self.busGB.setTitle(_translate("Admin", "Bus List"))
        self.deleteBusBtn.setText(_translate("Admin", "Delete Bus"))
        self.reserveGB.setTitle(_translate("Admin", "Reservation List"))
        self.deleteReservationBtn.setText(_translate("Admin", "Delete Reservation"))

    def initCityTable(self):
        index = 0
        query = QSqlQuery()
        query.exec_("select * from City")
        self.cityTable.clear()
        self.cities.clear()
        self.cityTable.setHorizontalHeaderLabels(['Name'])

        while query.next():
            id = query.value(0)
            name = query.value(1)
            #print(id,name)

            self.cities[name] = id
            self.cityTable.setRowCount(index + 1)
            self.cityTable.setItem(index, 0, QTableWidgetItem(name))

            index += 1

    def insertCity(self,name):
        if name != "" and name not in self.cities.keys():
             query = QSqlQuery()
             query.prepare("insert into City(name) values(:cityName)")
             query.bindValue(":cityName" , name)
             if query.exec_() == False:
                 criticalMessage("Could not insert into City table")
             else:
                 self.initCityTable()
                 self.cityNameLineEdit.clear()
                 self.initReservationForm()
        else:
            criticalMessage("Could not insert into City table")

    def deleteCity(self):
        selected = self.cityTable.currentIndex()
        if not selected.isValid() or len(self.cityTable.selectedItems()) < 1:
            return

        name = self.cityTable.selectedItems()[0].text()
        query = QSqlQuery()
        query.prepare("delete from City where id = :id")
        query.bindValue(":id",self.cities[name])
        if query.exec_() == False:
            criticalMessage("Could not delete this city from table")
        else:
            self.cityTable.removeRow(selected.row())
            self.cityTable.setCurrentIndex(QModelIndex())
            self.initCityTable()
            self.initReservationForm()

    def initBusTable(self):
        index = 0
        query = QSqlQuery()
        query.exec_("select * from Bus")
        self.busTable.clear()
        self.buses.clear()
        self.busTable.setHorizontalHeaderLabels(['Bus Id' , 'Capacity' , 'Driver Name'])

        while query.next():
            id = query.value(0)
            capacity = query.value(1)
            driverName = query.value(2)
            #print(id,capacity,driverName)

            self.buses.append(id)
            self.busTable.setRowCount(index + 1)
            self.busTable.setItem(index, 0, QTableWidgetItem(str(id)))
            self.busTable.setItem(index, 1, QTableWidgetItem(str(capacity)))
            self.busTable.setItem(index, 2, QTableWidgetItem(driverName))

            index += 1

    def insertBus(self,capacity,driverName):
        if driverName != "":
             query = QSqlQuery()
             query.prepare("insert into Bus(capacity,driverName) values(:cap,:name)")
             query.bindValue(":cap" , capacity)
             query.bindValue(":name", driverName)
             if query.exec_() == False:
                 criticalMessage("Could not insert into Bus table")
             else:
                 self.initBusTable()
                 self.driverNameLineEdit.clear()
                 self.initReservationForm()
        else:
            criticalMessage("Could not insert into Bus table")

    def deleteBus(self):
        selected = self.busTable.currentIndex()
        if not selected.isValid() or len(self.busTable.selectedItems()) < 1:
            return

        id = int(self.busTable.selectedItems()[0].text())
        query = QSqlQuery()
        query.prepare("delete from Bus where id = :id")
        query.bindValue(":id",id)
        if query.exec_() == False:
            criticalMessage("Could not delete this bus from table")
        else:
            self.busTable.removeRow(selected.row())
            self.busTable.setCurrentIndex(QModelIndex())
            self.initBusTable()
            self.initReservationForm()

    def initReservationForm(self):
        self.busCombo.clear()
        self.busCombo.addItems([str(busId) for busId in self.buses])

        self.originCombo.clear()
        self.originCombo.addItems(self.cities.keys())

        self.destCombo.clear()
        self.destCombo.addItems(self.cities.keys())

        self.dptDatePicker.setDateTime(QDateTime().currentDateTime())
        self.arvDatePicker.setDateTime(QDateTime().currentDateTime())

    def insertPlan(self):
        busId = int(self.busCombo.currentText())
        originId = self.cities[self.originCombo.currentText()]
        destId = self.cities[self.destCombo.currentText()]
        dptDateTime = self.dptDatePicker.dateTime()
        arvDateTime = self.arvDatePicker.dateTime()
        dptDateTimeText = dptDateTime.toString("yyyy-MM-dd hh:mm")
        arvDateTimeText = arvDateTime.toString("yyyy-MM-dd hh:mm")
        now = QDateTime().currentDateTime()

        if originId == destId:
            criticalMessage("Origin and destination cannot be the same!!!")
            return
        
        #first step of date checking
        if dptDateTime > now and arvDateTime > now and arvDateTime > dptDateTime:
            if self.dateConflict(busId,dptDateTimeText,arvDateTimeText):
                criticalMessage("This bus has another plan that conflicts with specified datetime")
            else:
                query = QSqlQuery()
                query.prepare("insert into Plan(busId, originId, destId, dptDate, arvDate) values(:busId, :originId, :destId, :dptDate, :arvDate)")
                query.bindValue(":busId",busId)
                query.bindValue(":originId",originId)
                query.bindValue(":destId",destId)
                query.bindValue(":dptDate",dptDateTimeText)
                query.bindValue(":arvDate",arvDateTimeText)

                if query.exec_() == False:
                    criticalMessage("Could not insert into Plan table")
                else:
                    self.initPlanTable()
        else:
            criticalMessage("Illogical datetime specified")

    def dateConflict(self,busId,dptDateTimeText,arvDateTimeText):
        query = QSqlQuery()
        query.prepare("select count(*) from Plan where busId = :busId and not (:dptinp > arvDate or :dptarv < dptDate)")
        query.bindValue(":busId" , busId)
        query.bindValue(":dptinp",dptDateTimeText)
        query.bindValue(":dptarv",arvDateTimeText)
        if query.exec_() == False:
            print("Execution failed")
            return False
        query.next()
        return query.value(0) != 0

    def initPlanTable(self):
        index = 0
        query = QSqlQuery()
        query.exec_("""select *,
(select (capacity - (select count(*) as ReservedSeats from Reservation where planId = tbt.planId)) as Remained from Bus as b where b.id = tbt.busId) as RemainedSeats
from (select id as planId,busId,(select c.name from City as c where c.id == p.originId) as Origin , (select c.name from City as c where c.id == p.destId) as Destination , dptDate , arvDate from Plan as p)
as tbt""")

        self.planTable.clear()
        self.planTable.setHorizontalHeaderLabels(['Plan Id','Bus Id' , 'Origin' , 'Destination' , 'Departure' , 'Arrival' , 'Remained Seats'])
        
        while query.next():
            self.planTable.setRowCount(index + 1)
            for i in range(7):
                self.planTable.setItem(index, i, QTableWidgetItem(str(query.value(i))))

            index += 1

    def deletePlan(self):
        selected = self.planTable.currentIndex()
        if not selected.isValid() or len(self.planTable.selectedItems()) < 1:
            return

        id = int(self.planTable.selectedItems()[0].text())
        query = QSqlQuery()
        query.prepare("delete from Plan where id = :id")
        query.bindValue(":id",id)
        if query.exec_() == False:
            criticalMessage("Could not delete this plan from table")
        else:
            self.planTable.removeRow(selected.row())
            self.planTable.setCurrentIndex(QModelIndex())
            self.initPlanTable()

    def initReservationTable(self):
        index = 0
        query = QSqlQuery()
        query.exec_("select r.id as ReservationId , u.id as UserId, r.planId as PlanId , u.name as TicketOwnerName , r.seatNumber as SeatNumber  from Reservation as r inner join User as u on u.id = r.userId")
        self.reserveTable.clear()
        self.reserveTable.setHorizontalHeaderLabels(['Reservation Id' , 'User Id' , 'Plan Id' , 'Owner Name' , 'Reserved Seat No'])

        while query.next():
            self.reserveTable.setRowCount(index + 1)

            for i in range(5):
                self.reserveTable.setItem(index, i, QTableWidgetItem(str(query.value(i))))

            index += 1

    def deleteReservation(self):
        selected = self.reserveTable.currentIndex()
        if not selected.isValid() or len(self.reserveTable.selectedItems()) < 1:
            return

        id = int(self.reserveTable.selectedItems()[0].text())
        query = QSqlQuery()
        query.prepare("delete from Reservation where id = :id")
        query.bindValue(":id",id)
        if query.exec_() == False:
            criticalMessage("Could not delete this reservation from table")
        else:
            self.reserveTable.removeRow(selected.row())
            self.planTable.setCurrentIndex(QModelIndex())
            self.initReservationTable()
