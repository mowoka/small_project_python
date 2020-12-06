import random, string


password_lenght = int(input("How long would does your password to be ?? "))

password_caracthers = string.ascii_letters + string.digits + string.punctuation

password = []

for x in range(password_lenght):
    password.append(random.choice(password_caracthers))

print(''.join(password))
