n=int(input("Enter the number of value in the list:"))
list=[]
for x in range(n):
	value=int(input("Enter the value in the list:"))
	list.append(value)
list.sort()
print(list[-1])