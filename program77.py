l = [22, 33, 44, 55, 66, 77]

x = int(input("Enter any element to find index value: "))

if x in l:
    i = l.index(x)
    print(i)
else:
    print("Specified element not found")