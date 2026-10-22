from random import *

digits = "0123456789"

def get_mno():
    mno = choice("6789")

    for x in range(9):
        mno = mno + choice(digits)

    return mno

print(get_mno())