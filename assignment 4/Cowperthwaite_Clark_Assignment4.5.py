"""
Assignment: Assignment 4.5

Sutton Cowperthwaite
Maryjane Clark

Description: Fox and Rabbit Simulation
Date: 9/21/13

"""




def main():
	import math
	# rbr is the rabbit birth rate without predation 
	rBr = 0.01
	# fbr is the fox birth rate when no rabbits are available 
	fBr = 0.005
	# interaction is the likelihood that a rabbit and fox will meet
	I = 0.00001

	# hunt is the likelihood that when a fox & rabbit meet that the fox catches
	#   the rabbit
	S = 0.01
	# rabbits is the current rabbit population
	R = int(input("\nPlease enter the initial rabbit population: "))
	# foxes is the current fox population 
	F = int(input("Please enter the initial foxes population: "))
	# num_days is the number of days to run the simulation
	Days = int(input("Please enter the number of days to run the simulation: "))
	# display_freq is how often to display results in the table, does not impact calculations
	#	display always starts with initial populations
	dFreq = int(input("Please enter the frequency of days for displaying data: "))
	DaysList=[]
	for i in range(0, Days + 1):
		DaysList.append(i)
	
	Rabround=R
	Foxround=F
	Rabceil=R
	Foxceil=F
	Rabfloor=R
	Foxfloor=F
	Rraw=R
	Fraw=F
	RabrList=[R]
	FoxrList=[F]
	RabfList=[R]
	FoxfList=[F]
	RabcList=[R]
	FoxcList=[F]
	FoxList=[F]
	RabList=[R]
	for i in range(1, Days + 1):		
		dFr=round(I*S*Rabround*Foxround-(fBr*Foxround))
		dRr=round(rBr*Rabround-(I*Rabround*Foxround))
		Rabround=Rabround+dRr
		Foxround=Foxround+dFr
		RabrList.append(Rabround)
		FoxrList.append(Foxround)
		
		# compute the new number of rabbits and foxes for the day and take the ceiling of result
	for i in range(1, Days + 1):		
		dFc=I*S*Rabceil*Foxceil-fBr*Foxceil
		dRc=rBr*Rabceil-(I*Rabceil*Foxceil)
		Rabceil=math.ceil(Rabceil+dRc)
		Foxceil=math.ceil(Foxceil+dFc)
		RabcList.append(Rabceil)
		FoxcList.append(Foxceil)
		
		# compute the new number of rabbits and foxes for the day and take the floor of result
	for i in range(1, Days + 1):		
		dFf=I*S*Rabfloor*Foxfloor-fBr*Foxfloor
		dRf=rBr*Rabfloor-(I*Rabfloor*Foxfloor)
		Rabfloor=math.floor(Rabfloor+dRf)
		Foxfloor=math.floor(Foxfloor+dFf)
		RabfList.append(Rabfloor)
		FoxfList.append(Foxfloor)
		# compute the new number of rabbits and foxes for the day and leave as a fraction
	for i in range(1, Days + 1):
		dF=I*S*Rraw*Fraw-fBr*Fraw
		dR=rBr*Rraw-(I*Rraw*Fraw)
		Rraw=(Rraw+dR)
		Fraw=(Fraw+dF)
		RabList.append(Rraw)
		FoxList.append(Fraw)
		
		
		
		
#Round Ave
	rRA = sum(RabrList)/len(RabrList)
	rFA = sum(FoxrList)/len(FoxrList)
	

	print("\nRounded Population Averages:")

	print("{:9s}{:>10.3f}".format("Rabbits:", rRA))

	print("{:9s}{:>10.3f}".format("Foxes:", rFA))
#Floor Ave
	fRA = sum(RabfList)/len(RabfList)
	fFA = sum(FoxfList)/len(FoxfList)
	

	print("\nFloor Population Averages:")

	print("{:9s}{:>10.3f}".format("Rabbits:", fRA))

	print("{:9s}{:>10.3f}".format("Foxes:", fFA))
#Ceil Ave
	cRA = sum(RabcList)/len(RabcList)
	cFA = sum(FoxcList)/len(FoxcList)
	

	print("\nCeiling Population Averages:")

	print("{:9s}{:>10.3f}".format("Rabbits:", cRA))

	print("{:9s}{:>10.3f}".format("Foxes:", cFA))	
# Ave
	RA = sum(RabList)/len(RabList)
	FA = sum(FoxList)/len(FoxList)
	print("\nPopulation Averages:")
	print("{:9s}{:>10.3f}".format("Rabbits:", RA))
	print("{:9s}{:>10.3f}".format("Foxes:", FA))





	# print out Table Heading
	# Here is a version you can use as a guide. You don't have to keep it setup this way. 
	print()
	displayStr = "{:<10s}{:^20s}{:^19s}{:^20s}{:^29s}".format(

	"", "Rounded Values", "Floor Values", "Ceil Values", "Raw Values")
	print(displayStr)
	displayStr = "{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>15s}{:>15s}".format(

		"Day", "Rabbits", "Foxes", "Rabbits", "Foxes", "Rabbits", "Foxes", "Rabbits", "Foxes")
	print(displayStr)
	
	# create a for-loop to print out the values using the frequency that the user specified

	#	be sure to use string formatting to make everything line up nicely
	Day0=0
	print("-" * 100)
	RabList=['%.2f' % elem for elem in RabList]
	FoxList=['%.2f' % elem for elem in FoxList]
	print(displayStr)
	for i in range(0, Days + 1,dFreq):
		displayStr = "{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>15}{:>15}".format(
		DaysList[i], RabrList[i], FoxrList[i], RabfList[i], FoxfList[i], RabcList[i], FoxcList[i], RabList[i], FoxList[i])	
		print(displayStr)	
	
	
	

	
	print()

	

main()
