class LichTiepNhanGiaoDichLam:
    def __init__(self, conn):
        self.conn = conn

    def lay_lich_tiep_nhan(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM lich_tiep_nhan"
        cursor.execute(query)
        return cursor.fetchall()
