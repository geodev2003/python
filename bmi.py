w = float(input("Nhập cân nặng (kg): "))
h = float(input("Nhập chiều cao (m): "))

bmi = w / (h**2)
print("\nBMI: ", + bmi)

if (bmi > 0 and bmi < 18.5):
    print("Thiếu cân")
elif (bmi >= 18.5 and bmi < 25):
    print("Bình thường")
elif (bmi >= 25 and bmi < 30):
    print("Thừa cân")
else:
    print("Béo phì")
    
# Tính cân nặng lý tưởng
# BMI lý tưởng là 22
# Suy ra W = 22 * (h**2)
ideal_w = 22 * (h**2)
print(f"\nIdeal weight: {ideal_w:.1f} kg")

# So sánh sự chênh lệch
diff = w - ideal_w

if diff > 0.5:
    print(f"Bạn đang dư khoảng  {diff:.1f} kg so với cân nặng lý tưởng")
elif diff < -0.5:
    print(f"Bạn cần tăng thêm {abs(diff):.1f} kg so với cân nặng hiện tại")
else:
    print("Tuyệt vời cân nặng bạn đang ở mức lý tưởng")