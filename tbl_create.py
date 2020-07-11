import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", 
                                         user="root",
                                         password="",
                                         database="stock_buah")
    if connection.is_connected(): 
        sql_create = """CREATE TABLE tbl_buah(
            id_buah int AUTO_INCREMENT PRIMARY KEY,
            nama_buah varchar(150) NOT NULL,
            total_buah int(125) NOT NULL
        )"""
        cursor = connection.cursor()
        cursor.execute(sql_create)
        print("Execute Table Success")
except Error as e:
    print("Failed to create table error: {}".format(e))
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Mysql Connection closed")