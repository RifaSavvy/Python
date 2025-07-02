with open("filename.txt") as f:
	words= f.read().split()
	print("word count:",len(words))
