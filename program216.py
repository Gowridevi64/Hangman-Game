l = [1,2,3,4,5,6,7,8,9]

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

l1 = list(filter(even, l))

print(l1)