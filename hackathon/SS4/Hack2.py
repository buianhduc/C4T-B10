name = input("Nhap ten cua ban: ")
email = input("Nhap email cua ban: ")
password = input("Nhap password cua ban:")
repassword = input("Nhap laij mat khau cua ban: ")
while(repassword!=password):
    print("Mat khau nhap lai khong trung khop!")
    repassword = input("Nhap lai mat khau cua ban: ")
    