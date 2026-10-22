q1 = '''Is python case sensitive when dealing with identifiers?
a.yes
b.No
c.Machine Independent
d.None'''

q2 = '''Which of the following is not a keyword?
a.eval
b.assert
c.local
d.pass'''

q3 = '''Which one of these is a floor division operator?
a./
b.//
c.%
d.None'''

q4 = '''What is the output of this 3*1**3?
a.27
b.9
c.3
d.1'''

questions = {q1: "a", q2: "a", q3: "b", q4: "c"}

name = input("Enter your name: ")
print("Hello", name, "Welcome to the quiz")

score = 0

for i, j in questions.items():
    print()
    print(i)

    option = input("Do you want to skip this question (yes/no): ")

    if option == "yes":
        continue

    ans = input("Enter your answer (a/b/c/d): ")

    if ans == questions[i]:
        print("Correct answer! You got 1 point.")
        score = score + 1
    else:
        print("Wrong answer.")

    print("Current score is:", score)

print()
print("Quiz Completed")
print("Final Score:", score)