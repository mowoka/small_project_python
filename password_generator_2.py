import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = int(input('Input number of password ? '))

lenght = int(input('Password lenght? '))

for p in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)