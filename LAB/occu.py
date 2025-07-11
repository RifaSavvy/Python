a=input("Enter the String")
words=a.split()
c=list(set(words))
print(c)
for i in c:
	count=0
	for j in words:
		if i==j:
			count+=1
	print("Occurance of Word",i,"is",count)
			
		
