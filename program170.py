d={100:'A',200:'B',300:'c'}
value=input("Enter the values to find key")
for k,v in d.items():
	if v==value:
		print("The corresponding key:",k)