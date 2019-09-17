from turtle import *
i=int(input("Nhap so canh: "))
angle=360/i
for n in range(i):
    forward(50)
    right(angle)
mainloop()
