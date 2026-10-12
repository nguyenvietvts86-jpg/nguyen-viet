import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# YÊU CẦU 1: Tạo DataFrame chứa 10 sinh viên
# ==========================================
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Điểm chuyên cần': [8.0, 9.0, 7.0, 9.5, 7.5, 6.0, 9.0, 7.0, 7.5, 9.0],
    'Điểm giữa kỳ': [7.5, 8.0, 6.5, 9.0, 7.0, 5.5, 8.5, 7.0, 7.0, 9.0],
    'Điểm cuối kỳ': [8.0, 8.5, 7.0, 9.0, 7.5, 6.5, 8.5, 7.5, 7.5, 9.5]
}

df = pd.DataFrame(data)
print("--- YÊU CẦU 1: BẢNG DỮ LIỆU BAN ĐẦU ---")
display(df)


# ==========================================
# YÊU CẦU 2: Tính điểm tổng kết
# Công thức: 20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ
# ==========================================
df['Tong_ket'] = (
    0.2 * df['Điểm chuyên cần'] +
    0.3 * df['Điểm giữa kỳ'] +
    0.5 * df['Điểm cuối kỳ']
)

print("\n--- YÊU CẦU 2: BẢNG DỮ LIỆU SAU KHI TÍNH ĐIỂM TỔNG KẾT ---")
display(df)


# ==========================================
# YÊU CẦU 3: Xếp loại sinh viên
# >= 8.5: Giỏi | 7.0-<8.5: Khá | 5.0-<7.0: Trung bình | < 5.0: Yếu
# ==========================================
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

print("\n--- YÊU CẦU 3: BẢNG DỮ LIỆU SAU KHI XẾP LOẠI ---")
display(df)


# ==========================================
# YÊU CẦU 4: Thống kê cơ bản
# ==========================================
# Điểm tổng kết trung bình của lớp
dtb_lop = df['Tong_ket'].mean()

# Sinh viên có điểm tổng kết cao nhất
max_sv = df.loc[df['Tong_ket'].idxmax()]

# Sinh viên có điểm tổng kết thấp nhất
min_sv = df.loc[df['Tong_ket'].idxmin()]

# Số sinh viên đạt (điểm tổng kết >= 5.0)
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

print("\n--- YÊU CẦU 4: KẾT QUẢ THỐNG KÊ ---")
print(f"- Điểm tổng kết trung bình của lớp: {dtb_lop:.2f}")
print(f"- Sinh viên có điểm cao nhất: {max_sv['Họ và tên']} ({max_sv['Tong_ket']})")
print(f"- Sinh viên có điểm thấp nhất: {min_sv['Họ và tên']} ({min_sv['Tong_ket']})")
print(f"- Số sinh viên đạt (>= 5.0): {so_sv_dat}")


# ==========================================
# YÊU CẦU 5: Trực quan hóa dữ liệu (Matplotlib)
# ==========================================
plt.figure(figsize=(10, 5))
plt.barh(df['Họ và tên'], df['Tong_ket'], color='skyblue')
plt.xlabel('Điểm Tổng Kết')
plt.ylabel('Họ và Tên Sinh Viên')
plt.title('BIỂU ĐỒ THỂ HIỆN ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN')
plt.xlim(0, 10)

# Hiển thị giá trị điểm trên từng cột ngang
for index, value in enumerate(df['Tong_ket']):
    plt.text(value + 0.1, index, f"{value:.2f}", va='center')

plt.gca().invert_yaxis() # Đảo ngược trục y để sinh viên đầu tiên ở trên cùng
plt.show()
