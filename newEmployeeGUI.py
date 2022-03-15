from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import adminMenu
import admin_functions
from connection import connection



class newEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.firstNameText = QLineEdit(None)
        self.lastNameText = QLineEdit(None)
        self.positionText = QLineEdit(None)
        self.salaryText = QLineEdit(None)
        self.usernameText = QLineEdit(None)
        self.passwordText = QLineEdit(None)

        self.firstNameText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.lastNameText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.positionText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.salaryText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.usernameText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.passwordText.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.menu()

    def menu(self):
        stylesheet = "QWidget{ " \
                     "" \
                     "}" \
                     "QPushButton{" \
                     "border-radius: 10px;" \
                     "width: 180px;" \
                     "height: 50px;" \
                     "background-color: rgb(186, 144, 71);" \
                     "font-size: 15px;" \
                     "}" \
                     "QLineEdit {" \
                     "max-width: 370px;" \
                     "min-height: 35px;" \
                     "border-radius: 5px;" \
                     "background-color: rgba(51, 50, 50, 0.7);" \
                     "}" \

        self.setFixedSize(500, 600)
        self.setWindowTitle("New Employee")

        oImage = QImage('background_logo.jpg')
        sImage = oImage.scaled(QSize(500, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.firstNameText.setPlaceholderText("Employee First Name")
        self.lastNameText.setPlaceholderText("Employee Last Name")
        self.positionText.setPlaceholderText("Employee Position")
        self.salaryText.setPlaceholderText("Employee Salary")
        self.usernameText.setPlaceholderText("Employee Username")
        self.passwordText.setPlaceholderText("Employee Password")

        insert = QPushButton("Insert", clicked = self.onClickAddEmployee)

        ret = QPushButton("Return")
        ret.clicked.connect(self.onClickReturn)
        ret.clicked.connect(self.close)

        layout = QGridLayout()
        layout.setContentsMargins(65, 0, 0, 0)
        layout.addWidget(self.firstNameText, 1, 1, 1, 5)
        layout.addWidget(self.lastNameText, 2, 1, 1, 5)
        layout.addWidget(self.positionText, 3, 1, 1, 5)
        layout.addWidget(self.salaryText, 4, 1, 1, 5)
        layout.addWidget(self.usernameText, 5, 1, 1, 5)
        layout.addWidget(self.passwordText, 6, 1, 1, 5)
        layout.addWidget(insert, 7, 2)
        layout.addWidget(ret, 7, 1)

        self.setStyleSheet(stylesheet)
        self.setLayout(layout)

    def onClickReturn(self):
        self.second_window = adminMenu.adminMain()
        self.second_window.show()

    def onClickAddEmployee(self):
        if self.firstNameText.text() or self.lastNameText.text() or self.positionText.text() or self.salaryText.text() or self.usernameText.text() or self.passwordText.text():
            admin_functions.add_employee(self.firstNameText.text(), self.lastNameText.text(), self.positionText.text(),
                                         int(self.salaryText.text()), self.usernameText.text(), self.passwordText.text())

            connection[0].execute("SELECT employee_id FROM employee "
                                  "ORDER BY employee_id DESC LIMIT 1 ")

            res = connection[0].fetchone()

            i = int(str(res).strip("(),"))
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f"Employee added successfully \n With the ID: {i}")
            msgBox.setWindowTitle("Insert Successfully")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            self.firstNameText.setText("")
            self.lastNameText.setText("")
            self.positionText.setText("")
            self.salaryText.setText("")
            self.usernameText.setText("")
            self.passwordText.setText("")
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Please fill all fields")
            msgBox.setWindowTitle("ValueError")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()


