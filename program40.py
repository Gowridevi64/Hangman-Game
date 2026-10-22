mail=input("Enter your mailid:")
try:
	i=mail.index('@')
	print("Your mailid is valid")
except valueError:
	print("Your mail is invalid")
