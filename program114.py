gradelist=[['mahesh','A'],['suresh','B'],['kishore','C'],['kiran','A'],['ramu','B']]
studentListA=[x for x in gradelist if x[-1]=='A']
studentListB=[x for x in gradelist if x[-1]=='B']
studentListC=[x for x in gradelist if x[-1]=='C']
print(studentListA)
print(studentListB)
print(studentListC)