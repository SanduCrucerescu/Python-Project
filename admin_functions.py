from datetime import datetime
from connection import connection
import mysql.connector as mysql

cnx = connection[1]
cursor = connection[0]


def delete_employee(employee_firstname, employee_lastname):
    cursor.execute(
        f"DELETE FROM employee WHERE employee_firstname = '{employee_firstname}' and employee_lastname = '{employee_lastname}';"
    )
    cnx.commit()


def search_employee(employee_firstname, employee_lastname):
    cursor.execute(f"SELECT * FROM employee "
                   f"WHERE employee_firstname = '{employee_firstname}' AND employee_lastname = '{employee_lastname}'")
    res = cursor.fetchone()
    res = str(res).strip("(),''")

    if res == "None":
        return False
    else:
        return True


def search_employeeID(empID):
    cursor.execute(f"SELECT * FROM employee  WHERE employee_id = '{empID}'")
    res = cursor.fetchone()
    res = str(res).strip("(),''")

    if res == "None":
        return False
    else:
        return True


def add_employee(employee_firstname, employee_lastname, employee_position, employee_salary, employee_username, empployee_password):
    now = datetime.now()
    employee_employmentdate = now.strftime("%Y-%m-%d")

    try:
        cursor.execute(
            f"INSERT INTO employee (employee_firstname, employee_lastname, employee_position, Employee_emploimentdate, employee_salary) VALUES ('{employee_firstname}', '{employee_lastname}', '{employee_position}', '{employee_employmentdate}', '{employee_salary}');"
        )
        cnx.commit()

        cursor.execute("SET @employee_id = LAST_INSERT_ID()")
        cursor.execute(
            f"INSERT INTO employee_login (employee_id, employee_username, employee_password) VALUES  (@employee_id, '{employee_username}', '{empployee_password}');"
        )
        cnx.commit()
        return True
    except (mysql.Error, mysql.Warning, ValueError) as e:
        print(e)
        return False


def admin_edit_rsvp(rsvp_id):
    cursor.execute(f"DELETE FROM reservation WHERE reservation_id = '{rsvp_id}';")
    cnx.commit()


def search_reservations(rsvp_id):
    cursor.execute(f"SELECT reservation_id FROM reservation where reservation_id = {rsvp_id}")
    res = cursor.fetchone()
    res = str(res).strip("(),''")

    if res == "None":
        return False
    else:
        return True


def admin_edit_employee(employee_id, employee_firstname, employee_lastname, employee_position, employee_salary, employee_username, empployee_password):
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


def logging_main_menu(employee_username, employee_password):
    cursor.execute(
        f"SELECT employee_username, employee_password FROM employee_login WHERE employee_username = '{employee_username}' and employee_password = '{employee_password}';"
    )
    data = "error"
    for i in cursor:  # assigns i (login details) to the cursor to be checked.
        data = i

    if data == "error":
        return 0



    cursor.execute(
        f"SELECT employee_position FROM employee INNER JOIN employee_login ON employee.employee_id = employee_login.employee_id WHERE employee_username = '{employee_username}';"
    )  # grab employee position using their username provided.

    status = cursor.fetchone()
    position = str(status).strip("(),'")


    if position == "General Manager":  # checks for admin or staff.
        print(f"{position}\nWelcome to your Admin page.\n")

        return 1
    else:

        return 0
