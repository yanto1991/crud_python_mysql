import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost", 
                                         user="root",
                                         password="",
                                         database="stock_buah")
    if connection.is_connected(): 
        sql_insert = """insert into tbl_buah(nama_buah,total_buah) values (%s, %s)"""
        values = [("Anggur", 10),
        ("Appel", 20),
        ("Melon", 25),
        ("Mangga", 15),
        ("Pisang", 10)]
        for val in values:
            cursor = connection.cursor()
            cursor.execute(sql_insert, val)
            connection.commit()
        print("{} Data Berhasil Ditambahkan".format(len(values)))
except Error as e:
    print("Failed to create table error: {}".format(e))
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Mysql Connection closed")