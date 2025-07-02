s= input("Enter String: ")
vowels= "aeiouAEIOU"
v,c=0,0
for ch in s:
	if ch.isalpha():
	#used to check whether string or char is an alphabet..every datatype is assosciated with a class 
		if ch in vowels:
			v +=1
		else:
			c+=1
print("Vowels:",v,"Consonants:",c)
