second = int(input("Nhập vào số giây:"))

h = second // 3600
m = (second % 3600)/60
s = (second % 3600) % 60

print(f"Tương ứng với {h} giờ {m:.0f} phút {s} giây")