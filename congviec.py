from db_connection import DatabaseConnection

class CongViec:
    @staticmethod
    def load_cong_viec():
        """Tải danh sách công việc"""
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cong_viec")
        return cursor.fetchall()

    @staticmethod
    def add_cong_viec(ten_cong_viec, mo_ta, luong, ngay_dang, nha_tuyen_dung_id):
        """Thêm công việc mới"""
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cong_viec (ten_cong_viec, mo_ta, luong, ngay_dang, nha_tuyen_dung_id) "
                       "VALUES (%s, %s, %s, %s, %s)", 
                       (ten_cong_viec, mo_ta, luong, ngay_dang, nha_tuyen_dung_id))
        conn.commit()
