a=10
def f1():
	global a
	a=20
	print(a)
def f2():
	print(a)
f1()
f2()