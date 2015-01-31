from graphics import *
def graphic_filter(picture,filter1):
	"""
	Applies the user-selected graphic filter to the user-selected GIF image
	Params - pixels at points in window's width and heighth, RGB colors
	Return - the modified GIF image
	"""
	img=Image(Point(0,0),picture)
	w=img.getWidth()
	h=img.getHeight()
	pic=GraphWin(picture,w,h+2)
	img.move(w//2,h//2)
	img.draw(pic)
	if filter1 == "grey":
		"""
		Applies a greyscale filter to the GIF
		Params- pixel colors and points
		Return- modified image in grayscale
		"""
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
		"""
		Applies a black and white filter to the GIF
		Params- pixel colors and points
		Return- modified image in black and white
		"""
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
		"""
		Applies a red filter to the GIF
		Params- pixel colors and points
		Return- modified image in red filter
		"""
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				color=color_rgb(abs(red),abs(0),abs(0))	
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "green":
		"""
		Applies a green filter to the GIF
		Params- pixel colors and points
		Return- modified image in green filter
		"""	
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				color=color_rgb(abs(0),abs(green),abs(0))	
				img.setPixel(x,y,color)
		img.undraw() 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "blue":
		"""
		Applies a blue filter to the GIF
		Params- pixel colors and points
		Return- modified image in blue filter
		"""
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)
				color=color_rgb(abs(0),abs(0),abs(blue))	
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "posterize":
		"""
		Applies a posterized (painted looking) filter to the GIF
		Params- pixel colors and points
		Return- modified image in posterize
		"""
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
		"""
		Applies a negative (switched black and white) filter to the GIF
		Params- pixel colors and points
		Return- modified image in negative filter
		"""
		for x in range(w):
			for y in range(h):
				red,green,blue=img.getPixel(x,y)		
				color=color_rgb(abs(256-red),abs(256-green),abs(256-blue))	
				img.setPixel(x,y,color)
		img.undraw()	 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "Arty Fourths":
		"""
		Splits the GIF into four parts and applies colored
		filters to the GIF
		Params- pixel colors and points
		Return- modified image in filter
		"""
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
		"""
		Applies a switched color filter to the GIF, colors become
		their opposite
		Params- pixel colors and points
		Return- modified image in switched color filter
		"""
		for x in range(w):
			for y in range(0,h):
				red,green,blue=img.getPixel(x,y)					
				color=color_rgb(abs(green),abs(blue),abs(red))	
				img.setPixel(x,y,color)
		img.undraw() 
		img.draw(pic)		 
		return img,pic
	elif filter1 == "Vertical Mirror":
		"""
		Applies a vertical mirror filter to the GIF, image is split
		in half vertically and reflected across the y-axis
		Params- pixel colors and points
		Return- modified image in vertical mirror filter
		"""
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
