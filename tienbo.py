bill = float(input("Nhập tổng tiền hóa đơn (đ):"))
tip_percent = float(input("Nhập tỉ lệ tiền bo (%): "))
total_people = int(input("Nhập tổng số người đi: "))

tip = (bill * tip_percent) / 100

total_bill = bill + tip 

money_per_one = total_bill / total_people

print(f"Tiền tip là: {tip}đ")
print(f"Tổng tiền thanh toán là: {total_bill}đ")
print(f"Tiền của 1 người là: {money_per_one}đ")