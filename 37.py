def gcd(a,b):
	return 1 if b==0 else gcd(b, a%b)
print(gcd(48,18))
