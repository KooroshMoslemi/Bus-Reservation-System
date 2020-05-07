# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(362, 272)
        self.registerBtn = QtWidgets.QPushButton(Register)
        self.registerBtn.setGeometry(QtCore.QRect(110, 190, 121, 61))
        self.registerBtn.setObjectName("registerBtn")
        self.splitter_5 = QtWidgets.QSplitter(Register)
        self.splitter_5.setGeometry(QtCore.QRect(20, 10, 311, 171))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter = QtWidgets.QSplitter(self.splitter_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.nameLabel = QtWidgets.QLabel(self.splitter)
        self.nameLabel.setObjectName("nameLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.usernameLabel = QtWidgets.QLabel(self.splitter_2)
        self.usernameLabel.setObjectName("usernameLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.passwordLabel = QtWidgets.QLabel(self.splitter_3)
        self.passwordLabel.setObjectName("passwordLabel")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.rePasswordLabel = QtWidgets.QLabel(self.splitter_4)
        self.rePasswordLabel.setObjectName("rePasswordLabel")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.splitter_4)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.registerBtn.setText(_translate("Register", "Register"))
        self.nameLabel.setText(_translate("Register", "Name:"))
        self.usernameLabel.setText(_translate("Register", "Username:"))
        self.passwordLabel.setText(_translate("Register", "Password:"))
        self.rePasswordLabel.setText(_translate("Register", "Repeat Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
