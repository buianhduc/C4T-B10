myColor = ['green','blue','yellow','pink']
option = input("Type in item you want to be deleted: ")
if(option.isdigit()):
    myColor.pop(int(option)-1)
else:
    myColor.remove(option)
print(*myColor, sep = ",")