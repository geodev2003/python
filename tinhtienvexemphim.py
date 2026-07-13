tuoi = int(input("Nhập tuổi:"))
la_sinh_vien = input("Bạn là sinh viên (y: đúng , n: sai):").lower()          
ngay = int(input("Bạn muốn xem phim vào thứ mấy (2-8):"))
so_luong = int(input("Số lượng người xem là:"))

gia_ve = 100000

print("\n===============================\n")

if ngay == 7 or ngay == 8:
    gia_ve += 20000
    print("- Thứ 7 và Chủ nhật phụ thu thêm 20.000VNĐ/vé")
    
if tuoi <= 12 or tuoi >= 60:
    ty_le_tra = 0.5
    print("- Người dưới 12 tuổi hoặc trên 60 tuổi được giảm 50% giá vé.")
elif la_sinh_vien == 'y' and (ngay >=2 and ngay <=6):
    ty_le_tra = 0.7
    print("- Sinh viên đi từ thứ 2 đến thứ 6 được giảm 30% giá vé")
else:
    ty_le_tra = 1
    print("- Không thuộc trường hợp áp dụng ưu đãi.")


tong_tien = (gia_ve * ty_le_tra) * so_luong

if so_luong >= 5: 
    tong_tien *= 0.9
    print("- Số lượng >= 5 người được giảm 10% tổng tiền") 

print(f"==> Tổng tiền vé là {tong_tien:,.0f} VNĐ")      