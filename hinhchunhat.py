print("Chọn:\n 1. Tính diện tích\n 2. Tính chu vi\n 0. Tính chu vi và diện tích")
s = int(input("Nhập lựa chọn: "))

l = float(input("Nhập chiều dài (m):"))
w = float(input("Nhập chiều rộng (m):"))

cv = (l + w) * 2
dt = l * w

print("===========================")
if s == 1:
    print(f">> Diện tích là: {dt:.2f} m^2")
elif s == 2:
    print(f">> Chu vi là: {cv:.2f} m")
else:
    print(f">> Diện tích là: {dt:.2f} m^2\n Chu vi là: {cv:.2f} m")
