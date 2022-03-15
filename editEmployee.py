from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import adminMenu
import admin_functions
from connection import connection



class editEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.id = QLineEdit()
        self.firstNameText = QLineEdit(None)
        self.lastNameText = QLineEdit(None)
        self.positionText = QLineEdit(None)
        self.salaryText = QLineEdit(None)
        self.usernameText = QLineEdit(None)
        self.passwordText = QLineEdit(None)

        self.id.setAttribute(Qt.WA_MacShowFocusRect, 0)
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
                     "height: 35px;" \
                     "background-color: rgb(186, 144, 71);" \
                     "font-size: 15px;" \
                     "}" \
                     "QLineEdit {" \
                     "max-width: 450px;" \
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

        self.id.setPlaceholderText("Employee ID")
        self.firstNameText.setPlaceholderText("Employee First Name")
        self.lastNameText.setPlaceholderText("Employee Last Name")
        self.positionText.setPlaceholderText("Employee Position")
        self.salaryText.setPlaceholderText("Employee Salary")
        self.usernameText.setPlaceholderText("Employee Username")
        self.passwordText.setPlaceholderText("Employee Password")

        insert = QPushButton("Insert", clicked = self.onClickAddEmployee)
        search = QPushButton("Search Employee", clicked = self.onClickSearchEmployee)
        ret = QPushButton("Return")
        ret.clicked.connect(self.onClickReturn)
        ret.clicked.connect(self.close)

        layout = QGridLayout()
        layout.addWidget(self.id, 0, 0)
        layout.addWidget(search, 0, 1)
        layout.addWidget(self.firstNameText, 1, 0, 1, 3)
        layout.addWidget(self.lastNameText, 2, 0, 1, 3)
        layout.addWidget(self.positionText, 3, 0, 1, 3)
        layout.addWidget(self.salaryText, 4, 0, 1, 3)
        layout.addWidget(self.usernameText, 5, 0, 1, 3)
        layout.addWidget(self.passwordText, 6, 0, 1, 3)
        layout.addWidget(insert, 7, 0)
        layout.addWidget(ret, 7, 1)

        self.setStyleSheet(stylesheet)
        self.setLayout(layout)

    def onClickReturn(self):
        self.second_window = adminMenu.adminMain()
        self.second_window.show()

    def onClickSearchEmployee(self):
        if admin_functions.search_employeeID(self.id.text()) == False:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("No employee Exists with this ID")
            msgBox.setWindowTitle("No user Selected")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            if self.id.text():
                connection[0].execute("SELECT Employee_firstname, Employee_lastname, Employee_position, "
                                      "Employee_salary, employee_username, employee_password "
                                      "FROM employee INNER JOIN employee_login "
                                      "ON employee_login.employee_id = employee.Employee_id "
                                      f"WHERE employee.Employee_id = {int(self.id.text())} ;")

                res = connection[0].fetchone()
                self.firstNameText.setText(res[0])
                self.lastNameText.setText(res[1])
                self.positionText.setText(res[2])
                self.salaryText.setText(str(res[3]))
                self.usernameText.setText(res[4])
                self.passwordText.setText(res[5])
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Please insert an employee ID")
                msgBox.setWindowTitle("No user Selected")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()


    def onClickAddEmployee(self):
        if self.id.text() or self.firstNameText.text() or self.lastNameText.text() or self.positionText.text() or self.salaryText.text() or self.usernameText.text() or self.passwordText.text():
            admin_functions.admin_edit_employee(int(self.id.text()), self.firstNameText.text(), self.lastNameText.text(),
                                                self.positionText.text(),
                                                int(self.salaryText.text()), self.usernameText.text(),
                                                self.passwordText.text())
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Employee modiffied successfully")
            msgBox.setWindowTitle("modiffied Successfully")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            self.id.setText("")
            self.firstNameText.setText("")
            self.lastNameText.setText("")
            self.positionText.setText("")
            self.salaryText.setText("")
            self.usernameText.setText("")
            self.passwordText.setText("")
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("All Fields need to be filled")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
