from PyQt5 import QtCore

from connection import connection
#import reservationMenu
import admin_functions
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import loginGUI
import customerUI


def run():
    connection[0].execute("select hotel_name from hotel")
    print("Welcome to", str(connection[0].fetchone()).strip("(),"))
    userChoise = int(input("Are you a customer(1) or and employee(2) or exit(0):"))

    if userChoise == 2:
        admin_functions.logging_main_menu()
    elif userChoise == 1:
        customerOption = int(input("Do you want to see a reservation(1) or make a reservation(2):"))
        if customerOption == 1:
            first_name = input("Please input your first name: ")
            last_name = input("Please input your last name: ")
            connection[0].execute("SELECT customer_firstname, customer_lastname, check_in, check_out, "
                                  "number_of_rooms, adults, children, date_reservation,Room_type, price FROM rooms r "
                                  "inner join bookings b on b.room_id = r.rooms_id "
                                  "inner join Reservation re on re.reservation_id = b.reservation_id "
                                  "inner join customer cu on cu.customer_id = re.customers_id "
                                  f"where cu.customer_firstname = '{first_name}' and cu.customer_lastname = '{last_name}'")
            print("First Name |", "Last Name |", "  Check In  |", "  Check Out  |", "Number of Rooms |", "Adults |",
                  "Children |", "Date of Reservation |", "   Room Type   |", "Price")
            for x in connection[0].fetchall():
                print(
                    f"{x[0]:<13} {x[1]:<11} {x[2]}    {x[3]} {x[4]:>12} {x[5]:>12} {x[6]:>9}          {x[7]} {x[8]:>19} {x[9]:>9}")
            os.system('read -n1 -r -p "Press any key to continue..." key')
            run()
        elif customerOption == 2:
            reservationMenu.reservationMenu()
    elif userChoise == 0:
        exit(0)


# run()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        stylesheet = "QWidget{ " \
                     "" \
                     "}" \
                     "QPushButton{" \
                     "border-radius: 10px;" \
                     "width: 150px;" \
                     "height: 50px;" \
                     "background-color: rgb(186, 144, 71);" \
                     "}" \
                     "QLabel{" \
                     "font-size: 30px" \
                     "font-family: Myriad Pro;" \
                     "background-color: black;" \
                     "color: rgb(186, 144, 71);" \
                     "}" \

        self.setStyleSheet(stylesheet)
        self.setWindowTitle("Front Page")
        self.setFixedSize(QSize(500, 600))
        oImage = QImage('login_screen-100.jpg')
        sImage = oImage.scaled(QSize(500, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.text = QLabel("Select Your Option")
        self.text.setStyleSheet(''' font-size: 20px; color: rgb(186, 144, 71);  ''')

        customer = QPushButton("Employee")
        customer.clicked.connect(self.onClickLogin)
        customer.clicked.connect(self.close)

        employee = QPushButton("Customer")
        employee.clicked.connect(self.onClickCustomer)
        employee.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 200, 0, 0)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text)
        layout.addWidget(customer)
        layout.addWidget(employee)

        connection[0].execute("CREATE OR REPLACE VIEW Reservations "
                              "AS "
                              "SELECT re.reservation_id, customer_firstname, customer_lastname, check_in, check_out, "
                              "adults, children, date_reservation, number_of_rooms, sum(price) as pr FROM bookings b "
                              "inner join Reservation re on re.reservation_id = b.reservation_id "
                              "inner join customer cu on cu.customer_id = re.customers_id "
                              "group by re.reservation_id,customer_firstname, customer_lastname, "
                              "check_in, check_out, adults, children, date_reservation, number_of_rooms;")


        self.setLayout(layout)

    def onClickLogin(self):
        self.sub_window = loginGUI.Login()
        self.sub_window.show()

    def onClickCustomer(self):
        self.sub_window = customerUI.customerUI()
        self.sub_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
