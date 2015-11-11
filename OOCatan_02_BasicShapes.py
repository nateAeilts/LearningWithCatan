import cTurtle
from math import *
import random
#################################
#   Cntrl f (search) "!!!"      #
#   to find known problems/     #
#   needed changes              #
#################################


###########################################################################################################
##  drawRectangle:
##      -Draws a rectangle, in order the bottom left, bottom right, top right, top left
##      -Does not shade or color anything.
##      -It leaves the turtle where it started, but not with the same heading.
##		
##  Parameters:
##      turtle = Self explanatory
##      bottom_top = an integer, the length of the bottom and top sides
##      left_right = an integer, the length of the left and right sides
##		
##  Syntax:
##      N/A
##		
##  Functions Used:
##      -Established cTurtle directional commands
##		
##  Files/Functions where used:
##      A whole lot of places
##		
###########################################################################################################
def drawRectangle(turtle, bottom_top, left_right):
	for i in range(2):
		turtle.forward(bottom_top)
		turtle.left(90)
		turtle.forward(left_right)
		turtle.left(90)


###########################################################################################################
##  drawCenteredRectangle:
##      -Draws a rectangle centered where ever the turtle happens to be, oriented in the
##          direction the turtle is already facing.
##      -Again, begins in the bottom left corner, relative to where turtle began. (Sides in same order)
##      -Does not shade or color anything.
##      -It leaves the turtle in the same place it began, and with the same heading.
##      -Should use even numbers, because the length parameters get divided by two.
##		
##  Parameters:
##      turtle...
##      bottom_top = integer of side length, assumes the first & third sides drawn are the
##                  bottom & top, respectively
##      left_right = integer of side length, assumes the second & fourth sides drawn are right &
##                  left, respectively
##		
##  Syntax:
##      ctr = captures turtle's position before drawing rectangle
##      hdg = captures turtle's heading before drawing rectangle
##		
##  Functions Used:
##      -Established cTurtle directional commands
##      -drawRectangle
##		
##  Files/Functions where used:
##      
###########################################################################################################
def drawCenteredRectangle(turtle, bottom_top, left_right): 
	ctr = turtle.position()
	hdg = turtle.heading()
	turtle.up()
	turtle.right(90)
	turtle.forward(left_right//2)
	turtle.right(90)
	turtle.forward(bottom_top//2)
	turtle.setheading(hdg)
	turtle.down()
	drawRectangle(turtle, bottom_top, left_right)
	turtle.up()
	turtle.goto(ctr)


###########################################################################################################
##  eraser:
##      !!!Need to change this to draw a centered rectangle for sake of continuity with other shape-
##          drawing functions
##      -This function basically draws a white rectangle and fills it in with white.
##		
##  Parameters:
##      turtle...
##      bottom_top & left right = both the same as drawRectangle and drawCenteredRectangle
##		
##  Syntax:
##      N/A
##		
##  Functions Used:
##      -Established cTurtle directional commands
##      -drawRectangle      !!! Why oh why did I not just go with drawCenteredRectangle the first time?
##		
##  Files/Functions where used:
##      
###########################################################################################################
def eraser(turtle, bottom_top, left_right): 
	turtle.color("black","white")
	turtle.begin_fill()
	turtle.down()
	drawRectangle(turtle, bottom_top, left_right)
	turtle.up()
	turtle.end_fill()
	turtle.color("black")


###########################################################################################################
##  drawPolygon:
##      -The simplest way to draw regular polygons. 
##		
##  Parameters:
##      turtle...
##      numSides = integer, the number of sides the polygon will have (high numbers create ~circle)
##      sideLength = integer, controls the the size of the end shape
##		
##  Syntax:
##      turnAngle = the required angle to turn the turtle at every vertex to draw a complete polygon
##		
##  Functions Used:
##      -Established cTurtle directional commands
##		
##  Files/Functions where used:
##      
###########################################################################################################   
def drawPolygon(turtle,numSides,sideLength):
	turnAngle = 360/numSides
	for i in range(numSides):
		turtle.forward(sideLength)
		turtle.right(turnAngle)


###########################################################################################################
##  drawWood:
##      -Draws a tree, centered at the location desired by the user (NOT where the turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the tree figure to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      N/A
##		
##  Functions Used:
##      -Established cTurtle directional commands
##      -drawRectangle
##		
##  Files/Functions where used:
##      
###########################################################################################################        
def drawWood(turtle, center, size):   
	turtle.goto(center[0],center[1]-(0.6*size))
	turtle.color("black","chocolate")
	turtle.down()
	turtle.begin_fill()
	drawRectangle(turtle,(0.2*size),(0.7*size))
	turtle.end_fill()
	turtle.up()
	turtle.goto(center[0]-(0.3*size),center[1]-(0.2*size))
	turtle.color("black","ForestGreen")
	turtle.down()
	turtle.begin_fill()
	for i in range(3):
		turtle.forward(0.8*size)
		turtle.left(120)
	turtle.end_fill()
	turtle.up()


###########################################################################################################
##  drawWheat:
##      -Draws a wheat symbol, centered at the location desired by the user (NOT where the
##          turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the wheat figure to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      N/A
##		
##  Functions Used:
##      -Established cTurtle directional commands
##      -drawRectangle
##		
##  Files/Functions where used:
##      
###########################################################################################################
def drawWheat(turtle, center, size):
	center = (center[0]+(0.2*size),center[1]+(0.2*size)) #  !!! I think I was fixing something: just go with it
	turtle.up()
	turtle.goto(center)
	turtle.right(60)
	turtle.color("black","gold")
	turtle.down()
	turtle.begin_fill()
	for i in range(3):
		turtle.forward(0.8*size)
		turtle.right(120)
	turtle.end_fill()
	turtle.left(120)
	turtle.goto(center[0],center[1]-(0.2*size))
	turtle.begin_fill()
	for i in range(3):
		turtle.forward(0.5*size)
		turtle.left(120)
	turtle.end_fill()
	turtle.right(60)
	turtle.backward(0.15*size)
	turtle.color("black","brown")
	turtle.begin_fill()
	drawRectangle(turtle,0.3*size,0.15*size)
	turtle.end_fill()
	turtle.up()


###########################################################################################################
##  drawSheep:
##      -Draws a sheep symbol, centered at the location desired by the user (NOT where the
##          turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the sheep figure to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      N/A
##		
##  Functions Used:
##      -Established cTurtle directional commands
##      -drawRectangle
##		
##  Files/Functions where used:
##      
###########################################################################################################    
def drawSheep(turtle, center, size):
	turtle.color("black","black")
	#Drawing legs
	turtle.up()
	turtle.goto(center[0]-(0.1*size),center[1]-(0.5*size))
	turtle.down()
	turtle.begin_fill()
	drawRectangle(turtle, (0.1*size), (0.4*size))
	turtle.end_fill()
	turtle.up()
	turtle.goto(center[0]+(0.3*size),center[1]-(0.5*size))
	turtle.down()
	turtle.begin_fill()
	drawRectangle(turtle, (0.1*size), (0.4*size))
	turtle.end_fill()
	turtle.up()
	#Drawing body
	turtle.color("black","white")
	turtle.goto(center[0],center[1]-(0.3*size))
	turtle.begin_fill()
	turtle.down()
	turtle.circle(0.3*size)
	turtle.up()
	turtle.goto(center[0]+(0.3*size),center[1]-(0.3*size))
	turtle.down()
	turtle.circle(0.3*size)
	turtle.end_fill()
	turtle.up()
	#Drawing head
	turtle.goto(center[0]+(0.55*size),center[1]-(0.1*size))
	turtle.begin_fill()
	turtle.down()
	turtle.circle(0.2*size)
	turtle.up()
	turtle.end_fill()
	turtle.color("black","black")
	turtle.goto(center[0]+(0.7*size),center[1]-(0.05*size))
	turtle.begin_fill()
	turtle.down()
	turtle.circle(0.1*size)
	turtle.up()
	turtle.end_fill()


###########################################################################################################
##  drawBricks:
##      -Draws a brick symbol, centered at the location desired by the user (NOT where the
##          turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the brick figure to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      newStart = I'm not sure, really. Probably fixed something temporarily, then got left in... works though
##		
##  Functions Used:
##      -Established cTurtle directional commands
##      -drawRectangle
##		
##  Files/Functions where used:
##      
###########################################################################################################
def drawBricks(turtle, center, size):
	newStart = (center[0]+(0.2*size),center[1]) ## !!!  Again, this idealy wouldn't be here, but tweaked
	turtle.up()                                 ##      something somewhere on the fly. Just leave it for now
	turtle.goto(newStart)
	turtle.color("black","#B8231E")
	turtle.begin_fill()
	turtle.down()
	drawRectangle(turtle,(0.4*size),(0.2*size))
	drawRectangle(turtle,(-0.4*size),(0.2*size))
	turtle.backward(0.2*size)
	drawRectangle(turtle,(0.4*size),(-0.2*size))
	drawRectangle(turtle,(-0.4*size),(-0.2*size))
	turtle.up()
	turtle.end_fill()
	turtle.goto(newStart[0],newStart[1]-(0.2*size))
	turtle.begin_fill()
	turtle.down()
	drawRectangle(turtle,(-0.4*size),(-0.2*size))
	turtle.up()
	turtle.end_fill()


###########################################################################################################
##  drawOre:
##      -Draws a ore symbol, centered at the location desired by the user (NOT where the
##          turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the ore figure to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      N/A
##		
##  Functions Used:
##      -Established cTurtle directional commands
##      -drawPolygon
##		
##  Files/Functions where used:
##      
###########################################################################################################
def drawOre(turtle, center, size):
	turtle.color("black","dark gray")
	turtle.goto(center[0]+(0.2*size),center[1]+(0.3*size))
	turtle.down()
	turtle.begin_fill()
	drawPolygon(turtle, 8, (0.2*size))
	turtle.end_fill()
	turtle.up()
	turtle.goto(center[0]-(0.1*size),center[1]+(0.15*size))
	turtle.down()
	turtle.begin_fill()
	drawPolygon(turtle, 8, (0.2*size))
	turtle.end_fill()
	turtle.up()
	turtle.goto(center[0]+(0.3*size),center[1])
	turtle.down()
	turtle.begin_fill()
	drawPolygon(turtle, 8, (0.2*size))
	turtle.end_fill()
	turtle.up()


###########################################################################################################
##  drawBaseHex:
##      -Draws a normal hexagon, centered at the location desired by the user (NOT where the
##          turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the hex to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      norm = !!! captures pensize before changing it, to enable changing back, but I don't know why this
##                  was necessary
##		
##  Functions Used:
##      -Established cTurtle directional commands
##		
##  Files/Functions where used:
##      
###########################################################################################################
def drawBaseHex(turtle, center, size):
	norm = turtle.pensize() ##  !!! I have not idea why I messed with the pensize at all...
	turtle.up()
	turtle.setheading(0)
	turtle.goto(center[0]+size,center[1])
	turtle.down()
	turtle.right(120)
	turtle.pensize(2)
	for i in range(6):
		turtle.forward(size)
		turtle.right(60)
	turtle.up()
	turtle.pensize(norm)
	turtle.goto(center)
	turtle.setheading(0)
	
	
###########################################################################################################
##  drawSettlement:
##      -Draws settlement "piece" centered where the user desires (NOT where the
##          turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the settlement figure to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      squareLen = integer, captures the length of the "square" part of a settlement piece
##		
##  Functions Used:
##      -Established cTurtle directional commands
##		
##  Files/Functions where used:
##      
###########################################################################################################
def drawSettlement(turtle, center, size):
	turtle.up()
	turtle.goto(center[0]-(size*0.15),center[1])
	turtle.setheading(0)
	turtle.down()
	turtle.right(90)
	turtle.begin_fill()
	squareLen = size*0.3
	for i in range (3):
		turtle.forward(squareLen)
		turtle.left(90)
	turtle.right(45)
	turtle.forward((squareLen*(sqrt(2)))/2)
	turtle.left(90)
	turtle.forward((squareLen*(sqrt(2)))/2)
	turtle.end_fill()
	turtle.up()
	turtle.goto(center)
	turtle.setheading(0)


###########################################################################################################
##  drawCity:
##      -Draws city "piece" centered where the user desires (NOT where the
##          turtle already rests)
##		
##  Parameters:
##      turtle...
##      center = tuple of integers, where the user wants the city figure to be centered
##      size = integer, the size used in building the board, given here to allow for scaling. Will
##              probably always be 70
##		
##  Syntax:
##      roofCorner = coordinate tuple, captures a reference point for later use
##      squareLen = integer, allows easy drawing of the "base" of the piece
##		
##  Functions Used:
##      -Established cTurtle directional commands
##		
##  Files/Functions where used:
##      
###########################################################################################################
def drawCity(turtle, center, size):
	turtle.up()
	turtle.goto(center[0]-(size*0.25),center[1])
	roofCorner = turtle.position()
	turtle.setheading(270)
	turtle.down()
	turtle.begin_fill()
	squareLen = size*0.3
	turtle.forward(squareLen)
	turtle.left(90)
	turtle.forward(squareLen+(size*0.1))
	turtle.left(90)
	turtle.forward(squareLen)
	turtle.left(45)
	turtle.forward((squareLen*(sqrt(2)))/2)
	turtle.left(90)
	turtle.forward((squareLen*(sqrt(2)))/2)
	turtle.setheading(180)
	turtle.goto(roofCorner)
	turtle.end_fill()
	turtle.up()
	turtle.goto(center)
	turtle.setheading(0)
