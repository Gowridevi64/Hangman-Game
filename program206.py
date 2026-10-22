def fact(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result

print(fact(4))