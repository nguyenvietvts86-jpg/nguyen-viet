import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu 10 sinh viên
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Điểm chuyên cần': [8.0, 9.0, 7.0, 9.5, 7.5, 6.0, 9.0, 7.0, 7.5, 9.0],
    'Điểm giữa kỳ': [7.5, 8.0, 6.5, 9.0, 7.0, 5.5, 8.5, 7.0, 7.0, 9.0],
    'Điểm cuối kỳ': [8.0, 8.5, 7.0, 9.0, 7.5, 6.5, 8.5, 7.5, 7.5, 9.5]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df['Tong_ket'] = (0.2 * df['Điểm chuyên cần'] + 0.3 * df['Điểm giữa kỳ'] + 0.5 * df['Điểm cuối kỳ']).round(2)

# Xếp loại
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

# Hiển thị bảng điểm
st.subheader("📋 Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df, use_container_width=True)

# Thống kê cơ bản
st.subheader("📊 Thống kê chung của lớp")
dtb_lop = df['Tong_ket'].mean()
max_sv = df.loc[df['Tong_ket'].idxmax()]
min_sv = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Điểm tổng kết trung bình của lớp", value=f"{dtb_lop:.2f}")
    st.metric(label="Số sinh viên đạt (>= 5.0)", value=so_sv_dat)

with col2:
    st.metric(label="SV điểm cao nhất", value=f"{max_sv['Họ và tên']} ({max_sv['Tong_ket']})")
    st.metric(label="SV điểm thấp nhất", value=f"{min_sv['Họ và tên']} ({min_sv['Tong_ket']})")

st.markdown("---")

# Danh sách chọn sinh viên
st.subheader("🔍 Tra cứu thông tin sinh viên")
selected_name = st.selectbox("Chọn tên sinh viên cần xem:", df['Họ và tên'].tolist())
selected_student = df[df['Họ và tên'] == selected_name].iloc[0]

scol1, scol2, scol3, scol4, scol5 = st.columns(5)
scol1.metric("Chuyên cần", selected_student['Điểm chuyên cần'])
scol2.metric("Giữa kỳ", selected_student['Điểm giữa kỳ'])
scol3.metric("Cuối kỳ", selected_student['Điểm cuối kỳ'])
scol4.metric("Tổng kết", selected_student['Tong_ket'])
scol5.metric("Xếp loại", selected_student['Xep_loai'])

st.markdown("---")

# Biểu đồ cột điểm tổng kết
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 4))
bars = ax.barh(df['Họ và tên'], df['Tong_ket'], color='skyblue', edgecolor='navy')

ax.set_xlabel('Điểm Tổng Kết')
ax.set_ylabel('Họ và Tên Sinh Viên')
ax.set_title('BIỂU ĐỒ THỂ HIỆN ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN')
ax.set_xlim(0, 10)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, f"{width:.2f}", va='center')

ax.invert_yaxis()
st.pyplot(fig)

# Thông tin người tạo ở cuối trang
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: small;'>"
    "Người tạo ứng dụng: Nguyễn Văn Việt - MSSV: 034208010894"
    "</p>", 
    unsafe_allow_html=True
)
