computer = {
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}
computer['TOSHIBA'] = 10
brand = input("Enter the computer brand: ")
computer[brand] = int(input("How many are there: "))
