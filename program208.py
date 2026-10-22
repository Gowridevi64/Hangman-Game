count=0
def factorial(n):
	global count
	count=count+1
	print("Executing factorial with n values:",n)
	if n==0:
		result=1
	else:
		result=n*factorial(n-1)
	return result
print(factorial(3))
print(count)