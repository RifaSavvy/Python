year= int(input("Enter a year:"))
if(year % 400==0)or (year % 100!=0 and year % 4==0):
	 print("Leap year")
else: 
 	print("Not a leap year")
