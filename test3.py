# Hybrid solution of periodic interest calculator
# Used for Assignment 9

# Author: Jeffrey LaMarche
# Data: October 30th 2013

def main():
	print()
	print("This program calculates the future value of an investment.")
	print()

	principal = eval(input("Enter the initial principal: "))
	rate = eval(input("Enter the interest rate: "))
	periods = eval(input("Enter the number of compounding periods per year: "))
	years = eval(input("Enter the number of years: "))

	print()
	
	for i in range(years * periods):
		interest = principal * (rate / periods)
		principal = principal + interest
		
		print("Year {:2} period {} interest earned: ${:5.2f}".format((i // periods) + 1, (i % 4) + 1, interest))

	print("\nThe amount in {} years is: ${:5.2f}".format(years, principal))
	
	print()

main()
