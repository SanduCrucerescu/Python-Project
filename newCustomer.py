from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import reservation
from connection import connection
import sys

class newCustomer(QWidget):
    id = 0
    def __init__(self):
        super().__init__()
        self.text = QLabel("New Customer")
        self.firstName = QLineEdit()
        self.firstName.setPlaceholderText("First Name")
        self.firstName.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.lastName = QLineEdit()
        self.lastName.setPlaceholderText("Last Name")
        self.lastName.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.address = QLineEdit()
        self.address.setPlaceholderText("Address")
        self.address.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Phone Number")
        self.phone.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.submit = QPushButton("Continue", clicked = self.addNewCustomer)
        self.newCustomer()

    def newCustomer(self):
        stylesheet = "QWidget{ " \
                     "" \
                     "}" \
                     "QPushButton{" \
                     "border-radius: 10px;" \
                     "width: 60px;" \
                     "height: 30px;" \
                     "background-color: rgb(186, 144, 71);" \
                     "font-size: 15px;" \
                     "}" \
                     "QLineEdit {" \
                     "max-width: 302px;" \
                     "min-height: 35px;" \
                     "border-radius: 5px;" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \
                     "QLabel{" \
                     "font-size: 20px;" \
                     "color: rgb(186, 144, 71);" \
                     "}" \

        self.setFixedSize(500, 600)
        oImage = QImage('background_logo.jpg')
        sImage = oImage.scaled(QSize(500, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.text.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(30)
        layout.addWidget(self.text)
        layout.addWidget(self.firstName)
        layout.addWidget(self.lastName)
        layout.addWidget(self.address)
        layout.addWidget(self.phone)
        layout.addWidget(self.submit)

        self.setLayout(layout)
        self.setStyleSheet(stylesheet)

    def addNewCustomer(self):
        if self.address.text() or self.phone.text():
            connection[0].execute(f"INSERT INTO customer (customer_firstname, customer_lastname, "
                                  f"customer_address, customer_phone) VALUES('{self.firstName.text()}',"
                                  f"'{self.lastName.text()}', '{self.address.text()}', '{self.phone.text()}'); ")
            connection[1].commit()
            connection[0].execute("SET @customer_id = last_insert_id();")
            connection[0].execute("select @customer_id;")
            newCustomer.id = results = int(str(connection[0].fetchone()).strip("(),"))
            self.onClickContimue()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Every field needs to be filled")
            msgBox.setWindowTitle("ValueError")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

    def onClickContimue(self):
        result = QMessageBox.question(self, "Welcome", "You can now continue with the reservation", QMessageBox.Close)
        if result == QMessageBox.Close:
            self.sub_window = reservation.reservationMenu()
            self.sub_window.show()
            self.close()
