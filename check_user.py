import sys

from connection import connection
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import reservation
import newCustomer


class checkUser(QWidget):
    id = 0
    status = True

    def checkUser(self, first_name, last_name):
        connection[0].execute(
            f"select exists(SELECT * FROM customer WHERE customer_firstname = '{first_name}' and customer_lastname = '{last_name}');")
        results = int(str(connection[0].fetchone()).strip("(),"))

        if results == 1:
            connection[0].execute(f"SELECT customer_id FROM customer WHERE "
                                  f"customer_firstname = '{first_name}' and customer_lastname = '{last_name}';;")
            results = int(str(connection[0].fetchone()).strip("(),"))
            return results, True
        elif results == 0:
            return 0, False

    def __init__(self):
        super().__init__()
        self.text = QLabel("Enter Details")
        self.firstNameText = QLineEdit(None)
        self.lastNameText = QLineEdit(None)
        self.firstNameText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.lastNameText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.menu()

    def menu(self):
        stylesheet = "QWidget{ " \
                     "" \
                     "}" \
                     "QPushButton{" \
                     "border-radius: 10px;" \
                     "width: 150px;" \
                     "height: 30px;" \
                     "background-color: rgb(186, 144, 71);" \
                     "}" \
                     "QLineEdit {" \
                     "max-width: 310px;" \
                     "min-height: 35px;" \
                     "border-radius: 5px;" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \

        self.setFixedSize(500, 600)
        oImage = QImage('login_screen-100.jpg')
        sImage = oImage.scaled(QSize(500, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.id = 0

        self.firstNameText.setPlaceholderText("Customer First Name")
        self.lastNameText.setPlaceholderText("Customer Last Name")
        self.text.setStyleSheet(''' font-size: 20px; color: rgb(186, 144, 71);  ''')
        self.text.setAlignment(Qt.AlignCenter)

        submit = QPushButton("Submit", clicked=self.onClickSubmit)
        exit = QPushButton("Close", clicked=QCoreApplication.quit)

        layout = QGridLayout()
        layout.setContentsMargins(50, 150, 0, 0)
        layout.addWidget(self.text, 0, 1, 1, 3)
        layout.addWidget(self.firstNameText, 1, 1, 1, 5)
        layout.addWidget(self.lastNameText, 2, 1, 1, 5)
        layout.addWidget(submit, 3, 1)
        layout.addWidget(exit, 3, 2, Qt.AlignCenter)
        layout.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(stylesheet)
        self.setLayout(layout)

    def onClickSubmit(self):
        if self.firstNameText.text() or self.lastNameText.text():
            res = self.checkUser(self.firstNameText.text(), self.lastNameText.text())
            if res[1]:
                result = QMessageBox.question(self, "Welcome", "Welcome Back", QMessageBox.Close)
                if result == QMessageBox.Close:
                    self.sub_window = reservation.reservationMenu()
                    self.sub_window.show()
                    self.close()
                    checkUser.id = res[0]
            elif not res[1]:
                result = QMessageBox.question(self, "Error", "Welcome, since you are a new customer we need some "
                                                             "additional information", QMessageBox.Close)
                if result == QMessageBox.Close:
                    self.sub_window = newCustomer.newCustomer()
                    self.sub_window.firstName.setText(self.firstNameText.text())
                    self.sub_window.lastName.setText(self.lastNameText.text())
                    self.sub_window.show()
                    self.close()
                    checkUser.id = res[0]
                    checkUser.status = res[1]
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Please complete every field")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()


    def getCustomerId(self):
        return checkUser.id
