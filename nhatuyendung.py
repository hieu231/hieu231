import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class NhaTuyenDungForm:
    def __init__(self, root):
        self.root = root
        self.label_title = ttk.Label(root, text="Quản lý nhà tuyển dụng", font=("Arial", 18, "bold"))
        self.label_title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.tree = ttk.Treeview(root, columns=('#1', '#2', '#3', '#4', '#5', '#6'), show="headings")
        self.tree.heading('#1', text='ID', anchor='w')
        self.tree.heading('#2', text='Tên công ty', anchor='w')
        self.tree.heading('#3', text='Địa chỉ', anchor='w')
        self.tree.heading('#4', text='Điện thoại', anchor='w')
        self.tree.heading('#5', text='Email', anchor='w')
        self.tree.heading('#6', text='Ngày tạo', anchor='w')
        self.tree.pack()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.btn_add = tk.Button(self.btn_frame, text="Thêm nhà tuyển dụng", command=self.add_nhatuyendung)
        self.btn_add.grid(row=0, column=0, padx=10)

        self.btn_edit = tk.Button(self.btn_frame, text="Sửa thông tin", command=self.edit_nhatuyendung)
        self.btn_edit.grid(row=0, column=1, padx=10)

        self.btn_delete = tk.Button(self.btn_frame, text="Xoá nhà tuyển dụng", command=self.delete_nhatuyendung)
        self.btn_delete.grid(row=0, column=2, padx=10)

        self.load_nhatuyendung()

    def load_nhatuyendung(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='quan_ly_viec_lam',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nha_tuyen_dung")
            nhatuyendung_data = cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in nhatuyendung_data:
                self.tree.insert('', 'end', values=row)
            cursor.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def add_nhatuyendung(self):
        def add_nhatuyendung_to_db():
            ten_cong_ty = entry_ten_cong_ty.get()
            dia_chi = entry_dia_chi.get()
            dien_thoai = entry_dien_thoai.get()
            email = entry_email.get()

            if ten_cong_ty == "" or dia_chi == "" or dien_thoai == "" or email == "":
                messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin.")
                return

            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    database='quan_ly_viec_lam',
                    user='root',
                    password=''
                )
                cursor = conn.cursor()
                insert_query = "INSERT INTO nha_tuyen_dung (ten_cong_ty, dia_chi, dien_thoai, email) VALUES (%s, %s, %s, %s)"
                data = (ten_cong_ty, dia_chi, dien_thoai, email)
                cursor.execute(insert_query, data)
                conn.commit()
                messagebox.showinfo("Thành công", "Thêm nhà tuyển dụng thành công.")
                self.load_nhatuyendung()
                add_window.destroy()
            except mysql.connector.Error as e:
                messagebox.showerror("Lỗi", f"Lỗi: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

        add_window = tk.Toplevel(self.root)
        add_window.title("Thêm nhà tuyển dụng")

        label_ten_cong_ty = tk.Label(add_window, text="Tên công ty:")
        label_ten_cong_ty.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        entry_ten_cong_ty = tk.Entry(add_window, width=50)
        entry_ten_cong_ty.grid(row=0, column=1, padx=10, pady=5)

        label_dia_chi = tk.Label(add_window, text="Địa chỉ:")
        label_dia_chi.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        entry_dia_chi = tk.Entry(add_window, width=50)
        entry_dia_chi.grid(row=1, column=1, padx=10, pady=5)

        label_dien_thoai = tk.Label(add_window, text="Điện thoại:")
        label_dien_thoai.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        entry_dien_thoai = tk.Entry(add_window, width=50)
        entry_dien_thoai.grid(row=2, column=1, padx=10, pady=5)

        label_email = tk.Label(add_window, text="Email:")
        label_email.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entry_email = tk.Entry(add_window, width=50)
        entry_email.grid(row=3, column=1, padx=10, pady=5)

        btn_add = tk.Button(add_window, text="Thêm", command=add_nhatuyendung_to_db)
        btn_add.grid(row=4, column=1, padx=10, pady=10)

    def edit_nhatuyendung(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhà tuyển dụng để sửa.")
            return

        data = self.tree.item(selected_item, 'values')
        nha_tuyen_dung_id = data[0]

        def edit_nhatuyendung_in_db():
            ten_cong_ty = entry_ten_cong_ty.get()
            dia_chi = entry_dia_chi.get()
            dien_thoai = entry_dien_thoai.get()
            email = entry_email.get()

            if ten_cong_ty == "" or dia_chi == "" or dien_thoai == "" or email == "":
                messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin.")
                return

            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    database='quan_ly_viec_lam',
                    user='root',
                    password=''
                )
                cursor = conn.cursor()
                update_query = "UPDATE nha_tuyen_dung SET ten_cong_ty=%s, dia_chi=%s, dien_thoai=%s, email=%s WHERE nha_tuyen_dung_id=%s"
                data = (ten_cong_ty, dia_chi, dien_thoai, email, nha_tuyen_dung_id)
                cursor.execute(update_query, data)
                conn.commit()
                messagebox.showinfo("Thành công", "Sửa thông tin nhà tuyển dụng thành công.")
                self.load_nhatuyendung()
                edit_window.destroy()
            except mysql.connector.Error as e:
                messagebox.showerror("Lỗi", f"Lỗi: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Sửa thông tin nhà tuyển dụng")

        label_ten_cong_ty = tk.Label(edit_window, text="Tên công ty:")
        label_ten_cong_ty.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        entry_ten_cong_ty = tk.Entry(edit_window, width=50)
        entry_ten_cong_ty.grid(row=0, column=1, padx=10, pady=5)
        entry_ten_cong_ty.insert(0, data[1])

        label_dia_chi = tk.Label(edit_window, text="Địa chỉ:")
        label_dia_chi.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        entry_dia_chi = tk.Entry(edit_window, width=50)
        entry_dia_chi.grid(row=1, column=1, padx=10, pady=5)
        entry_dia_chi.insert(0, data[2])

        label_dien_thoai = tk.Label(edit_window, text="Điện thoại:")
        label_dien_thoai.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        entry_dien_thoai = tk.Entry(edit_window, width=50)
        entry_dien_thoai.grid(row=2, column=1, padx=10, pady=5)
        entry_dien_thoai.insert(0, data[3])

        label_email = tk.Label(edit_window, text="Email:")
        label_email.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entry_email = tk.Entry(edit_window, width=50)
        entry_email.grid(row=3, column=1, padx=10, pady=5)
        entry_email.insert(0, data[4])

        btn_edit = tk.Button(edit_window, text="Lưu", command=edit_nhatuyendung_in_db)
        btn_edit.grid(row=4, column=1, padx=10, pady=10)

    def delete_nhatuyendung(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhà tuyển dụng để xoá.")
            return

        confirmation = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xoá nhà tuyển dụng này?")
        if confirmation:
            nha_tuyen_dung_id = self.tree.item(selected_item, 'values')[0]
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    database='quan_ly_viec_lam',
                    user='root',
                    password=''
                )
                cursor = conn.cursor()
                delete_query = "DELETE FROM nha_tuyen_dung WHERE nha_tuyen_dung_id = %s"
                cursor.execute(delete_query, (nha_tuyen_dung_id,))
                conn.commit()
                messagebox.showinfo("Thành công", "Xoá nhà tuyển dụng thành công.")
                self.load_nhatuyendung()
            except mysql.connector.Error as e:
                messagebox.showerror("Lỗi", f"Lỗi: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = NhaTuyenDungForm(root)
    app.run()
