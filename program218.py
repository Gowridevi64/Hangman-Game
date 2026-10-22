l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda n:n%3==0 and n%2==1,l))
print(l1)