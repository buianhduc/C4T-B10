import random

def operator(a,b,oper):                        #Gia tri bieu thuc
    if(oper=='+'): return a+b
    elif(oper == '-'): return a-b
    elif(oper == '*'): return a*b

print("Welcome to your freaking math test")        #Loi chao
print("If it's true, type Y")
print("If it's false, type N")

s=raw_input("Press S to begin ")            #An bat dau

if(s=="S" or s=="s"):           #Neu bat dau
    while True:
        a=random.randint(-100,100)
        b=random.randint(-100,100)          #lay gia tri a,b,c
        c=random.randint(-100,100)
        oper = random.choice('+-*;')           #lay dau
        print("{0}+{1}={2} ?".format(a,b,c))    #in ra cau hoi
        answer=raw_input("Y/N")                 #Nhap cau tra loi
        if(operator(a,b,oper)==c):
            if(answer == "N" or answer =="n"): 
                print("You failed")
                break;
        if(operator(a,b,oper)!=c):                                      #kiem tra
            if(answer == "Y" or answer =="y"): 
                print("You failed")
                break;
        



