myNumber = raw_input("Enter your list's elements: ")
myNumber = myNumber.split()
myNumber = list(map(int, myNumber))
Sum=0
for i in myNumber:
    Sum+=i;
print(Sum)