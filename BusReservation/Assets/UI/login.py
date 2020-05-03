# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(294, 168)
        self.splitter = QtWidgets.QSplitter(Login)
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

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.usernameLabel.setText(_translate("Login", "Username:"))
        self.passwordLabel.setText(_translate("Login", "Password:"))
        self.loginButton.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
