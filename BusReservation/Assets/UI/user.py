# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User(object):
    def setupUi(self, User):
        User.setObjectName("User")
        User.resize(489, 397)
        self.planReserveGB = QtWidgets.QGroupBox(User)
        self.planReserveGB.setGeometry(QtCore.QRect(10, 10, 471, 381))
        self.planReserveGB.setObjectName("planReserveGB")
        self.splitter_2 = QtWidgets.QSplitter(self.planReserveGB)
        self.splitter_2.setGeometry(QtCore.QRect(10, 20, 451, 351))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.planReserveTable = QtWidgets.QTableWidget(self.splitter_2)
        self.planReserveTable.setObjectName("planReserveTable")
        self.planReserveTable.setColumnCount(0)
        self.planReserveTable.setRowCount(0)
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

        self.retranslateUi(User)
        QtCore.QMetaObject.connectSlotsByName(User)

    def retranslateUi(self, User):
        _translate = QtCore.QCoreApplication.translate
        User.setWindowTitle(_translate("User", "User Panel"))
        self.planReserveGB.setTitle(_translate("User", "Plan Reservation"))
        self.seatLabel.setText(_translate("User", "Empty Seats:"))
        self.reserveBtn.setText(_translate("User", "Reserve"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User = QtWidgets.QWidget()
    ui = Ui_User()
    ui.setupUi(User)
    User.show()
    sys.exit(app.exec_())
