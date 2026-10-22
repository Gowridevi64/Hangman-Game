from random import *

alphabets = "abcdefghijklmnopqrstuvwxyz"

def get_name():
    name = choice(alphabets).upper()
    n = randint(2, 9)

    for x in range(n):
        name = name + choice(alphabets)

    return name

print(get_name())