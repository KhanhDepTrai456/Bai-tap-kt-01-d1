# Import thư viện tkinter
from tkinter import *
from tkinter import messagebox

# Tạo cửa sổ chính
window = Tk()
window.title("Máy tính đơn giản")
window.geometry("400x300")

# Hàm kiểm tra đầu vào có phải là số tự nhiên
def is_natural_number(str_num):
    if not str_num.isdigit():
        return False
    num = int(str_num)
    return num >= 0

# Hàm xử lý phép tính
def calculate(operation):
    # Lấy giá trị từ ô nhập liệu
    num1 = entry1.get()
    num2 = entry2.get()
    
    # Kiểm tra đầu vào
    if not is_natural_number(num1) or not is_natural_number(num2):
        result_label.config(text="Lỗi: Vui lòng nhập số tự nhiên!")
        return
    
    # Chuyển đổi sang số
    num1 = int(num1)
    num2 = int(num2)
    
    # Thực hiện phép tính
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result_label.config(text="Lỗi: Không thể chia cho 0!")
            return
        result = num1 / num2
    
    # Hiển thị kết quả
    result_label.config(text=f"Kết quả: {result}")

# Tạo và định vị các thành phần giao diện
Label(window, text="Số thứ nhất:").pack(pady=10)
entry1 = Entry(window)
entry1.pack()

Label(window, text="Số thứ hai:").pack(pady=10)
entry2 = Entry(window)
entry2.pack()

# Khung chứa các nút phép tính
button_frame = Frame(window)
button_frame.pack(pady=20)

# Tạo các nút phép tính
Button(button_frame, text="+", command=lambda: calculate("+"), width=5).pack(side=LEFT, padx=5)
Button(button_frame, text="-", command=lambda: calculate("-"), width=5).pack(side=LEFT, padx=5)
Button(button_frame, text="*", command=lambda: calculate("*"), width=5).pack(side=LEFT, padx=5)
Button(button_frame, text="/", command=lambda: calculate("/"), width=5).pack(side=LEFT, padx=5)

# Nhãn hiển thị kết quả
result_label = Label(window, text="Kết quả: ")
result_label.pack(pady=20)

# Khởi chạy ứng dụng
window.mainloop()