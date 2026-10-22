fname = input("Enter file name: ")

f = open(fname, "w")

data = input("Enter data to write: ")

f.write(data)

f.close()