computer = {
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}
computer['TOSHIBA'] = 10
computer['FUJISTSU'] = 15
computer['ALIENWARE'] = 5

price = {
    'HP':600,
    'DELL':650,
    'MACBOOK':12000,
    'ASUS':400,
    'TOSHIBA':600,
    'FUJISTSU':900,
    'ALIENWARE':1000,
}

total = 0

for key in computer:
    temp = price[key]*computer[key]
    total += temp

print("The total price is ",total)
