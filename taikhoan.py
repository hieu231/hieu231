class TaiKhoan:
    @staticmethod
    def tao_tai_khoan(username, password, role):
        conn = TaiKhoan.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO taikhoan (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, role))
        conn.commit()
        cursor.close()
        conn.close()
