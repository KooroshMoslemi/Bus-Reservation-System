import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QModelIndex,QDateTime
from util import *


class RegisterWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Register")
        self.resize(362, 272)
        self.registerButton = QtWidgets.QPushButton(self)
        self.registerButton.setGeometry(QtCore.QRect(110, 190, 121, 61))
        self.registerButton.setObjectName("registerButton")
        self.splitter_5 = QtWidgets.QSplitter(self)
        self.splitter_5.setGeometry(QtCore.QRect(20, 10, 311, 171))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter = QtWidgets.QSplitter(self.splitter_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.nameLabel = QtWidgets.QLabel(self.splitter)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(self.splitter)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.usernameLabel = QtWidgets.QLabel(self.splitter_2)
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.passwordLabel = QtWidgets.QLabel(self.splitter_3)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.splitter_3)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.rePasswordLabel = QtWidgets.QLabel(self.splitter_4)
        self.rePasswordLabel.setObjectName("rePasswordLabel")
        self.rePasswordLineEdit = QtWidgets.QLineEdit(self.splitter_4)
        self.rePasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rePasswordLineEdit.setObjectName("rePasswordLineEdit")


        #connect
        self.registerButton.clicked.connect(self.register)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Register", "Register"))
        self.registerButton.setText(_translate("Register", "Register"))
        self.nameLabel.setText(_translate("Register", "Name:"))
        self.usernameLabel.setText(_translate("Register", "Username:"))
        self.passwordLabel.setText(_translate("Register", "Password:"))
        self.rePasswordLabel.setText(_translate("Register", "Repeat Password:"))

    def register(self):
        name = self.nameLineEdit.text()
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        re_password = self.rePasswordLineEdit.text()

        if name == "" or username == "" or password == "" or re_password == "":
            criticalMessage("Empty field is not allowed!")
            return
        if password != re_password:
            criticalMessage("Password confirmation failed")
            return
        if self.uniqueUsername(username) == False:
            criticalMessage("Repetitive username is not allowed!")
            return

        query = QSqlQuery()
        query.prepare("insert into User(name,username,password,isAdmin) values(:name,:username,:password,0)")
        query.bindValue(":name" , name)
        query.bindValue(":username" , username)
        query.bindValue(":password" , password)
        if query.exec_() == False:
            criticalMessage("Registration Failed!")
        else:
            self.close()
        

    def uniqueUsername(self,username):
        index = 0
        query = QSqlQuery()
        query.prepare("select count(*) from User where username = :username")
        query.bindValue(":username",username)
        query.exec_()
        query.next()
        return query.value(0) == 0