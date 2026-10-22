name=input("Enter name:")
n=int(input("Enter of subjects:"))
marks=[]
for x in range(n):
	m=int(input("Enter marks:"))
	marks.append(m)
total=sum(marks)
avg=total/n
result="Pass"
for m in marks:
	if m<35:
		result="Fail"
print("Name:",name)
print("Marks",marks)
print("Total",total)
print("Avg",avg)
print("Result",result)