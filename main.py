# main.py
from tkinter import Tk, messagebox
from trangchu import CongViecForm  # Đảm bảo nhập khẩu đúng class TrangChu từ trangchu.py

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Quản Lý Giao Dịch Việc Làm")
        
        # Khởi tạo và sử dụng TrangChu
        self.trangchu = TrangChu()
        self.trangchu.display()

        # Các thành phần GUI khác (nếu cần)
        # Ví dụ:
        self.quit_button = ttk.Button(root, text="Thoát", command=root.quit)
        self.quit_button.pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
