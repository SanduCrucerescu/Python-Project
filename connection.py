import mysql.connector as mysql
import pandas as pd

def connection():
    cnx = mysql.connect(host="localhost", user="root", password = "Crucerescu12?" ,database="Hotel_Management")
    mycursor = cnx.cursor(buffered=True)
    return mycursor, cnx

connection = connection()

# connection[0].execute("select * from customer where customers_id = 3")
# result = connection[0].fetchone()
# print(result)
# csvPlanets = pd.read_csv("/Users/alex/Downloads/Hotel DB Data - Employee Login Data.csv", index_col=False, # change the location of the cvs in order for the program to work
#                              delimiter=',')
# for i, row in csvPlanets.iterrows():
#     sql = "INSERT INTO employee_login VALUES(%s,%s,%s)"
#     connection[0].execute(sql, tuple(row))
#     connection[1].commit()
