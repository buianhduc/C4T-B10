def valid(s):           #kiem tra email
    dot=0
    a=0
    for i in range(len(s)):
        if(s[i]=='@'): a+=1
        elif(s[i]=='.'): dot+=1
    if(a>=1 and dot>=1): return True
    else: return False

def passvalid(s):                           #kiem tra password
    if(len(s)<8): return False
    else:
        char=0
        number=0
        for i in range(len(s)):
            if(s[i].isdigit()==True): number+=1
            elif(s[i].isalpha()==True): char+=1
        if(number<1 or char<1): return False
    return True  



name = raw_input("Nhap ten cua ban: ")

email = raw_input("Nhap email cua ban: ")           #nhap thong tin

password = raw_input("Nhap password cua ban:")
repassword = raw_input("Nhap lai mat khau cua ban: ")

val=valid(email)
valpass=passvalid(password)                             #lay gia tri dung sai cuar email va password

while(repassword!=password or val == False or valpass == False):        #neu 1 trong 3 cai sai
    if(valpass == False):                                                      #neu mat khau sai
        print("Mat khau khong hop le: ")
        password = raw_input("Nhap lai mat khau: ")
        valpass = password
    else:                                                               #neu mat khau dung nhung sai nhap lai
        if(repassword!=password):
            print("Mat khau nhap lai khong trung khop!")
            repassword = raw_input("Nhap lai mat khau cua ban: ")
    
    if(val == False):                                               #neu email sai
        print("Email khong hop le")
        email = raw_input("Nhap lai email: ")
        val=valid(email)


    