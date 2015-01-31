"""
Assignment: Assignment 8

Sutton Cowperthwaite
Maryjane Clark

Description: GIF Filters
Date: 10/22/13

"""
from graphics import *
def display_gif(picture):
	"""
	Produces the main photo from the selection and shows it to the user
	"""
	border=20
	#get image
	img=Image(Point(0,0),picture)
	#get image height and width
	w=img.getWidth()
	h=img.getHeight()
	#display gif
	pic=GraphWin(picture,w+2*border,h+2*border)
	#move image anchor to center
	img.move(w//2+border,h//2+border)
	#put image on window
	img.draw(pic)
	return img,pic
"""	
	
def graphic_filter(picture,filter1):
	"""
	Adds Filters to the selected picture then imports it back to the main file
	"""
	border=20
	img=Image(Point(0,0),picture)
	w=img.getWidth()
	h=img.getHeight()
	pic=GraphWin(picture,w+2*border,h+2*border)
	img.move(w//2,h//2)
	img.draw(pic)
	if filter1 == "grey":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				red=green=blue=.22126*red+(.7152*green)+(.0722*blue)
				color=color_rgb(abs(red),abs(green),abs(blue))	
				img.setPixel(x,y,color)			 
		img.undraw()	
		img.draw(pic)			 
		return img,pic
	elif filter1 == "b/w":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				avgcolor=(red+green+blue)/3
				if avgcolor > 130:
					color=color_rgb(255,255,255)	
				else:
					color=color_rgb(0,0,0)
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "red":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				color=color_rgb(abs(red),abs(0),abs(0))	
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "green":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				color=color_rgb(abs(0),abs(green),abs(0))	
				img.setPixel(x,y,color)
		img.undraw() 
		img.draw(pic)		 
		return img.pic
	elif filter1 == "blue":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				color=color_rgb(abs(0),abs(0),abs(blue))	
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "posterize":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				if red < 51:
					red=25
				elif red <102:
					red= 76
				elif red < 153:
					red=127
				elif red < 204:
					red=170
				else:
					red=230	
				if green < 51:
					 green=25
				elif green <102:
					green= 76
				elif green < 153:
					green=127
				elif green < 204:
					green=170
				else:
					green=230
				if blue < 51:
					blue=25
				elif blue <102:
					blue= 76
				elif blue < 153:
					blue=127
				elif blue < 204:
					blue=170
				else:
					blue=230							
				color=color_rgb(abs(red),abs(green),abs(blue))	
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "negative":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)		
				color=color_rgb(abs(255-red),abs(255-green),abs(255-blue))	
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "Arty Fourths":
		w1=int(w/2)
		h1=int(h/2)
		for x in range(0,w1):
			for y in range(0,h1):
				red,green,blue=img.getPixel(x,y)
				avgcolor=(red+green+blue)/3
				if avgcolor > 130:
					color=color_rgb(255,255,0)	
				else:
					color=color_rgb(0,0,255)
				img.setPixel(x,y,color)
		for x in range(w1,w):
			for y in range(h1,h):
				red,green,blue=img.getPixel(x,y)
				avgcolor=(red+green+blue)/3
				if avgcolor > 130:
					color=color_rgb(0,0,255)	
				else:
					color=color_rgb(255,255,0)
				img.setPixel(x,y,color)
		for x in range(0,w1):
			for y in range(h1,h):
				red,green,blue=img.getPixel(x,y)
				avgcolor=(red+green+blue)/3
				if avgcolor > 130:
					color=color_rgb(255,0,0)	
				else:
					color=color_rgb(0,255,0)
				img.setPixel(x,y,color)					
		for x in range(w1,w):
			for y in range(0,h1):
				red,green,blue=img.getPixel(x,y)
				avgcolor=(red+green+blue)/3
				if avgcolor > 130:
					color=color_rgb(0,255,0)	
				else:
					color=color_rgb(255,0,0)
				img.setPixel(x,y,color)	
		img.undraw() 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "Switch Color":
		for x in range(w):
			for y in range(0,h):
				red,green,blue=img.getPixel(x,y)					
				color=color_rgb(abs(green),abs(blue),abs(red))	
				img.setPixel(x,y,color)
		img.undraw() 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "Vertical Mirror":
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				color=color_rgb(abs(red),abs(green),abs(blue))	
				img.setPixel(w-x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	else:
		exit()			
"""
	
def graphics_main():
	"""
	Allows user to choice a photo,then exports the choice to other function which displays it.
	Then asks user if that is the photo they want then asks for filters.
	
	
	"""
	userA=input("\nWould you like to play with filters and gifs? (y/n):")
	userA=userA[:1].lower()
	if userA == "y":
		x=7
	elif userA != "n":
		print("You pressed a wrong key, but we will assume you wanted to play") 
		userA= "y"
	while userA =="y":	
		userB="y"
		while userB == "y":
			print("Welcome to the GIF image Filter Program!")
			print("")
			print("GIF in Directory:")	
			print("1 hibiscus.gif")
			print("2 Pangolins.gif")
			print("3 Quit")
			while True:	
				Num=input("\nPlease choice a Selection Number from the List:") 		
				#Get the orginal Picture
				if Num =="1":
					picture="hibiscus.gif"
					img1,pic1 = display_gif(picture)
					break
				elif Num == "2":
					picture="pangolins.gif"
					img1,pic1=display_gif(picture)
					break
				elif Num== "3":
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
					userB="n"
			else:
				userB="y"
				pic1.close()
						
		#Filters
		userC=input("\nWould you like to play with filters? (y/n):")
		userC=userC[:1].lower()
		if userA == "y":
			x=7
		elif userC != "n":
			print("You pressed a wrong key, but we will assume you wanted to play") 
			userC= "y"
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
				choice=input("Please enter the number of your Filter: ")
				if choice=="1":
					filter1="grey"
					img2,pic2 =Cowperthwaite_Clarkgraphic_filter(picture,filter1)
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

