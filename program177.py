n = int(input("Enter number of students: "))
d = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter the student marks: "))
    d[name] = marks

while True:
    name = input("Enter the student name to get marks: ")
    marks = d.get(name, -1)

    if marks == -1:
        print("Student not found")
    else:
        print("The marks of", name, "are", marks)

    option = input("Do you want to find another student marks (yes/no): ")

    if option == "no":
        break

print("Thank you for using the application")