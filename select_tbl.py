import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", 
                                         user="root",
                                         password="",
                                         database="stock_buah")
    if connection.is_connected(): 
        sql_select = """select * from tbl_buah"""
        cursor = connection.cursor()
        cursor.execute(sql_select)
        result = cursor.fetchall()
        for vals in result:
            print(vals)
except Error as e:
    print("Failed to create table error: {}".format(e))
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Mysql Connection closed")