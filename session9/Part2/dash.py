from turtle import *

def draw(colour, count):
    pensize(10)
    shape("turtle")
    color(colour)
    if(count == 0):
        forward(100)
    elif(count%2!=0):
        right(90)
        penup()
        forward(10)
        pendown()
        right(90)
        forward(100)
    else:
        left(90)
        penup()
        forward(10)
        pendown()
        left(90)
        forward(100)



myColor = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
count = 0
for i in myColor:
    draw(i,count)
    count += 1

mainloop()