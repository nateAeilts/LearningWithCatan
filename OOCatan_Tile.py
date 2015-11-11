from OOCatan_Resources import *

class Tile(): #I'm not sure I'm doing inheretence right...
    def __init__(self, tile_name=None, tile_name_position=None, tile_center=None, tile_resource_position=None, tile_vertices={}, tile_neighbors=[], tile_background_color="white", tile_roads=[]):
        self.name = tile_name
        self.name_position = tile_name_position
        self.center = tile_center
        self.resource_position = tile_resource_position
        self.vertices = tile_vertices
        self.neighbors = tile_neighbors
        self.background_color = tile_background_color
        self.roads = tile_roads
        
    def withNeighborsString(self):
        neighborsString = '{:8}'.format(self.name)
        for i in range(len(self.neighbors)):
            neighborsString += '{:8}'.format(self.neighbors[i])
        return neighborsString
    
    def vertNamesString(self):
        namesString = '{:8}'.format(self.name)
        for v in self.vertices:
            namesString += '{:6}'.format(str(v))
        return namesString        
        
class LandTile(Tile):
    wood_x_trans = 0.3
    wood_y_trans = -0.1
    wood_land_scale = 0.2
    
    brick_x_trans = 0.3
    brick_y_trans = 0.2
    brick_land_scale = 0.4
    
    sheep_x_trans = 0.0
    sheep_y_trans = 0.0
    sheep_land_scale = 0.27
    
    wheat_x_trans = 0.2
    wheat_y_trans = 0.25
    wheat_land_scale = 0.2
    
    ore_x_trans = 0.2
    ore_y_trans = 0.1
    ore_land_scale = 0.2
    
    dice_number_x_trans = 0.4
    dice_number_y_trans = 0.7
    
    def __init__(self, tile_dice_num=None, tile_dice_position=None, tile_resource_type=None, tile_has_robber=False):
        self.kind = "LandTile"
        self.dice_number = tile_dice_num
        self.dice_position = tile_dice_position
        self.resource_type = tile_resource_type
        self.resource_position = None
        self.has_robber = tile_has_robber
    
    def toString(self):
        s = '{:5}'.format(self.name) + '{:20}'.format(str(self.center)) + '{:13}'.format(str(self.dice_number)) + '{:10}'.format(str(self.resource_type)) + str(self.has_robber)
        return s
        
    def withRoadsString(self):
        s = '{:5}'.format(self.name)
        for r in self.roads:
            s += '{:10}'.format(r)
        return s
        
class SeaTile(Tile):
    ratio_y_trans = 1.0
    
    wood_x_trans = 0
    wood_y_trans = -0.1
    wood_sea_scale = 0.2
    
    brick_x_trans = -0.1
    brick_y_trans = 0.05
    brick_sea_scale = 0.4
    
    sheep_x_trans = 0.2
    sheep_y_trans = 0
    sheep_sea_scale = 0.27
    
    wheat_x_trans = 0
    wheat_y_trans = 0.2
    wheat_sea_scale = 0.2
    
    ore_x_trans = 0
    ore_y_trans = 0.1
    ore_sea_scale = 0.2
    
    def __init__(self, tile_trade_type=None, tile_trade_ratio=None, tile_trade_ratio_label=None, tile_ratio_position=None):
        self.kind = "SeaTile"
        self.trade_type = tile_trade_type
        self.resource_position = None
        self.trade_ratio = tile_trade_ratio
        self.trade_ratio_label = tile_trade_ratio_label
        self.ratio_position = tile_ratio_position
        
    def toString(self):
        s = '{:5}'.format(self.name) + '{:20}'.format(str(self.center)) + '{:13}'.format(str(self.trade_type)) + '{:10}'.format(str(self.trade_ratio)) + '{:5}'.format(str(self.trade_ratio_label))
        return s