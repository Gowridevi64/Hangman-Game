w=input("Enter word to search for vowels:")
s=set(w)
vowels={"a","e","i","o","u"}
d=s.intersection(vowels)
print(d)