l=[10,202,30,40,30,100]
x=int(input("Enter an element to remove:"))
if x in l:
	l.remove(x)
else:
	print("Specified element not found")