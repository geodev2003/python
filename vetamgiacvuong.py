h = int(input("Nhập chiều cao tam giác vuông:"))

# Canh lề trái
for i in range(0, h+1):
    print("*" * i)
    
# Canh lề trái - đảo ngược
for i in range(h, 0, -1):
    print("*" * i)
    
# Canh lề phải
for i in range(0, h+1):
    khoang_trang = " " * (h - i)
    dau_sao = "*" * i
    
    print(khoang_trang, dau_sao)
    
# Canh lề phải - đảo ngược
for i in range(h, 0, - 1):
    khoang_trang = " " * (h - i)
    dau_sao = "*" * i
    
    print(khoang_trang + dau_sao)
    

# Hàm rjust() - Right Justify - Căn lề phải
for i in range(0, h):
    print(("*" * i).rjust(h))
    

# Hàm ljust() - Left Justify - Căn lề trái
for i in range(0, h):
    print(("*" * i).ljust(h))
    

# Hàm center() - Center - Căn giữa
#        *    
#       ***   
#      *****  
#     ******* 
#    *********

chieu_rong_day = 2 * h - 1

for i in range(1, h + 1):
    so_sao = 2 * i - 1
    chuoi_sao = "*" * so_sao
    
    print(chuoi_sao.center(chieu_rong_day))