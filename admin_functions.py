from datetime import datetime
import mysql.connector as mysql

def delete_employee(employee_firstname, employee_lastname):
    cnx = mysql.connect(host="localhost", user="root", password="Crucerescu12?", database="Hotel_Management")
    cursor = cnx.cursor()
    cursor.execute(
        f"DELETE FROM employee WHERE employee_firstname = '{employee_firstname}' and employee_lastname = '{employee_lastname}';"
    )
    cnx.commit()
    cursor.close()


def search_employee(employee_firstname, employee_lastname):
    cnx = mysql.connect(host="localhost", user="root", password="Crucerescu12?", database="Hotel_Management")
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM employee "
                   f"WHERE employee_firstname = '{employee_firstname}' AND employee_lastname = '{employee_lastname}'")
    res = cursor.fetchone()
    res = str(res).strip("(),''")

    cursor.close()
    if res == "None":
        return False
    else:
        return True


def search_employeeID(empID):
    cnx = mysql.connect(host="localhost", user="root", password="Crucerescu12?", database="Hotel_Management")
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM employee  WHERE employee_id = '{empID}'")
    res = cursor.fetchone()
    res = str(res).strip("(),''")

    cursor.close()
    if res == "None":
        return False
    else:
        return True


def add_employee(employee_firstname, employee_lastname, employee_position, employee_salary, employee_username, empployee_password):
    cnx = mysql.connect(host="localhost", user="root", password="Crucerescu12?", database="Hotel_Management")
    cursor = cnx.cursor()
    now = datetime.now()
    employee_employmentdate = now.strftime("%Y-%m-%d")

    cursor.execute("START TRANSACTION; "
                    f"INSERT INTO employee (employee_firstname, employee_lastname, employee_position, Employee_emploimentdate, employee_salary) "
                    f"VALUES ('{employee_firstname}', '{employee_lastname}', '{employee_position}', '{employee_employmentdate}', '{employee_salary}'); "
                    f"SET @employee_id = LAST_INSERT_ID(); "
                    f"INSERT INTO employee_login (employee_id, employee_username, employee_password) "
                    f"VALUES  (@employee_id, '{employee_username}', '{empployee_password}'); "
                    "COMMIT;")


def admin_edit_rsvp(rsvp_id):
    cnx = mysql.connect(host="localhost", user="root", password="Crucerescu12?", database="Hotel_Management")
    cursor = cnx.cursor()
    cursor.execute(f"DELETE FROM reservation WHERE reservation_id = '{rsvp_id}';")
    cnx.commit()
    cursor.close()


def search_reservations(rsvp_id):
    cnx = mysql.connect(host="localhost", user="root", password="Crucerescu12?", database="Hotel_Management")
    cursor = cnx.cursor()
    cursor.execute(f"SELECT reservation_id FROM reservation where reservation_id = {rsvp_id}")
    res = cursor.fetchone()
    res = str(res).strip("(),''")

    cursor.close()
    if res == "None":
        return False
    else:
        return True


def admin_edit_employee(employee_id, employee_firstname, employee_lastname, employee_position, employee_salary, employee_username, empployee_password):
    cnx = mysql.connect(host="localhost", user="root", password="Crucerescu12?", database="Hotel_Management")
    cursor = cnx.cursor()
    cursor.execute(
        f"START TRANSACTION; "
        f"UPDATE employee "
        f"SET Employee_firstname = '{employee_firstname}' , Employee_lastname = '{employee_lastname}', "
        f"Employee_position = '{employee_position}' , Employee_salary = {employee_salary} "
        f"WHERE Employee_id = {employee_id};"
        f"UPDATE employee_login "
        f"SET employee_username = '{employee_username}' , employee_password = '{empployee_password}'"
        f"WHERE employee_id = {employee_id}; "
        f"COMMIT;"
    )
    cursor.close()



def logging_main_menu(employee_username, employee_password):
    # cursor.execute(
    #     f"SELECT employee_username, employee_password FROM employee_login WHERE employee_username = '{employee_username}' and employee_password = '{employee_password}';"
    # )
    # data = "error"
    # for i in cursor:  # assigns i (login details) to the cursor to be checked.
    #     data = i
    #
    # if data == "error":
    #     return 0

    c = mysql.connect(host="localhost", user="root", password = "Crucerescu12?" ,database="Hotel_Management")
    con = c.cursor()
    con.execute(
        f"SELECT employee_position FROM employee INNER JOIN employee_login ON employee.employee_id = "
        f"employee_login.employee_id WHERE employee_username = '{employee_username}' and employee_password = '{employee_password}'; "
    )  # grab employee position using their username provided.

    status = con.fetchone()

    position = str(status).strip("(),'")
    con.close()

    if position == "General Manager":  # checks for admin or staff.
        return 1
    else:
        return 0


