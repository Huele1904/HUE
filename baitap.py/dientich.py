
def tinh_dien_tich_chu_nhat(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

# Nhập chiều dài và chiều rộng từ người dùng
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))

# Tính và hiển thị kết quả
dien_tich = tinh_dien_tich_chu_nhat(chieu_dai, chieu_rong)
print(f"Diện tích hình chữ nhật là: {dien_tich}")
