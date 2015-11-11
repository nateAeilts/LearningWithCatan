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

def drawBoard(boardObj, verbose=False):
    catanTurtle = boardObj.catan_turtle
    t = catanTurtle.turtle
    
    for tileName in boardObj.tile_names:
        currentTile = boardObj.tile_map[tileName]
        catanTurtle.drawTile(currentTile, verbose)
        
    for v in boardObj.playable_vertices:
        currentV = boardObj.vertex_map[v]
        catanTurtle.drawVert(currentV, verbose)
        
    catanTurtle.placeRobber(boardObj)
    
    for p in boardObj.players:
        currentPlayer = boardObj.players[p]
        catanTurtle.drawPlayerCorner(currentPlayer, verbose)