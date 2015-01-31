"""
Assignment: Assignment 8

Sutton Cowperthwaite
Maryjane Clark

Description: GIF Filters
Date: 10/22/13

"""
from graphics import *
from graphics_filters import *
def display_gif(picture):
	"""
	Displays the user-selected GIF image centered in a window
	Params - picture selected and points in window
	Return - user selected GIF image
	"""
	#get image
	img=Image(Point(0,0),picture)
	#get image height and width
	w=img.getWidth()
	h=img.getHeight()
	#display gif
	pic=GraphWin(picture,w,h)
	#move image anchor to center
	img.move(w//2,h//2)
	#put image on window
	img.draw(pic)
	return img,pic
	
def graphics_main():
	"""
	Evaluates user input to select GIF image, filter type,
	and allows user to save the final product. Handles user errors.
	Params- filenames, picture, string literals
	Return- GIF image, filtered GIF image, saved file
	"""
	userA=input("\nWould you like to play with filters and gifs? (y/n):")
	userA=userA[:1].lower()
	if userA == "y":
		x=7 
	elif userA != "n":
		print("You pressed a wrong key, but we will assume you wanted to play. (You can quit at any time.)") 
		userA= "y"	
	while userA =="y":	
		userB="y"
		while userB == "y":
			print()
			print("Welcome to the GIF image Filter Program!")
			print()
			print("GIF in Directory:")	
			print("1 hibiscus.gif")
			print("2 Pangolins.gif")
			print("3 babyelephant.gif")
			print("4 turtle.gif")
			print("5 redrocks.gif")
			print("6 grumpycat.gif")
			print("7 justiceleague.gif")
			print("8 Quit")
			while True:	
				Num=input("\nPlease choose a Selection Number from the List:") 		
				#Get the orginal Picture
				if Num =="1":
					picture="hibiscus.gif"
					img1,pic1 = display_gif(picture)
					break
				elif Num == "2":
					picture="pangolins.gif"
					img1,pic1=display_gif(picture)
					break
				elif Num == "3":
					picture="babyelephant.gif"
					img1,pic1=display_gif(picture)
					break
				elif Num == "4":
					picture="turtle.gif"
					img1,pic1=display_gif(picture)
					break	
				elif Num == "5":
					picture= "redrocks.gif"
					img1,pic1=display_gif(picture)
					break
				elif Num == "6":
					picture= "grumpycat.gif"
					img1,pic1=display_gif(picture)
					break
				elif Num == "7":
					picture= "justiceleague.gif"	
					img1,pic1=display_gif(picture)
					break
				elif Num == "8":
					print("Goodbye")
					exit()
				else:
					print("Answer Invalid")		
			userB=input("Is this the picture you want? (y/n):")
			userB=userB[:1].lower()
			
			if userB == "y":
				x=7
			elif userB != "n":
				print("You pressed a wrong key, but we will assume this is the picture you want")
				userB= "y"
			if userB=="y":
				userB = "n"
			else:
				userB="y"
				pic1.close()
					
						
		#Filters
		userC=input("\nWould you like to play with filters? (y/n):")
		userC=userC[:1].lower()
		if userA == "y":
			x=7
		elif userC != "n":
			print("Answer Invalid") 
			break
		while userC == "y":	
			print("\n Image Filter Options:")
			print("1: Grayscale")
			print("2: Black and White")
			print("3: Red Tone")
			print("4: Green Tone")
			print("5: Blue Tone")
			print("6: Posterize")
			print("7: Negative")
			print("8: Arty Fourths")
			print("9: Switch Color")
			print("10: Vertical Mirror")
			print("11:Cancel")
			while True:
				print()
				choice=input("Please enter the number of your Filter: ")
				if choice=="1":
					filter1="grey"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="2":	
					filter1="b/w"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="3":
					filter1="red"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="4":
					filter1="green"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="5":	
					filter1="blue"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="6":	
					filter1="posterize"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="7":
					filter1="negative"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="8":	
					filter1="Arty Fourths"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="9":
					filter1="Switch Color"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="10":
					filter1="Vertical Mirror"
					img2,pic2 =graphic_filter(picture,filter1)
					break
				elif choice=="11":	
					print("Goodbye")
					exit()
				else:
					print("Filter Choice is not in Range")
						
			userC=input("Is this the filter you want? (y/n):")
			userC=userC[:1].lower()
			if userC=="y":
				userC="n"
			else:
				userC="y"
				pic2.close()
		print()	
		#save file under user-selected filename	
		save=input("Would you like to Save your File? (y/n) ")
		if save == "y":
			x=7
		elif save != "n":
			print("You pressed a wrong key, but we will assume you wanted to save") 
			userA= "y"
		if save =="y":
			File=input("Enter a file name: ")
			File= File+".gif"
			print(File)
			img2.save(File)	
		
		userstay=input("Are you done? (y/n): ")
		userstay=userstay[:1].lower()
		print(userstay)
		if userstay=="y":
			userA="n"
			
		else:
			userA="y"
			pic1.close()
			pic2.close()
			
				


graphics_main() 
