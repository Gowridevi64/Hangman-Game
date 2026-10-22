f = open("fruits.txt", "w")

l = ["apple\n", "banana\n", "grapes\n", "orange\n"]

f.writelines(l)

f.close()