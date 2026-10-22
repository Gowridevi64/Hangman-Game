def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

l = [10, 15, 20, 25, 30, 35, 40]

l1 = []

for n in l:
    if even(n) == True:
        l1.append(n)

print(l1)