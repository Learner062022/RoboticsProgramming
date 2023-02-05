import string 
import random
characters_generator = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
tuple_numbers = tuple('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
for number in tuple_numbers:
    characters_generator += number
    password = ''
    while len(password) != 10:
        password += random.choice(characters_generator)
    else:
        print(password)
