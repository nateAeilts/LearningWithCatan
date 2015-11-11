import cTurtle
from math import *
import random
##	I am trying to convert all of this to object oriented patterns, but I'm not sure where to start
##		with the resources.
##  CENTER = (0,0)
##  DICE = [1, 2, 3, 4, 5, 6]
DICE_VALUES = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
NUM_TILES_SIDE = 4 ##DO NOT CHANGE THIS... YET. Maybe someday...
PLAYER_COLORS = ["Red","Blue","Orange","Dark Green"]
PORTS = ["Trade-Wood", "Trade-Wheat", "Trade-Sheep", "Trade-Brick", "Trade-Ore", "Trade", "Trade", "Trade", "Trade"]
PROGRESS = ["RoadBuilding","YearOfPlenty","Monopoly","RoadBuilding","YearOfPlenty","Monopoly"]
RESOURCE_TILES = ["Wood", "Wood", "Wood", "Wood", "Wheat", "Wheat", "Wheat", "Wheat", "Sheep", "Sheep", "Sheep", "Sheep", "Brick", "Brick", "Brick", "Ore", "Ore", "Ore", "Desert"]
RESOURCE_TYPES = ["Wood", "Brick", "Sheep", "Wheat", "Ore"]
SIZE = 70 	##optimal size is ~70
			##I'm really not certain why I've made every function accept this as a parameter. Could just use it...
VERBOSE = True


def AisWithinDofB(p1,p2,distance):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < distance
    
def findMiddleAB(A,B):
    midX = round(((A[0] + B[0])/2), 2)
    midY = round(((A[1] + B[1])/2), 2)
    return (midX, midY)
   
    
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

###########################################################################################################
##  CENTER:
##      You might think this is a no brainer, but if I remember correctly, I included this variable
##      because almost all of the shapes drawn have a "center" parameter. So for them, the center
##      is different. I'm not sure where this actual "global" variable gets used, though... It might
##      have been simply for the sake of not having to type "(0,0)" here and there.
##		
##  Syntax:
##      A tuple for instructing cTurtle
##		
##  Files/Functions where used:
##           
###########################################################################################################

###########################################################################################################
##  DICE_VALUES:
##      A list of dice values and numbers of times they appear on a given board.
##		
##  Syntax:
##      Self Explanatory
##		
##  Files/Functions where used:
##        
###########################################################################################################

###########################################################################################################
##  NUM_TILES_SIDE:
##      This is an unused and unusable option as yet, a pipe dream that some day we'd be able to
##      create any size board we like, with any number of tiles (measured as tiles per side of the
##      larger hex of the whole board).
##		
##  Syntax:
##      N/A
##		
##  Files/Functions where used:
##           
###########################################################################################################

###########################################################################################################
##  PLAYER_COLORS:
##      You guessed right: this is a list of player colors. Be careful changing though--I'm not sure
##      they aren't checked against somewhere... Maybe...
##		
##  Syntax:
##      Self Explanatory
##		
##  Files/Functions where used:
##      
###########################################################################################################

###########################################################################################################
##  PORTS:
##      This list contains the number of tiles that are special "trade" tiles. Placing a settlement 
##      on a dock vertex on one of these tiles allows a player to trade 2 of a specific resource
##      card for one of a any other that is available in the bank. Plain "Water" tiles (no trading
##      bonus at all) are injected into this list in the [need to find] function in order to prepare
##		
##      for actually drawing the docks later.
##  Syntax:
##      "WaterWd" = Water Wood tile (2xWood card for 1xAny other)
##      "WaterWt" = Water Wheat trade tile
##      "WaterSp" = Water Sheep trade tile
##      "WaterBk" = Water Brick trade tile
##      "WaterOr" = Water Ore trade tile
##      "Trade"   = Standard trade tile (3xSame Resource card for 1xAny other)
##		
##  Files/Functions where used:
##      
###########################################################################################################

###########################################################################################################
##  PROGRESS:   !!!Need to figure out what happens with knight and vp cards
##      This is the list of the different kinds of Progress Cards, which are a subset of Development
##      cards (I think). There are only two of each, I think. The "Knight"/"Soldier" and "Victory Point"
##      cards added to this somewhere else.
##		
##  Syntax:
##      "RoadX2"   = "Road Builder" card (When played, player places two roads immediately)
##      "Plenty"   = "Year of Plenty" card (!!!Don't remember)
##      "Monopoly" = "Monopoly" card (!!!Don't remember)
##		
##  Files/Functions where used:
##           
###########################################################################################################

###########################################################################################################
##  RESOURCE_TILES:
##      This list contains the number of each kind of resource tile as it is found on the game board.
##      Specifically, there are 4x"Wood", 4x"Wheat", 4x"Sheep", 3x"Brick", 3x"Ore",
##      and only one "Desert" tile on any given board. This list gets "ripped" apart in building the
##      board, which is why the RESOURCE_TYPES list exists: I needed a list of possible RESOURCE_TYPES
##      against which to check for various parts of building the more complicated data structures.
##		
##  Syntax:
##      This one's pretty straight forward.
##		
##  Files/Functions where used:
##      
###########################################################################################################

###########################################################################################################
##  RESOURCE_TYPES:
##      This is a simple list of the actual types of RESOURCE_TYPES I use to check against for setting
##      things up later.
##		
##  Syntax:
##      Self explanatory
##		
##  Files/Functions where used:
##      
###########################################################################################################

###########################################################################################################
##  SIZE:
##      Yup. Most of the code drawing stuff accounts for variable sizes, but things start to look a
##      little funny if you get too far away from about 70
##		
##  Syntax:
##      It's a number. Of pixels. I think.
##		
##  Files/Functions where used:
##      Nearly everywhere
##		
###########################################################################################################

###########################################################################################################
##  TILE_REFS:
##      There are 36 tiles on any given board (including non-playable water/trade tiles. This is a list
##      of 36 six dual-alphabetical "names" that are used to set up the tile dictionary later on. The
##      "names" are listed backwards because the dictionary is created by popping the last element.
##		
##  Syntax:
##      Simply two letter combinations used to identify each tile individually.
##		
##  Files/Functions where used:
##           
###########################################################################################################

###########################################################################################################
##  VERBOSE:
##      A simple toggle for printing the data structures after board set up
##		
##  Syntax:
##		
##  Files/Functions where used:
##      SetupBoard
##           
###########################################################################################################