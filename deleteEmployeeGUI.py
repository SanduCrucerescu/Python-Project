from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import adminMenu
import admin_functions


class deleteEmployee(QWidget):
    def __init__(self):
        super().__init__()
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
                     "width: 138px;" \
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

        self.setFixedSize(500, 500)
        self.setWindowTitle("Delete Employee")

        oImage = QImage('background_logo.png')
        sImage = oImage.scaled(QSize(500, 500))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.firstNameText.setPlaceholderText("Employee First Name")
        self.lastNameText.setPlaceholderText("Employee Last Name")

        delete = QPushButton("Delete", clicked = self.onClickDelete)

        ret = QPushButton("Return")
        ret.clicked.connect(self.onClickReturn)
        ret.clicked.connect(self.close)

        layout = QGridLayout()
        layout.setContentsMargins(100, 180, 0, 0)
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(30)
        layout.addWidget(self.firstNameText, 1, 1, 1, 3)
        layout.addWidget(self.lastNameText, 2, 1, 1, 3)
        layout.addWidget(delete, 3, 1)
        layout.addWidget(ret, 3, 2)

        self.setStyleSheet(stylesheet)
        self.setLayout(layout)

    def onClickReturn(self):
        self.second_window = adminMenu.adminMain()
        self.second_window.show()

    def onClickDelete(self):
        if not admin_functions.search_employee(self.firstNameText.text(), self.lastNameText.text()):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("No employee with this first name and last name exists")
            msgBox.setWindowTitle("ValueError")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            if self.firstNameText.text() or self.lastNameText.text():
                admin_functions.delete_employee(self.firstNameText.text(), self.lastNameText.text())
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(f"You have deleted {self.firstNameText.text()} {self.lastNameText.text()} successfully")
                msgBox.setWindowTitle("Delete Successfully")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                self.firstNameText.setText("")
                self.lastNameText.setText("")
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("All fields need to be inserted")
                msgBox.setWindowTitle("ValueError")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
