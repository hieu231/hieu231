import mysql.connector
from tkinter import messagebox

class Login:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host='localhost',
            database='quan_ly_viec_lam',
            user='root',
            password=''
        )

    @staticmethod
    def validate_login(username, password):
        conn = Login.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM nguoi_dung WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        conn.close()
        return result
