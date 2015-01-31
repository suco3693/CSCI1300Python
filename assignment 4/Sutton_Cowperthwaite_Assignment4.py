"""
Assignment 4: Foxes and Rabbits
Author: Sutton Cowperthwaite
Description: Population Model of Foxes and Rabbits on a Small Island
Date: 9/10/13
"""



def run_simulation():	
	import math #Import math files
	print()	# adds a newline for nicer output.
	#Rabbit brith rate
	rBr=0.01 
	#Fox birth rate
	fBr=0.005
	# INTERACT is the likelihood that a rabbit and fox will meet
	I=0.00001
	# SUCCESS is the likelihood that when a fox & rabbit meet that the 
	#   fox catches the rabbit
	S=0.01
	
	#Starting Populations and Days Ran
	R=eval(input("Enter Starting rabbit population: "))
	F = eval(input("Enter Starting fox population: "))
	days=eval(input("Enter number of days you want to run the program for: "))

	# Print out some header info here with labels for days, rabbits, foxes 
	print ("Days \t\t\t Rabbits \t\t\t Foxes")
	

	# Print out the starting simulation values
	print(0,"\t\t\t",R,"\t\t\t\t",F)


	# write a for-loop to iterate through the simulated days
	#Calculate new daily populations
	#Print out new populations
	for i in range(days+1):
		
		dF=I*S*R*F-fBr*F
		dR=rBr*R-(I*R*F)
		R=round(R+dR)
		F=round(F+dF)
		print(i+1,"\t\t\t",R,"\t\t\t\t",F)
	
run_simulation()
