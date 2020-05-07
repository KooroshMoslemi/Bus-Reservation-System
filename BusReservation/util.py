from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlQuery,QSqlDatabase

def dbConnect():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("Bus.db")
    if not db.open():
        QMessageBox.critical(None, "Cannot open database","Unable to establish a database connection.", QMessageBox.Cancel)
        return
    enableForeignKey()

def enableForeignKey():
    query = QSqlQuery()
    query.exec_("PRAGMA foreign_keys=ON")

def criticalMessage(message):
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(message)
    msg.setIcon(QMessageBox.Critical)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Ok)
    return msg.exec_()