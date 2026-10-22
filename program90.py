l=[10,20,30,40,50,10]
x=int(input("Enter an element to remove:"))
while x in l:
	l.remove(x)
print(l)