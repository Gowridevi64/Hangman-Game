import mathopr
def isprime(num):
    c = 0
    for x in range(1, num + 1):
        if num % x == 0:
            c = c + 1

    if c == 2:
        return True
    else:
        return False

print(isprime(7))
print(isprime(8))
print(isprime(13))
print(isprime(15))