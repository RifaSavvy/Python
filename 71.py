try:
	x = int(input("Enter number: "))
except ValueError:
	print("Invalid input")
else:
	print("Valid Input")
finally:
	print("End of program")	
