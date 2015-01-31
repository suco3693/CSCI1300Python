"""
Assignment: Assignment 5

Sutton Cowperthwaite
Maryjane Clark

Description: Fox and Rabbit Simulation with files
Date: 9/26/13

"""




def main():
	In=open("initvals.txt","r")
	rBr=float(eval(In.readline()))
	fBr=float(eval(In.readline()))
	I=float(eval(In.readline()))
	S=float(eval(In.readline()))
	In.close()
	import math
	# rabbits is the current rabbit population
	R = int(input("\nPlease enter the initial rabbit population: "))
	# foxes is the current fox population 
	F = int(input("Please enter the initial foxes population: "))
	# num_days is the number of days to run the simulation
	Days = int(input("Please enter the number of days to run the simulation: "))
	# display_freq is how often to display results in the table, does not impact calculations
	#	display always starts with initial populations
	dFreq = int(input("Please enter the frequency of days for displaying data: "))
	#FileName input
	File=input("Please enter filename to store results: ")
	File=(File + ".csv")
	Output=File
	DaysList=[]
	for i in range(0, Days + 1):
		DaysList.append(i)
		
	Rraw=R
	Fraw=F
	FoxList=[F]
	RabList=[R]
	
	for i in range(1, Days + 1):
		dF=I*S*Rraw*Fraw-fBr*Fraw
		dR=rBr*Rraw-(I*Rraw*Fraw)
		Rraw=float(Rraw+dR)
		Fraw=float(Fraw+dF)
		RabList.append(Rraw)
		FoxList.append(Fraw)
		
# Ave
	RA = sum(RabList)/len(RabList)
	FA = sum(FoxList)/len(FoxList)
#Output	
	print()
	File=open(File,"w")
	print("Days, Rabbits, Foxes, Average Foxes, Average Rabbits",file=File)
	String="{},{},{},{},{}".format(0,R,F,FA,RA)
	
	print(String,file=File)
	for i in range(1, Days+1 ,dFreq):
		displayStr = DaysList[i],FoxList[i],RabList[i]
		displayStr="{},{},{}".format(DaysList[i],FoxList[i],RabList[i])	
		print(displayStr,file=File)	
	File.close()
	print("Simulation Finished -results data written to",File)
	

	
	

	

main()
