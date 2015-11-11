import cTurtle
from math import *
from OOCatan_Resources import *
from OOCatan_CatanTurtle import *
from OOCatan_Player import *
from OOCatan_Supplies import *
from OOCatan_Tile import *
from OOCatan_Vertex import *
from OOCatan_Road import *
import random

def DSDrawWood(catanTurtle, size):
    t = catanTurtle.turtle
    startP = t.position()
    startHdg = t.heading()
    
    t.goto(startP[0]-size//2, startP[1])
    catanTurtle.drawRectangle(top_bottom=size, left_right=size*2, border_color="Black", fill_color="Chocolate")
    t.goto(startP[0]-size*2, startP[1]-size*0.3)
    t.left(60)
    catanTurtle.drawRegularPolygon(num_sides=3, side_length=size*4, border_color="Black", fill_color="ForestGreen")
    t.setheading(startHdg)
    
def DSDrawBrick(catanTurtle, size):
    t = catanTurtle.turtle
    startP = t.position()
    startHdg = t.heading()
    
    catanTurtle.drawRectangle(top_bottom=size, left_right=size//2, border_color="Black", fill_color="#B8231E")
    
    t.goto(startP[0]-size,startP[1])
    catanTurtle.drawRectangle(top_bottom=size, left_right=size//2, border_color="Black", fill_color="#B8231E")
    
    t.goto(startP[0]-(size//2),startP[1]+(size//2))
    catanTurtle.drawRectangle(top_bottom=size, left_right=size//2, border_color="Black", fill_color="#B8231E")
    
    t.goto(startP[0]+(size//2),startP[1]+(size//2))
    catanTurtle.drawRectangle(top_bottom=size, left_right=size//2, border_color="Black", fill_color="#B8231E")
    
    t.goto(startP[0]-(size//2),startP[1]-(size//2))
    catanTurtle.drawRectangle(top_bottom=size, left_right=size//2, border_color="Black", fill_color="#B8231E")
    
    t.setheading(startHdg)
    
def DSDrawSheep(catanTurtle, size):
    t = catanTurtle.turtle
    startP = t.position()
    startHdg = t.heading()
    
    legWidth = size//2
    puffWidth = size*1.1
    
    catanTurtle.drawRectangle(top_bottom=legWidth//1.5, left_right=legWidth*3, border_color="Black", fill_color="Black")
    
    t.goto(startP[0]-legWidth*1.4, startP[1])
    catanTurtle.drawRectangle(top_bottom=legWidth//1.2, left_right=legWidth*3.5, border_color="Black", fill_color="Black")
    
    t.goto(startP[0]-legWidth*3.5, startP[1])
    catanTurtle.drawRectangle(top_bottom=legWidth//1.5, left_right=legWidth*3, border_color="Black", fill_color="Black")
    
    t.goto(startP[0]-legWidth*3.7-legWidth, startP[1])
    catanTurtle.drawRectangle(top_bottom=legWidth//1.2, left_right=legWidth*3.5, border_color="Black", fill_color="Black")
    
    t.goto(startP[0]-legWidth*3.5, startP[1]+legWidth)
    catanTurtle.drawCenteredCircle(radius=puffWidth, border_color="Black", fill_color="White")
    
    t.goto(startP[0]-legWidth*0.5, startP[1]+legWidth)
    catanTurtle.drawCenteredCircle(radius=puffWidth, border_color="Black", fill_color="White")
    
    t.goto(startP[0]+legWidth, startP[1]+legWidth*2)
    catanTurtle.drawCenteredCircle(radius=puffWidth//1.3, border_color="Black", fill_color="White")
    
    t.goto(startP[0]+legWidth*1.8, startP[1]+legWidth*1.2)
    t.dot(puffWidth, "Black")
    
    t.goto(startP[0]+legWidth, startP[1]+legWidth*2.8)
    t.dot(puffWidth//4, "Black")
    
    t.goto(startP[0]+legWidth*1.8, startP[1]+legWidth*2.8)
    t.dot(puffWidth//4, "Black")
    
    t.setheading(startHdg)
    
def DSDrawWheat(catanTurtle, size):
    t = catanTurtle.turtle
    startP = t.position()
    startHdg = t.heading()
    
    t.right(60)
    catanTurtle.drawRegularPolygon(num_sides=3, side_length=size*3.5, border_color="Black", fill_color="Gold")
    t.left(180)
    t.goto(startP[0], startP[1]-size*1.2)
    catanTurtle.drawRegularPolygon(num_sides=3, side_length=size*2.5, border_color="Black", fill_color="Gold")
    t.setheading(startHdg)
    t.goto(startP[0]-size*0.8, startP[1]-size*0.4)
    catanTurtle.drawRectangle(top_bottom=size*1.6, left_right=size*0.8, border_color="Black", fill_color="Brown")
    
    t.setheading(startHdg)
    
def DSDrawOre(catanTurtle, size):
    t = catanTurtle.turtle
    startP = t.position()
    startHdg = t.heading()
    
    t.goto(startP[0]-size, startP[1]+size)
    t.left(30)
    catanTurtle.drawRegularPolygon(num_sides=7, side_length=size*1.3, border_color="Black", fill_color="#4F5087")
    
    t.goto(startP[0]-size, startP[1]-size*0.4)
    t.right(90)
    catanTurtle.drawRegularPolygon(num_sides=7, side_length=size*0.7, border_color="Black", fill_color="#4F5087")
    
    t.goto(startP[0]-size*0.2, startP[1]-size*0.2)
    t.setheading(startHdg)
    catanTurtle.drawRegularPolygon(num_sides=7, side_length=size, border_color="Black", fill_color="#4F5087")
    
    t.setheading(startHdg)

def DSDrawPlainTrade(catanTurtle, size):
    t = catanTurtle.turtle
    startP = t.position()
    t.goto(startP[0], startP[1]-size*0.6)
    t.write("?", font=("Arial",50,"bold"), align="center")
    
def DSDrawResourceSymbol(catanTurtle, tileObj=None, resourceType=None, verbose=False):
    t = catanTurtle.turtle
    if not tileObj == None:
        if tileObj.kind == "LandTile": #I think some revision of "LandTile" vs "SeaTile" is in order. It's creating redundancy.
            if not tileObj.resource_type == "Desert":
                if tileObj.resource_type == "Wood":
                    t.goto(tileObj.resource_position)
                    DSDrawWood(catanTurtle, catanTurtle.side_length * tileObj.wood_land_scale)
                elif tileObj.resource_type == "Brick":
                    t.goto(tileObj.resource_position)
                    DSDrawBrick(catanTurtle, catanTurtle.side_length * tileObj.brick_land_scale)
                elif tileObj.resource_type == "Sheep":
                    t.goto(tileObj.resource_position)
                    DSDrawSheep(catanTurtle, catanTurtle.side_length * tileObj.sheep_land_scale)
                elif tileObj.resource_type == "Wheat":
                    t.goto(tileObj.resource_position)
                    DSDrawWheat(catanTurtle, catanTurtle.side_length * tileObj.wheat_land_scale)
                elif tileObj.resource_type == "Ore":
                    t.goto(tileObj.resource_position)
                    DSDrawOre(catanTurtle, catanTurtle.side_length * tileObj.ore_land_scale)
        else: #tileObj.kind == "SeaTile"
            tradeType = tileObj.trade_type.split('-')
            if tradeType[0] == "Trade":
                t.goto(tileObj.resource_position)
                if len(tradeType) == 2:
                    if tradeType[1] == "Wood":
                        t.goto(tileObj.resource_position)
                        DSDrawWood(catanTurtle, catanTurtle.side_length * tileObj.wood_sea_scale)
                    elif tradeType[1] == "Brick":
                        t.goto(tileObj.resource_position)
                        DSDrawBrick(catanTurtle, catanTurtle.side_length * tileObj.brick_sea_scale)
                    elif tradeType[1] == "Sheep":
                        t.goto(tileObj.resource_position)
                        DSDrawSheep(catanTurtle, catanTurtle.side_length * tileObj.sheep_sea_scale)
                    elif tradeType[1] == "Wheat":
                        t.goto(tileObj.resource_position)
                        DSDrawWheat(catanTurtle, catanTurtle.side_length * tileObj.wheat_sea_scale)
                    elif tradeType[1] == "Ore":
                        t.goto(tileObj.resource_position)
                        DSDrawOre(catanTurtle, catanTurtle.side_length * tileObj.ore_sea_scale)
                else:
                    DSDrawPlainTrade(catanTurtle, catanTurtle.side_length)
                    
    else: #tileObj == None
        pass #I don't remember what I had in mind for this.
    
def DSMoveRobber(boardObj, fromTileObj, targetTileObj, verbose=False):
    DSDrawTile(boardObj.catan_turtle, fromTileObj, verbose)
    fromTileObj.has_robber = False
    for v in fromTileObj.vertices:
        DSDrawVert(boardObj.catan_turtle, boardObj.vertex_map[v], verbose)
    boardObj.robber_tile = targetTileObj.name
    targetTileObj.has_robber = True
    DSPlaceRobber(boardObj)
    
def DSPlaceRobber(boardObj, targetTileName=None, verbose=False):
    catanTurtle = boardObj.catan_turtle
    t = catanTurtle.turtle
    if targetTileName == None:
        targetTile = boardObj.tile_map[boardObj.robber_tile]
        t.goto(targetTile.center)
        t.dot(boardObj.side_length, "Black")
    else:
        fromTile = boardObj.tile_map[boardObj.robber_tile]
        targetTile = boardObj.tile_map[targetTileName]
        DSMoveRobber(boardObj, fromTile, targetTile, verbose)
    
def DSDrawTile(catanTurtle, tileObj, verbose=False):
    t = catanTurtle.turtle
    t.goto(tileObj.center)
    catanTurtle.drawCenteredHex(fill_color=tileObj.background_color)
    catanTurtle.writeTileName(tileObj)
    DSDrawResourceSymbol(catanTurtle, tileObj, None, verbose)
    if tileObj.kind == "LandTile":
        catanTurtle.writeDiceNumber(tileObj)
    else:
        catanTurtle.writeTradeRatio(tileObj)

#################################################################################################################
def DSDrawHouse(catanTurtle, vertObj, verbose=False):
    pass
    
def DSDrawCity(catanTurtle, vertObj, verbose=False):
    pass

def DSDrawProperty(catanTurtle, vertObj, verbose=False):
    if vertObj.property_type == "Settlement":
        DSDrawHouse(catanTurtle, vertObj, verbose)
    else:# vertObj.property_type == "City":
        DSDrawCity(catanTurtle, vertObj, verbose)

def DSDrawDock(catanTurtle, vertObj, verbose=False):
    t = catanTurtle.turtle
    ctr = t.position()
    startHdg = t.heading()
    
    t.setheading(vertObj.dock_heading)
    t.backward(catanTurtle.dock_size//1.6)
    t.left(90)
    t.backward(catanTurtle.dock_size//2)
    catanTurtle.drawRectangle(catanTurtle.dock_size, catanTurtle.dock_size*2, "black", "brown")
    t.goto(ctr)
    t.setheading(startHdg)
    
    t.goto(vertObj.name_position)
    startColor = catanTurtle.togglePenDownAndColor("White")
    t.write(str(vertObj.name_string), font=("Arial",8,"bold"), align="center")
    if startColor:
        catanTurtle.togglePenDownAndColor(*startColor)
    else:
        catanTurtle.togglePenDownAndColor()
    
def DSDrawVert(catanTurtle, vertObj, verbose=False):
    t = catanTurtle.turtle
    t.goto(vertObj.location)
    t.dot(catanTurtle.vert_size, "darkblue")
    if not vertObj.port_type == "Not A Port":
        DSDrawDock(catanTurtle, vertObj, verbose)
    if not vertObj.player_on == "Empty":
        DSDrawProperty(catanTurtle, vertObj, verbose)  
    t.goto(vertObj.name_position)
    startColor = catanTurtle.togglePenDownAndColor("White")
    t.write(str(vertObj.name_string), font=("Arial",8,"bold"), align="center")
    if startColor:
        catanTurtle.togglePenDownAndColor(*startColor)
    else:
        catanTurtle.togglePenDownAndColor()
        
####################################################################################################################
def DSRefreshPlayerCorner(catanTurtle, playerObj, verbose=False):
    t = catanTurtle.turtle
    topLeft = t.position()
    startHdg = t.heading()
    startP = playerObj.corner
    sl = catanTurtle.side_length
    c2c = catanTurtle.center_to_center

    
    
    t.setheading(startHdg)


def DSDrawPlayerCorner(catanTurtle, playerObj, verbose=False):
    t = catanTurtle.turtle
    topLeft = t.position()
    startHdg = t.heading()
    startP = playerObj.corner
    sl = catanTurtle.side_length
    c2c = catanTurtle.center_to_center
    
    t.goto(startP[0] + sl*3.5, startP[1])
    t.dot(sl*2, playerObj.color)
    startColor = catanTurtle.togglePenDownAndColor("White")
    t.write(playerObj.name, font=("Arial",20,"bold"), align="center")
    if startColor:
        catanTurtle.togglePenDownAndColor(*startColor)
    else:
        catanTurtle.togglePenDownAndColor()

    t.goto(startP)
    catanTurtle.drawRectangle(sl*7, c2c*1.5 - 5, "Black", "White")

    t.goto(playerObj.wood_position)# startP[0]+sl*0.5, startP[1]-c2c*0.2)
    DSDrawWood(catanTurtle, playerObj.wood_size)# catanTurtle.side_length*0.1)

    t.goto(playerObj.brick_position)
    DSDrawBrick(catanTurtle, playerObj.brick_size)

    t.goto(playerObj.sheep_position)
    DSDrawSheep(catanTurtle, playerObj.sheep_size)

    t.goto(playerObj.wheat_position)
    DSDrawWheat(catanTurtle, playerObj.wheat_size)

    t.goto(playerObj.ore_position)
    DSDrawOre(catanTurtle, playerObj.ore_size)

    t.setheading(startHdg)
    DSRefreshPlayerCorner(catanTurtle, playerObj, verbose)
    

