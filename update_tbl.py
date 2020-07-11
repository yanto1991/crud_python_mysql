import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", 
                                         user="root",
                                         password="",
                                         database="stock_buah")
    if connection.is_connected(): 
        sql_upate = """update  tbl_buah set total_buah=%s where nama_buah = %s"""
        val = (5, "Anggur")
        cursor = connection.cursor()
        cursor.execute(sql_upate, val)
        connection.commit()
        print("{} Table Berhasil DiUpdate".format(cursor.rowcount))
except Error as e:
    print("Failed to create table error: {}".format(e))
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Mysql Connection closed")