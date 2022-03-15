from PyQt5 import QtCore
from PyQt5.QtGui import *

import admin_functions
import main
import adminMenu
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


# hotel management menu.
# admins can alter the employee manifest (add/delete staff employees).
# admins can also delete a reservation using the reservation_id.
# staff can not access and will be looped back until a valid admin log in.

# staff credentials: lsleep0 |  7UwpuSI5ERv
# admin credentials: lpeckittf | wKAo4eumS

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.username_text = QLineEdit()
        self.username_text.setPlaceholderText("Username")
        self.password_text = QLineEdit()
        self.password_text.setPlaceholderText("Password")
        self.username_text.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.password_text.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.password_text.setEchoMode(QLineEdit.Password)
        self.login()

    def login(self):
        # LoginWindow.setWindowTitle("Login")
        # LoginWindow.setFixedSize(QSize(360, 300))
        # self.widget = QWidget(LoginWindow)
        # self.setGeometry(QtCore.QRect(20, 31, 276, 216))
        # self.setStyleSheet("background-color: white")


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


        self.text = QLabel("Log In")
        self.text.setStyleSheet(''' font-size: 20px; color: rgb(186, 144, 71);  ''')



        login = QPushButton("Login", clicked = self.on_click)
        exitLogin = QPushButton("Exit", clicked = self.onClickToMainMenu)

        exitLogin.clicked.connect(self.close)

        layout = QGridLayout()
        layout.setContentsMargins(50, 150, 0, 0)
        layout.addWidget(self.text, 0, 1, 1, 3, Qt.AlignCenter)
        layout.addWidget(self.username_text, 1, 1, 1, 5)
        layout.addWidget(self.password_text, 2, 1, 1, 5)
        layout.addWidget(login, 3, 1)
        layout.addWidget(exitLogin, 3, 2, Qt.AlignCenter)

        layout.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(stylesheet)
        self.setLayout(layout)
        self.show()

    def on_click(self):
        if self.username_text.text() or self.password_text.text():
            if admin_functions.logging_main_menu(self.username_text.text(), self.password_text.text()) == 1:
                self.ui = adminMenu.adminMain()
                self.ui.show()
                self.close()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Username or password incorrect")
                msgBox.setWindowTitle("Login  Error")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Please complete every field")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

    def onClickToMainMenu(self):
        self.ui = main.Main()
        self.ui.show()

