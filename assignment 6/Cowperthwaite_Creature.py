"""
Assignment 6
Sutton Cowperthwaite
Sutton Cowperthwaite's Creature

My creature's name is Steve. He has frog like eyes becuase I wanted
to see if I could figure out how to get the oval and circle shapes to match
up for it. He has wing like things becuase I wanted to see what it was like to
run a for loop with rectangles and that is what came out and I wanted to try to mae
wings. he is just a head without a body becuase I though it would look cooler.

"""
from graphics import *

def main():
	win=GraphWin("Creature",400,400)
	for i in range(0,20):
		bar=Rectangle(Point(400-i,200-i),Point(200-i,250))
		bar.draw(win)
	for j in range(0,20):
		bar2=Rectangle(Point(200-j,200-j),Point(j,250))
		bar2.draw(win)
	leg1=Rectangle(Point(230,200),Point(260,400))
	leg1.setFill("purple4")
	leg1.draw(win)
	leg2=leg1.clone()
	leg2.move(-85,0)
	leg2.draw(win)	
	arm1=Rectangle(Point(50,200),Point(200,230))
	arm1.setFill("purple4")
	arm2=arm1.clone()
	arm2.move(150,0)
	arm2.draw(win)
	arm1.draw(win)
	halo=Oval(Point(170,70),Point(240,120))
	halo.setFill("yellow3")
	halo.draw(win)
	halo1=Oval(Point(185,80),Point(220,105))
	halo1.setFill("grey")
	halo1.draw(win)
	body=Circle(Point(200,200),70)
	body.setFill("red")
	body.draw(win)
	eye1=Circle(Point(150,150),20)
	eye1.setFill("green")
	eye1.draw(win)
	eye2=eye1.clone()
	eye2.move(100,0)
	eye2.draw(win)
	inner1=Oval(Point(130,140),Point(170,160))
	inner1.setFill("black")
	inner2=inner1.clone()
	inner2.move(100,0)
	inner2.draw(win)
	inner1.draw(win)
	mouth=Polygon(Point(150,200),Point(160,210),Point(160,220),Point(240,220),Point(240,210),Point(250,200),Point(250,240),Point(150,240))
	mouth.setFill("cyan2")
	mouth.draw(win)
	t=Polygon(Point(190,230),Point(195,260),Point(205,260),Point(210,230))
	t.setFill("pink3")
	t.draw(win)
	nose=Polygon(Point(200,190),Point(220,200),Point(180,200))
	nose.setFill("white")
	nose.draw(win)
	win.getMouse()
	win.close()
main()		




