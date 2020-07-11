import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", 
                                         user="root", 
                                         password="")

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE Database stock_buah")
        print("Database Berhasil dibuat")
except Error as e:
    print("Failed to createDb", e)
finally:
    if (connection.is_connected()):
        cursor.close
        connection.close()
        print("mysql connection closed")