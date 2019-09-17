month = int(input("Nhap thang: "))
if(month<=7):
    if(month == 2): print("28")
    elif(month%2==0): print("30")
    else: print("31")
else:
    if(month%2==0): print("31")
    else: print("30")