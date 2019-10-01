myNumber = [3, 16, 95, 44, 15, 92, 21, 30, 57, 27, 93, 52, 13, 82, 50, 94, 11, 87, 57, 50, 23]
a = int(input("Number: "))
d = False
for i in range(len(myNumber)):
    if(a == myNumber[i]): 
        print("Found it. It's at position ",i+1)
        d = True
if(d==False): print("Can't be found")