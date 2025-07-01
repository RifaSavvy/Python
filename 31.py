#factorial using recursive function

def factorial(n):
	if n==0:
		return 1
	return n * factorial(n-1)
print(factorial(5))

#alculates the factorial of a number recursively, which means the function keeps calling itself with smaller values of n until it hits 0, and then it multiplies the results back up.
