myNumber = input("Enter your list's elements: ")
myNumber = myNumber.split()
myNumber = list(map(int, myNumber))

print("All even numbers: ")
for i in myNumber:
    if i%2==0:
        print(i, end = ',')
print('\n')
