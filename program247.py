from random import *

digits = "0123456789"

def get_eno():
    eno = "E-"

    for x in range(4):
        eno = eno + choice(digits)

    return eno

print(get_eno())