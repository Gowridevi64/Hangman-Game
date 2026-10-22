n=int(input("Enter a number:"))
f=0
for x in range(1,n+1):
	if n%x==0:
		f=f+1
if f==2:
	print("The number is a prime number")
else:
	print("The number is not a prime number")