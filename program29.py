username = ""
i = 0

while username != "gowri@gmail.com":
    username = input("Enter username: ")
    i = i + 1

    if username == "gowri@gmail.com":
        print("Login Successful")
        break

    if i == 10:
        print("Your maximum attempts completed")
        break