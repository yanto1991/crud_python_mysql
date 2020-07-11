import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", 
                                         user="root",
                                         password="",
                                         database="stock_buah")
    if connection.is_connected(): 
        sql_delete = """delete from tbl_buah where id_buah=%s"""
        val = (1, )
        cursor = connection.cursor()
        cursor.execute(sql_delete, val)
        connection.commit()
        print("{} Data Berhasil dihapus".format(cursor.rowcount))
except Error as e:
    print("Failed to delete data, error: {}".format(e))
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Mysql Connection closed")