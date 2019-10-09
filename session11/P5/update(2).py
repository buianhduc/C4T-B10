computer = {
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}
computer['TOSHIBA'] = 10
computer['FUJITSU'] = 15
computer['ALIENWARE'] = 5

price = {
    'HP':600,
    'DELL':650,
    'MACBOOK':12000,
    'ASUS':400,
    'ACER':350,
    'TOSHIBA':600,
    'FUJISTSU':900,
    'ALIENWARE':1000,
}

computer['DELL'] += 10
computer['MACBOOK'] -= 2

brand, quantity = input("What brand do you want to buy: ").split(':')
brand = brand.upper()
quantity = int(quantity)

if(quantity > computer[brand]):
    print("Sorry, we don't have enough product for you to buy :< ")
else:
    print("The total price of {0} {1} computers is {2}".format(quantity,brand,price[brand]*quantity))
    computer[brand] -= quantity
