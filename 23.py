#prime or not
n= int(input("Enter a number: "))
if n>1: #negative paadilla
	for i in range(2, int(n/2)+1): #1 allathond 2inn thodangi....+1 should include n/2
		if( n % i) == 0:
			print(n,"is not a prime number")
			break
	else:
			print(n, "is a prime number")
else:
	print(n, "is not a prime number")
