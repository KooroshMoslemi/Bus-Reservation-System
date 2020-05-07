import sys
from PyQt5 import QtCore, QtWidgets
from UserPanel import UserWindow
from AdminPanel import AdminWindow
from Register import RegisterWindow
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
from util import *


class Login(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login')
        self.setObjectName('Login')
        self.resize(294, 203)
        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.setGeometry(QtCore.QRect(20, 10, 261, 141))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.usernameLabel = QtWidgets.QLabel(self.widget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout.addWidget(self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.horizontalLayout.addWidget(self.usernameLineEdit)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwordLabel = QtWidgets.QLabel(self.widget1)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.widget1)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_2.addWidget(self.passwordLineEdit)
        self.loginButton = QtWidgets.QPushButton(self.splitter)
        self.loginButton.setObjectName("loginButton")
        self.registerLink = QtWidgets.QCommandLinkButton(self)
        self.registerLink.setGeometry(QtCore.QRect(90, 150, 101, 41))
        self.registerLink.setObjectName("registerLink")


        #Connecting to database
        dbConnect()

        self.loginButton.clicked.connect(lambda : self.auth(self.usernameLineEdit.text(),self.passwordLineEdit.text()))
        self.registerLink.clicked.connect(self.show_register)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Login"))
        self.usernameLabel.setText(_translate("Login", "Username:"))
        self.passwordLabel.setText(_translate("Login", "Password:"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.registerLink.setText(_translate("Login", "Register"))

    def auth(self,username,password):
        index = 0
        query = QSqlQuery()
        query.prepare("select * from User where username = :username and password = :password")
        query.bindValue(":username",username)
        query.bindValue(":password",password)
        query.exec_()
        

        if query.next():
            #print(True,query.value("name"),query.value("isAdmin"))
            self.show_admin() if query.value("isAdmin") == 1 else self.show_user(query.value("id"))
        else:
            QtWidgets.QMessageBox.critical(None, "Invalid Credentials",
                    "Username or password is not  correct", QtWidgets.QMessageBox.Ok)

    def show_admin(self):
        self.window = AdminWindow()
        self.close()
        self.window.show()

    def show_user(self,userId):
        self.window = UserWindow(userId)
        self.close()
        self.window.show()

    def show_register(self):
        self.window = RegisterWindow()
        self.window.show()



def main():
    app = QtWidgets.QApplication(sys.argv)

    #Normal Run
    login = Login()
    login.show()

    #Test Admin
    #dbConnect()
    #window = AdminWindow()
    #window.show()

    #Test User
    #dbConnect()
    #window = UserWindow(2)
    #window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
