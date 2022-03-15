from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import adminMenu
import admin_functions
import check_user
from check_user import checkUser
import viewReservation



class customerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.text = QLabel("Select an option")
        self.menu()

    def menu(self):
        stylesheet = "QWidget{ " \
                     "" \
                     "}" \
                     "QPushButton{" \
                     "border-radius: 10px;" \
                     "width: 200px;" \
                     "height: 50px;" \
                     "background-color: rgba(51, 50, 50, 0.88);" \
                     "}" \
                     "QVBoxLayout{" \
                     "text-align:center;" \
                     "}" \


        self.setFixedSize(500, 600)
        oImage = QImage('login_screen-100.jpg')
        sImage = oImage.scaled(QSize(500, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.setWindowTitle("Customer Menu")

        makeReservation = QPushButton("Make a Reservation")
        makeReservation.clicked.connect(self.onClickMakeReservation)
        makeReservation.clicked.connect(self.close)

        checkReservation = QPushButton("Check Reservation")
        checkReservation.clicked.connect(self.onClickCheckReservation)
        checkReservation.clicked.connect(self.close)
        self.text.setStyleSheet(''' font-size: 20px; color: rgb(186, 144, 71); ''')
        self.text.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 200, 0, 0)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text)
        layout.addWidget(makeReservation)
        layout.addWidget(checkReservation)

        self.setStyleSheet(stylesheet)
        self.setLayout(layout)

    def onClickReturn(self):
        self.second_window = adminMenu.adminMain()
        self.second_window.show()

    def onClickMakeReservation(self):
        self.sub_window = check_user.checkUser()
        self.sub_window.show()

    def onClickCheckReservation(self):
        self.sub_window = viewReservation.viewReservation()
        self.sub_window.show()

