from math import *
from OOCatan_Resources import *
from OOCatan_DataBuilders import *
from OOCatan_DrawBoard import *
import random

class BoardObj():
    def __init__(self, board_number_of_players=4):
        self.number_of_players = board_number_of_players
        self.tile_names = []
        self.tile_map = {}
        self.robber_tile = "0-0" #This changes to a random tile when the board is set up
        self.vertex_list = []
        self.playable_vertices = []
        self.vertex_map = {}
        self.road_list = []
        self.road_map = {}
        self.dice = (1,1)
        self.players = {}
        self.resource_cards = {}
        self.development_cards = {}
        self.side_length = SIZE
        self.center_to_center = round((sqrt(3)*self.side_length), 2)
    
    def setBoard(self):
        buildData(self, verbose=True)
        drawBoard(self, verbose=True)
        
    def moveRobberHelper(self, targetTileName=None, verbose=False):
        self.catan_turtle.placeRobber(self, targetTileName, verbose)
        
    def moveRobber(self, targetTileName=None, verbose=False):
        self.moveRobberHelper(targetTileName, verbose)
    
    def printTiles(self):
        print('{:^58}'.format("Land Tiles" + "\n"))
        print('{:5}'.format("name") + '{:20}'.format("center") + '{:13}'.format("dice_number") + '{:10}'.format("res_type") + str("has_robber"))
        for i in range(self.number_of_playable_tiles):
            print(self.tile_map[self.tile_names[i]].toString())
        print("\n\n" + '{:^58}'.format("Sea Tiles" + "\n"))
        print('{:5}'.format("name") + '{:20}'.format("center") + '{:13}'.format("trade_type") + '{:10}'.format("ratio") + str("ratio_label"))
        for i in range(self.number_of_playable_tiles, self.number_of_tiles_on_board):
            print(self.tile_map[self.tile_names[i]].toString())
        print()
            
    def printTilesWithVertexNames(self):
        for i in range(self.number_of_tiles_on_board):
            print(self.tile_map[self.tile_names[i]].vertNamesString())
        print()
            
    def printTilesWithVertexLocations(self):
        for i in range(self.number_of_tiles_on_board):
            print(self.tile_map[self.tile_names[i]].vertLocsString())
        print()
    
    def printTilesWithRoads(self):
        for i in range(self.number_of_playable_tiles):
            currentTile = self.tile_map[self.tile_names[i]]
            print(currentTile.withRoadsString())
        print()
    
    def printTilesWithNeighbors(self):
        for i in range(self.number_of_tiles_on_board):
            print(self.tile_map[self.tile_names[i]].withNeighborsString())
        print()
            
    def printVertices(self):#'{:5}' '{:20}' '{:12}' '{:10}' '{:11}' '{:6}'
        s = '{:5}'.format("name") + '{:20}'.format("location") + '{:10}'.format("playable") + '{:12}'.format("player_on") + '{:10}'.format(str("prop type")) + '{:12}'.format(str("prop color")) + '{:15}'.format(str("port_type")) + '{:6}'.format("dock_heading")
        # titleString = 
        print(s)
        for i in range(len(self.playable_vertices)):
            print(self.vertex_map[self.playable_vertices[i]].toString())
            if i % 3 == 2:
                print("----------------------------------------------------------------------------------------------------------")
        print()
            
    def printVerticesWithNeighbors(self):
        for i in range(len(self.vertex_list)):
            print(self.vertex_map[i].withNeighborsString())
        print()
        
    def printRoads(self):
        for r in self.road_list:
            print(self.road_map[r].toString())
            
    def printRoadsWithNeighbors(self):
        for i in range(len(self.road_list)):
            print(self.road_map[self.road_list[i]].withNeighborsString())
            if i % 3 == 2:
                print("-----------------------------------------------------")
    #def testHexes(self):
        
    