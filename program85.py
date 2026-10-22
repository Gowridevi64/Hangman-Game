list=[1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20,21,22,33,24]
evenList=[]
oddList=[]
for x in list:
	if x%2==0:
		evenList.append(x)
	else:
		oddList.append(x)
print("EvenList is:",evenList)
print("OddList is:",oddList)