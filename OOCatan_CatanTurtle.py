import cTurtle
from math import *
from OOCatan_Resources import *
from OOCatan_DrawShapes import *
import random

class CatanTurtle():
    def __init__(self, turtle=None, turtle_side_length=SIZE, num_of_tiles_to_side=None):
        if turtle == None:
            self.turtle = cTurtle.Turtle()
        self.turtle.speed(200)
        self.turtle.up()
        self.turtle.tracer(False)
        self.side_length = turtle_side_length
        if num_of_tiles_to_side == None:
            self.num_of_tiles_to_side = 4
        self.turtle.setup(23*self.side_length,13*self.side_length,-10,-30)
        self.pen_is_down = False #cTurtle documentation says a turtle should already have a boolean like this, but I couldn't get it to work
        self.dock_size = self.side_length//4
        self.vert_size = self.side_length//3.7
        self.center_to_center = round((sqrt(3)*self.side_length), 2)
        
    def goTo(self, position):
        self.turtle.goto(position)
    
    def togglePenDownAndColor(self, border_color=None, fill_color=None):
        t = self.turtle
            
        if self.pen_is_down:
            t.up()
            self.pen_is_down = False
        else:
            t.down()
            self.pen_is_down = True
            
        if border_color is None and fill_color is None:                
            pass
        else:
            startColor = self.turtle.color()
            if fill_color is None:
                t.fill(False)
                t.color(border_color)
            else:
                t.fill(True)
                t.color(border_color, fill_color)
            return startColor
            
    def getPosition(self):
        t = self.turtle
        x = round(t.position()[0],2)
        y = round(t.position()[1],2)
        return (x,y)
        
    def drawRegularPolygon(self, num_sides=3, side_length=SIZE, border_color="black", fill_color=None):
        t = self.turtle
        startColor = self.togglePenDownAndColor(border_color, fill_color)
        ctr = t.position()
        hdg = t.heading()
        turnAngle = 360/num_sides
        
        for i in range(num_sides):
            t.forward(side_length)
            t.right(turnAngle)
            
        if startColor:    
            self.togglePenDownAndColor(*startColor)
        else:
            self.togglePenDownAndColor()
        t.goto(ctr)
        t.setheading(hdg)
        
    def drawRectangle(self, top_bottom=10, left_right=10, border_color="black", fill_color=None):
        t = self.turtle
        startColor = self.togglePenDownAndColor(border_color, fill_color) #There's probably a better way to avoid this assignment if unnecessary
        
        for i in range(2):
            t.forward(top_bottom)
            t.right(90)
            t.forward(left_right)
            t.right(90)

        if startColor:    
            self.togglePenDownAndColor(*startColor)
        else:
            self.togglePenDownAndColor()
            
    def drawCenteredRectangle(self, top_bottom=10, left_right=10, border_color="black", fill_color=None):
        t = self.turtle
        ctr = t.position()
        hdg = t.heading()
        
        t.left(90)
        t.forward(left_right//2)
        t.left(90)
        t.forward(top_bottom//2)
        t.setheading(hdg)
        self.drawRectangle(top_bottom, left_right, border_color, fill_color)
        t.goto(ctr)
    
    def eraser(self, top_bottom, left_right, border_color="white", fill_color="white"):
        t = self.turtle
        self.drawRectangle(top_bottom, left_right, border_color, fill_color)
        
    def centeredEraser(self, top_bottom, left_right, border_color="white", fill_color="white" ):
        t = self.turtle
        self.drawCenteredRectangle(top_bottom, left_right, border_color, fill_color)
    
    def drawHex(self, side_length=SIZE, border_color="black", fill_color=None):
        self.drawRegularPolygon(6, side_length, border_color, fill_color)
    
    def getHexVertices(self):
        returnVerts = []
        t = self.turtle
        ctr = t.position()
        hdg = t.heading()
        
        t.left(120)
        t.forward(self.side_length)
        t.right(120)
        
        for i in range(6):
            returnVerts.append(self.getPosition())
            t.forward(self.side_length)
            t.right(60)
            
        t.goto(ctr)
        t.setheading(hdg)
        
        return returnVerts
    
    def drawCenteredHex(self, side_length=SIZE, border_color="black", fill_color=None):
        t = self.turtle
        ctr = t.position()
        hdg = t.heading()
        
        t.left(120)
        t.forward(side_length)
        t.right(120)
        self.drawHex(side_length, border_color, fill_color)
        t.goto(ctr)
        t.setheading(hdg)
    
    def drawCenteredCircle(self, radius=SIZE//2, border_color="Black", fill_color=None):
        t = self.turtle
        ctr = t.position()
        hdg = t.heading()
        
        t.forward(radius)
        t.left(90)
        
        startColor = self.togglePenDownAndColor(border_color, fill_color)
        t.circle(radius=radius, steps=500)
        if startColor:
            self.togglePenDownAndColor(*startColor)
        else:
            self.togglePenDownAndColor()
        
        t.goto(ctr)
        t.setheading(hdg)
    
    #########################################################################################################################
    def writeTileName(self, tileObj, verbose=False):
        t = self.turtle
        t.goto(tileObj.name_position)
        if tileObj.kind == "LandTile" and tileObj.resource_type == "Desert":
            startColor = self.togglePenDownAndColor(border_color="White")
            t.write(tileObj.name, font=("Arial",12), align="center")
            if startColor:    
                self.togglePenDownAndColor(*startColor)
            else:
                self.togglePenDownAndColor()
        else:
            t.write(tileObj.name, font=("Arial",12), align="center")
    
    def writeDiceNumber(self, tileObj, verbose=False):
        if not tileObj.resource_type == "Desert":
            t = self.turtle
            t.goto(tileObj.dice_position)
            t.write(str(tileObj.dice_number), font=("Arial",25,"bold"), align="center")
        
    def writeTradeRatio(self, tileObj, verbose=False):
        if not tileObj.trade_type == "Water":
            t = self.turtle
            t.goto(tileObj.ratio_position)
            t.write(tileObj.trade_ratio_label, font=("Arial",12), align="center")
    
    def drawResource(self, tileObj, verbose=False):
        DSDrawResource(self, tileObj, verbose)
    
    def drawTile(self, tileObj, verbose=False):
        DSDrawTile(self, tileObj, verbose)
        
    def placeRobber(self, boardObj, targetTileName=None, verbose=False):
        DSPlaceRobber(boardObj, targetTileName, verbose)
        
    def drawVert(self, vertObj, verbose=False):
        DSDrawVert(self, vertObj, verbose)
    
    def drawPlayerCorner(self, playerObj, verbose=False):
        DSDrawPlayerCorner(self, playerObj, verbose)
        
    # def drawDock(self, vertObj, verbose=False):
        # DSDrawDock(self, vertObj, verbose)
    
    # def drawProperty(self, vertObj, verbose=False):
        # DSDrawProperty(self, vertObj, verbose)
        