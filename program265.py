class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def display(self):
		print(self.name, self.age)
		
s1=Student("Ravi", 20)
s2=Student("Kiran",21)

s1.display()
s2.display()