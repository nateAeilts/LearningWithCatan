from OOCatan_Resources import *

class Road():
    def __init__(self, road_name=None, road_location=None, player_on_road="Empty", road_color="White", road_heading=0):
        self.name = road_name
        self.location = road_location
        self.player_on = player_on_road
        self.color = road_color
        self.heading = road_heading
        self.neighbors = []
        
    def toString(self):
        s = '{:10}'.format(str(self.name)) + '{:20}'.format(str(self.location)) + '{:12}'.format(self.player_on) + '{:12}'.format(str(self.color)) + '{:6}'.format(str(self.heading))
        return s
        
    def withNeighborsString(self):
        s = '{:10}'.format(str(self.name))
        for n in self.neighbors:
            s += '{:10}'.format(n)
        return s