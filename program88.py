n=int(input("Enter number of values:"))
list=[]
for x in range(n):
	value=int(input("Enter the values in the list:"))
	list.append(value)
search=int(input("Enter a element to search:"))
found=False
for  value in list:
	if value==search:
		found=True
if found:
    print("Element is found in the list:")
else:
    print("Element is not found in the list:")