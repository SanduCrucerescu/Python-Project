import newCustomer
from connection import connection
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import check_user
import customerUI

import sys


class roomTypes(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Room ID', 'Room Type'])
        self.roomTypes()

    def roomTypes(self):
        stylesheet = "QTableWidget {" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \

        self.setFixedSize(258, 350)
        self.setWindowTitle("Room Types")

        oImage = QImage('room_types.png')
        sImage = oImage.scaled(QSize(258, 350))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        connection[0].execute("select * from rooms")
        res = connection[0].fetchall()

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        layout = QHBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.setStyleSheet(stylesheet)

        # results = connection[0]
        # output = {}
        # for x in connection[0]:
        #     output[x[0]] = x[1]
        # for k, v in output.items():
        #     print(k, ":\t", v)


def numOfDays(date1, date2):
    return (date2 - date1).days


class reservationMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.text = QLabel("Welcome")
        self.text.setAccessibleName("text")
        self.checkInText = QLabel("Check In")
        self.checkOutText = QLabel("Check Out")
        self.numbOfRoomsText = QLabel("Number Of Rooms")
        self.checkIn = QDateEdit()
        self.checkIn.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.checkOut = QDateEdit()
        self.checkOut.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.numbOfRooms = QComboBox()
        self.adults = QLineEdit()
        self.adults.setPlaceholderText("Adults")
        self.adults.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.children = QLineEdit()
        self.children.setPlaceholderText("Children")
        self.children.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.roomType = QLineEdit()
        self.roomType.setPlaceholderText("Input room ID")
        self.roomType.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.makeReservation = QPushButton("Make Reservation", clicked=self.submit)
        self.roomType.setAccessibleName("roomType")
        self.viewRoomTypes = QPushButton("View Room Types", clicked=self.onClickViewRoomTypes)
        self.viewRoomTypes.setAccessibleName("btn")
        self.exit = QPushButton("Exit", clicked=self.onClickMainMenu)
        self.resMenu()

    def resMenu(self):
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
                     "QPushButton[accessibleName = 'btn'] {" \
                     "border-radius: 10px;" \
                     "height: 30px;" \
                     "margin-left: 160px;" \
                     "background-color: rgb(186, 144, 71);" \
                     "font-size: 15px;" \
                     "}" \
                     "QLineEdit {" \
                     "max-width: 302px;" \
                     "min-height: 35px;" \
                     "border-radius: 5px;" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \
                     "QLineEdit[accessibleName = 'roomType'] {" \
                     "max-width: 150px;" \
                     "min-height: 35px;" \
                     "border-radius: 5px;" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \
                     "QTableWidget {" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \
                     "QLabel{" \
                     "font-size: 20px;" \
                     "color: rgb(186, 144, 71);" \
                     "}" \
                     "QLabel[accessibleName = 'text']{" \
                     "font-size: 50px;" \
                     "color: rgb(186, 144, 71);" \
                     "}" \
                     "QDateEdit{" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "border-radius: 10px;" \
                     "height: 30px;" \
                     "}" \
                     "QDateEdit::up-arraow{" \
                     "background-color : red;" \
                     "}" \

        self.setFixedSize(700, 600)
        self.setWindowTitle("New Reservation")

        oImage = QImage('background_logo.jpg')
        sImage = oImage.scaled(QSize(700, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.numbOfRooms.addItems(["1", "2", "3", "4"])
        self.roomType.setAccessibleName("roomType")
        self.text.setAlignment(Qt.AlignCenter)

        layout = QGridLayout()
        layout.addWidget(self.text, 0, 0, 1, 3)
        layout.addWidget(self.adults, 1, 0)
        layout.addWidget(self.children, 1, 1)
        layout.addWidget(self.numbOfRoomsText, 2, 0)
        layout.addWidget(self.numbOfRooms, 3, 0)
        layout.addWidget(self.roomType, 3, 1)
        layout.addWidget(self.viewRoomTypes, 3, 1)
        layout.addWidget(self.checkInText, 4, 0)
        layout.addWidget(self.checkOutText, 4, 1)
        layout.addWidget(self.checkIn, 5, 0)
        layout.addWidget(self.checkOut, 5, 1)
        layout.addWidget(self.makeReservation, 6, 0)
        layout.addWidget(self.exit, 6, 1)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.setStyleSheet(stylesheet)

    def submit(self):
        if self.checkIn.text() or self.checkOut.text() or self.adults.text() or self.children.text() or self.numbOfRooms.currentText() or self.roomType.text():
            checkIn = self.checkIn.text().split("-")
            checkInFinal = datetime.date(int(checkIn[0]), int(checkIn[1]), int(checkIn[2]))
            checkOut = self.checkOut.text().split("-")
            checkOutFinal = datetime.date(int(checkOut[0]), int(checkOut[1]), int(checkOut[2]))

            try:
                roomType = list(self.roomType.text().split(","))  # int(roomtypes.split(",")))
                new_room = [int(g) for g in roomType]
            except ValueError:
                pass

            now = datetime.datetime.now()
            formattedDate = now.strftime('%Y-%m-%d')

            customer = 0

            # check which customer data to use
            if check_user.checkUser.status:
                customer = check_user.checkUser.id
            elif not check_user.checkUser.status:
                customer = newCustomer.newCustomer.id

            # inserting data into the customer table
            connection[0].execute(
                f"INSERT INTO reservation(customers_id, check_in,check_out,number_of_rooms,adults,children,date_reservation) "
                f"VALUES({customer}, '{checkInFinal}', '{checkOutFinal}',"
                f"{int(self.numbOfRooms.currentText())}, {int(self.adults.text())}, {int(self.children.text())}, '{formattedDate}' );")
            connection[1].commit()

            # inserting data into the bookings table
            for i in new_room:
                connection[0].execute(f"select room_rate from rooms where rooms_id = {i}")
                price = numOfDays(checkInFinal, checkOutFinal) * int(str(connection[0].fetchone()).strip("(),"))
                connection[0].execute("SET @reservation_id = (SELECT reservation_id FROM reservation "
                                      "ORDER BY reservation_id DESC LIMIT 1)")
                connection[0].execute(
                    f"INSERT INTO Bookings(Reservation_ID, Room_ID, price) VALUES(@reservation_id, {i}, {price});")
                connection[1].commit()

            #getting the latest reservation
            connection[0].execute("SELECT reservation_id FROM reservation "
                                  "ORDER BY reservation_id DESC LIMIT 1 ")

            res = connection[0].fetchone()
            i = int(str(res).strip("(),"))


            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f"Reservation complete.\n Reservation number: {i}")
            msgBox.setWindowTitle("Reservation Complete")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Error)
            msgBox.setText(f"Please complete all of the fields")
            msgBox.setWindowTitle("Login  Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

    def onClickViewRoomTypes(self):
        self.sub_window = roomTypes()
        self.sub_window.show()

    def onClickMainMenu(self):
        self.sub_window = customerUI.customerUI()
        self.sub_window.show()
        self.close()

