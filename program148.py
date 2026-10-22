s=input("Enter a word")
v=set(s)
for x in v:
	if x not in "aeiou":
		print(x)