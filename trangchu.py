import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

class CongViecForm:
    def __init__(self, root):
        self.root = root
        self.tree = ttk.Treeview(root, columns=('cong_viec_id', 'ten_cong_viec', 'mo_ta', 'luong', 'ngay_dang', 'nha_tuyen_dung_id'), show='headings')
        self.tree.heading('cong_viec_id', text='ID')
        self.tree.heading('ten_cong_viec', text='Tên công việc')
        self.tree.heading('mo_ta', text='Mô tả')
        self.tree.heading('luong', text='Lương')
        self.tree.heading('ngay_dang', text='Ngày đăng')
        self.tree.heading('nha_tuyen_dung_id', text='Nhà tuyển dụng')
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.load_cong_viec()
        
        self.add_button = tk.Button(root, text="Thêm công việc", command=self.add_cong_viec)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.edit_button = tk.Button(root, text="Sửa công việc", command=self.edit_cong_viec)
        self.edit_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.delete_button = tk.Button(root, text="Xoá công việc", command=self.delete_cong_viec)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

    def load_cong_viec(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='quan_ly_viec_lam',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cong_viec")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert('', tk.END, values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def add_cong_viec(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Thêm công việc")
        self.create_cong_viec_form(self.new_window, self.save_new_cong_viec)

    def edit_cong_viec(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Lỗi", "Chọn một công việc để sửa")
            return
        item = self.tree.item(selected_item)
        self.cong_viec_id = item['values'][0]
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Sửa công việc")
        self.create_cong_viec_form(self.new_window, self.save_edited_cong_viec, item['values'])

    def create_cong_viec_form(self, window, save_command, values=None):
        tk.Label(window, text="Tên công việc").grid(row=0, column=0)
        self.ten_cong_viec_entry = tk.Entry(window)
        self.ten_cong_viec_entry.grid(row=0, column=1)
        
        tk.Label(window, text="Mô tả").grid(row=1, column=0)
        self.mo_ta_entry = tk.Entry(window)
        self.mo_ta_entry.grid(row=1, column=1)
        
        tk.Label(window, text="Lương").grid(row=2, column=0)
        self.luong_entry = tk.Entry(window)
        self.luong_entry.grid(row=2, column=1)
        
        tk.Label(window, text="Ngày đăng").grid(row=3, column=0)
        self.ngay_dang_entry = DateEntry(window, date_pattern='y-mm-dd')
        self.ngay_dang_entry.grid(row=3, column=1)
        
        tk.Label(window, text="Nhà tuyển dụng").grid(row=4, column=0)
        self.nha_tuyen_dung_combobox = ttk.Combobox(window)
        self.load_nha_tuyen_dung()
        self.nha_tuyen_dung_combobox.grid(row=4, column=1)
        
        if values:
            self.ten_cong_viec_entry.insert(0, values[1])
            self.mo_ta_entry.insert(0, values[2])
            self.luong_entry.insert(0, values[3])
            self.ngay_dang_entry.set_date(values[4])
            self.nha_tuyen_dung_combobox.set(values[5])
        
        tk.Button(window, text="Lưu", command=save_command).grid(row=5, columnspan=2)

    def load_nha_tuyen_dung(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='quan_ly_viec_lam',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            cursor.execute("SELECT nha_tuyen_dung_id, ten_cong_ty FROM nha_tuyen_dung")
            rows = cursor.fetchall()
            self.nha_tuyen_dung_combobox['values'] = [f"{row[0]} - {row[1]}" for row in rows]
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def save_new_cong_viec(self):
        ten_cong_viec = self.ten_cong_viec_entry.get()
        mo_ta = self.mo_ta_entry.get()
        luong = self.luong_entry.get()
        ngay_dang = self.ngay_dang_entry.get()
        nha_tuyen_dung_id = self.nha_tuyen_dung_combobox.get().split(' ')[0]  # lấy ID nhà tuyển dụng từ combobox
        if not ten_cong_viec or not mo_ta or not luong or not ngay_dang or not nha_tuyen_dung_id:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='quan_ly_viec_lam',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            query = "INSERT INTO cong_viec (ten_cong_viec, mo_ta, luong, ngay_dang, nha_tuyen_dung_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (ten_cong_viec, mo_ta, luong, ngay_dang, nha_tuyen_dung_id))
            conn.commit()
            messagebox.showinfo("Thành công", "Thêm công việc thành công")
            self.load_cong_viec()
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
            self.new_window.destroy()

    def save_edited_cong_viec(self):
        ten_cong_viec = self.ten_cong_viec_entry.get()
        mo_ta = self.mo_ta_entry.get()
        luong = self.luong_entry.get()
        ngay_dang = self.ngay_dang_entry.get()
        nha_tuyen_dung_id = self.nha_tuyen_dung_combobox.get().split(' ')[0]  # lấy ID nhà tuyển dụng từ combobox
        if not ten_cong_viec or not mo_ta or not luong or not ngay_dang or not nha_tuyen_dung_id:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='quan_ly_viec_lam',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            query = """
            UPDATE cong_viec
            SET ten_cong_viec=%s, mo_ta=%s, luong=%s, ngay_dang=%s, nha_tuyen_dung_id=%s
            WHERE cong_viec_id=%s
            """
            cursor.execute(query, (ten_cong_viec, mo_ta, luong, ngay_dang, nha_tuyen_dung_id, self.cong_viec_id))
            conn.commit()
            messagebox.showinfo("Thành công", "Cập nhật công việc thành công")
            self.load_cong_viec()
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
            self.new_window.destroy()

    def delete_cong_viec(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Lỗi", "Chọn một công việc để xóa")
            return
        item = self.tree.item(selected_item)
        cong_viec_id = item['values'][0]
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='quan_ly_viec_lam',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            query = "DELETE FROM cong_viec WHERE cong_viec_id=%s"
            cursor.execute(query, (cong_viec_id,))
            conn.commit()
            messagebox.showinfo("Thành công", "Xóa công việc thành công")
            self.load_cong_viec()
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = CongViecForm(root)
    root.mainloop()
