n=int(input())
while True:
	if n==int(str(n)[::-1]):
		print(n)
		break
	n=n+1