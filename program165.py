d={45:'hyd',33:'pune',54:'delhi'}
key=int(input("Enter the key to find value:"))
if key in d:								
	print("The corresponding value is:",d.get(key))
else:
	print("The specified key is not available")