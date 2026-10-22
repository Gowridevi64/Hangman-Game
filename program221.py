from functools import reduce
l=[10,20,30,40,50,60,70,80]
l1=reduce(lambda x,y:x+y,l)
print(l1)