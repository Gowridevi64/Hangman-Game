def flower_line():
    print("🌸" * 25)

def welcome_box(name):
    flower_line()
    print("🌼      ===== OPEN QUIZ =====      🌼")
    flower_line()
    print(f"🌷 Hello {name}! Welcome to the quiz 🌷")
    flower_line()

name = input("Enter your name: ")
welcome_box(name)

# Questions
questions = [
"""1. Is Python case sensitive?
a) Yes
b) No
c) Sometimes
d) None""",

"""2. Which of the following is not a keyword?
a) eval
b) assert
c) pass
d) break""",

"""3. Which one is a floor division operator?
a) /
b) //
c) %
d) **""",

"""4. What is the output of 3*1**3?
a) 27
b) 9
c) 3
d) 1""",

"""5. Which symbol is used for comments?
a) //
b) #
c) /* */
d) --""",

"""6. Which data type is immutable?
a) list
b) set
c) tuple
d) dict""",

"""7. Which keyword is used to define a function?
a) fun
b) define
c) def
d) function""",

"""8. Which operator is used for power?
a) ^
b) **
c) //
d) %""",

"""9. Which one is a loop?
a) if
b) for
c) def
d) try""",

"""10. Output of 5//2?
a) 2.5
b) 3
c) 2
d) 1""",

"""11. Python is?
a) Compiled
b) Interpreted
c) Both
d) None""",

"""12. Which is a valid variable name?
a) 1var
b) var_1
c) var-1
d) @var""",

"""13. List is?
a) Immutable
b) Mutable
c) Both
d) None""",

"""14. Tuple uses?
a) []
b) {}
c) ()
d) <>""",

"""15. Dictionary uses?
a) []
b) {}
c) ()
d) ||""",

"""16. Input function?
a) scan()
b) input()
c) get()
d) read()""",

"""17. Output function?
a) echo()
b) print()
c) show()
d) display()""",

"""18. len() is used for?
a) add
b) length
c) delete
d) none""",

"""19. range() is used in?
a) if
b) loop
c) function
d) class""",

"""20. Python file extension?
a) .pt
b) .py
c) .pyt
d) .python""",

"""21. Boolean values?
a) yes/no
b) true/false
c) 1/0
d) all""",

"""22. Which is a string?
a) 123
b) 'abc'
c) True
d) None""",

"""23. Which is float?
a) 10
b) 10.5
c) '10'
d) True""",

"""24. Which keyword is used for condition?
a) for
b) if
c) def
d) try""",

"""25. Which is logical AND?
a) &&
b) and
c) &
d) &&&"""
]

# Answers
answers = [
"a","a","b","c","b",
"c","c","b","b","c",
"b","b","b","c","b",
"b","b","b","b","b",
"b","b","b","b","b"
]

score = 0

# Quiz Loop
for i in range(len(questions)):
    flower_line()
    print("🌺 Question", i+1)
    flower_line()
    print(questions[i])

    skip = input("🌼 Skip this question? (yes/no): ").lower()
    if skip == "yes":
        continue

    user_answer = input("🌷 Enter your answer (a/b/c/d): ").lower()

    if user_answer == answers[i]:
        print("✅ Correct! +1 point 🌸")
        score += 1
    else:
        print("❌ Wrong! -1 point 🌸")
        score -= 1

    print("🌻 Current score:", score)

flower_line()
print("🌼 ===== QUIZ COMPLETED ===== 🌼")
flower_line()
print(f"🌷 {name}, your final score is: {score} 🌷")
flower_line()