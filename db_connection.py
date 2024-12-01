import mysql.connector

class DatabaseConnection:
    @staticmethod
    def get_connection():
        """Kết nối đến cơ sở dữ liệu MySQL"""
        return mysql.connector.connect(
            host='localhost',            # Máy chủ cơ sở dữ liệu
            database='quan_ly_viec_lam', # Tên cơ sở dữ liệu
            user='root',                 # Tên người dùng MySQL (mặc định là 'root')
            password='',                 # Mật khẩu MySQL, để trống nếu không có
            port=3306                    # Port mặc định của MySQL
        )
