import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import loginGUI
import newEmployeeGUI
import deleteEmployeeGUI
import deleteReservation
import editEmployee


class adminMain(QWidget):
    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):
        stylesheet = "QWidget{ " \
                     "" \
                     "}" \
                     "QPushButton{" \
                     "border-radius: 10px;" \
                     "width: 150px;" \
                     "height: 50px;" \
                     "background-color: rgba(51, 50, 50, 0.88);" \
                     "font-size: 15px;" \
                     "" \
                     "}" \
                     "QLabel{" \
                     "font-size: 30px" \
                     "font-family: Myriad Pro;" \
                     "background-color: black;" \
                     "color: rgb(186, 144, 71);" \
                     "}" \

        self.setWindowTitle("Admin Menu")
        self.setFixedSize(QSize(500, 600))

        oImage = QImage('background_logo.jpg')
        sImage = oImage.scaled(QSize(500, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        newEmployee = QPushButton("Add a new employee")
        newEmployee.clicked.connect(self.onClickNewEmployee)
        newEmployee.clicked.connect(self.close)
        deleteEmployee = QPushButton("Delete an employee")
        deleteEmployee.clicked.connect(self.onClickDelete)
        deleteEmployee.clicked.connect(self.close)
        deleteReservation = QPushButton("Delete a reservation")
        deleteReservation.clicked.connect(self.onClickDeleteReservation)
        deleteReservation.clicked.connect(self.close)
        editEmployee = QPushButton("Edit an employee", clicked = self.onClickEdit)
        editEmployee.clicked.connect(self.close)
        logOut = QPushButton("Log Out")
        logOut.clicked.connect(self.onClickExit)
        logOut.clicked.connect(self.close)


        layout = QVBoxLayout()
        layout.addWidget(newEmployee)
        layout.addWidget(deleteEmployee)
        layout.addWidget(deleteReservation)
        layout.addWidget(editEmployee)
        layout.addWidget(logOut)

        self.setStyleSheet(stylesheet)
        self.setLayout(layout)

    def onClickExit(self):
        self.sub_window = loginGUI.Login()
        self.sub_window.show()

    def onClickNewEmployee(self):
        self.sub_window = newEmployeeGUI.newEmployee()
        self.sub_window.show()

    def onClickDelete(self):
        self.sub_window = deleteEmployeeGUI.deleteEmployee()
        self.sub_window.show()

    def onClickDeleteReservation(self):
        self.sub_window = deleteReservation.deleteReservation()
        self.sub_window.show()

    def onClickEdit(self):
        self.sub_window = editEmployee.editEmployee()
        self.sub_window.show()



if __name__ == '__main__':
     app = QApplication([])
     window = adminMain()
     window.show()
     sys.exit(app.exec_())
