from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import adminMenu
import admin_functions
from connection import connection


class deleteReservation(QWidget):
    def __init__(self):
        super().__init__()
        self.reservationIDText = QLineEdit()

        self.reservationIDText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.menu()

    def menu(self):
        stylesheet = "QWidget{ " \
                     "" \
                     "}" \
                     "QPushButton{" \
                     "border-radius: 10px;" \
                     "width: 138px;" \
                     "height: 30px;" \
                     "background-color: rgba(186, 144, 71, 0,7);" \
                     "font-size: 15px;" \
                     "}" \
                     "QLineEdit {" \
                     "max-width: 302px;" \
                     "min-height: 35px;" \
                     "border-radius: 5px;" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \
                     "QTableWidget {" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \

        self.setFixedSize(952, 500)
        self.setWindowTitle("Delete Reservation")

        oImage = QImage('rsvp_background.png')
        sImage = oImage.scaled(QSize(952, 500))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.reservationIDText.setPlaceholderText("Reservation ID")
        self.table = QTableWidget(self)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['First Name', 'Last Name', 'Check In', 'Check Out',
                                              'Adults', 'Children', 'Date of Reservation',
                                              'Number of Rooms', 'Price'])

        delete = QPushButton("Delete", clicked=self.onClickDeleteReservation)
        view = QPushButton("View Reservation", clicked=self.onClickShowReservation)

        ret = QPushButton("Return")
        ret.clicked.connect(self.onClickReturn)
        ret.clicked.connect(self.close)

        layout = QGridLayout()
        layout.addWidget(self.reservationIDText, 0, 5, 1, 3)
        layout.addWidget(self.table, 1, 1, 1, 10)
        layout.addWidget(delete, 2, 5)
        layout.addWidget(view, 2, 6)
        layout.addWidget(ret, 2, 7)

        self.setStyleSheet(stylesheet)
        self.setLayout(layout)

    def onClickReturn(self):
        self.second_window = adminMenu.adminMain()
        self.second_window.show()

    def onClickDeleteReservation(self):
        if self.reservationIDText.text():
            admin_functions.admin_edit_rsvp(self.reservationIDText.text())
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Reservation Deleted Successful")
            msgBox.setWindowTitle("Deleted Successfully")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            self.reservationIDText.setText("")
            self.table.clear()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Please insert a reservation ID")
            msgBox.setWindowTitle("No reservation selected")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

    def onClickShowReservation(self):
        if admin_functions.search_reservations(self.reservationIDText.text()):
            if self.reservationIDText.text():
                connection[0].execute("select customer_firstname, customer_lastname, check_in, check_out, "
                                      "adults, children, date_reservation, number_of_rooms, pr from Reservations "
                                      f"where reservation_id = '{self.reservationIDText.text()}'")

                res = connection[0].fetchall()

                self.table.setRowCount(0)
                for row_number, row_data in enumerate(res):
                    self.table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Please insert a reservation ID")
                msgBox.setWindowTitle("ValueError")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("No reservation exists with this ID")
            msgBox.setWindowTitle("ValueError")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
