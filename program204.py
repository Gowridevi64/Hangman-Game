a=10
def f1():
	global a
	a=30
	print(a)
def f2():
	global a 
	a=40
	print(a)
def f3():
	print(a)
f1()
f2()
f3()