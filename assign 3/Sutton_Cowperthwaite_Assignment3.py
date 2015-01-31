"""
Assignment 3

Author: Sutton Cowperthwaite
Description: Investment Calculator where you can find value with input of time in years
rate compounded, and yearly rate

"""

# futval.py

#	 A program to compute the value of an investment

#	 carried n years into the future



def main():

	years=eval(input("Enter years"))
	print("This program calculates the future value")

	print("of a", years,"-year investment.")

	principal = eval(input("Enter the initial principal: "))

	npr = eval(input("Enter the interest rate: "))

	compound=eval(input("Enter the number of compunding periods per year: "))

	

	for i in range(compound*years):

		principal = principal*(1+npr/compound)

	print("The value in", years, "years is:", principal)



main()
