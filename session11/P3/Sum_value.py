computer = {
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}
computer['TOSHIBA'] = 10

sum = 0

for key in computer:
    sum+=computer[key]

print("There are ",sum," computers on stock")