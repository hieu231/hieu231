from tkinter import ttk, Toplevel, messagebox
import mysql.connector


class ThongKe:
    """Lớp thống kê dữ liệu từ cơ sở dữ liệu"""
    
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host='localhost',
            database='quan_ly_viec_lam',
            user='root',
            password=''
        )
    
    @staticmethod
    def get_thong_ke():
        """Lấy thống kê dữ liệu từ cơ sở dữ liệu"""
        conn = ThongKe.get_connection()
        cursor = conn.cursor()
        query = """
            SELECT gioi_tinh, COUNT(*) 
            FROM ung_vien 
            GROUP BY gioi_tinh
        """
        cursor.execute(query)
        return cursor.fetchall()


class ThongKeForm:
    """Lớp giao diện hiển thị thống kê"""

    def __init__(self, root):
        self.root = root

        # Tạo bảng hiển thị thống kê
        self.tree = ttk.Treeview(root, columns=('gioi_tinh', 'so_luong'), show='headings')
        self.tree.heading('gioi_tinh', text='Giới tính')
        self.tree.heading('so_luong', text='Số lượng')
        self.tree.pack(fill="both", expand=True)

        # Nút tải thống kê
        self.load_button = ttk.Button(root, text="Tải thống kê", command=self.load_thong_ke)
        self.load_button.pack(padx=5, pady=5)

    def load_thong_ke(self):
        """Tải dữ liệu thống kê từ cơ sở dữ liệu"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            rows = ThongKe.get_thong_ke()
            for row in rows:
                self.tree.insert('', 'end', values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")
