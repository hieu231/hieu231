from db_connection import DatabaseConnection

class UngVien:
    @staticmethod
    def load_ung_vien():
        """Tải danh sách ứng viên"""
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ung_vien")
        return cursor.fetchall()

    @staticmethod
    def add_ung_vien(ho_ten, ngay_sinh, gioi_tinh, dia_chi, dien_thoai, email):
        """Thêm ứng viên mới"""
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ung_vien (ho_ten, ngay_sinh, gioi_tinh, dia_chi, dien_thoai, email) "
                       "VALUES (%s, %s, %s, %s, %s, %s)", 
                       (ho_ten, ngay_sinh, gioi_tinh, dia_chi, dien_thoai, email))
        conn.commit()
