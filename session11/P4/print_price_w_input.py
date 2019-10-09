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

key = input("Enter the brand: ")
print('The price of {0} is {1}'.format(key,price[key]))