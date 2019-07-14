import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                             database='test',
                             user='root',
                             password='root')
    sql_select_Query = "select * from user"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in python_developers is - ", cursor.rowcount)
    print("Printing each row's column values i.e.  developer record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1],"\n")


    cursor.close()

except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
