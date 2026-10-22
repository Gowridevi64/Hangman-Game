s=input("Enter a character:")
if s.isalnum():
	print("Alphanumeric Character:")
	if s.isalpha():
		print("Alphabet Character:")
		if s.islower():
			print("It is a lower case alphabet")
		else:
			print("It is a upper case alphaber")
	else:
		print("It is a digit")
elif s.isspace():
	print("It is a space")
else:
	print("It is a Special Characte")