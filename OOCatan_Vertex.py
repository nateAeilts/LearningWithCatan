from OOCatan_Resources import *

class Vertex():
    __VERT_ID = 0
    def __init__(self, vertex_name=None, vertex_location=None, vertex_name_position=None, player_on_vertex="Empty", vertex_is_playable=False, vertex_property_type="Empty", vertex_proptery_color="White", vertex_port_type="Not A Port", vertex_dock_heading=0, vertex_neighbors=[], vertex_surrounding_tiles=None):
        self.name = Vertex.__VERT_ID
        Vertex.__VERT_ID += 1
        if self.name < 10:
            self.name_string = "0" + str(self.name)
        else:
            self.name_string = str(self.name)
        self.location = vertex_location
        self.name_position = vertex_name_position
        self.player_on = player_on_vertex
        self.playable = vertex_is_playable
        self.property_type = vertex_property_type
        self.property_color = vertex_proptery_color
        self.port_type = vertex_port_type
        self.dock_heading = vertex_dock_heading
        self.neighbors = vertex_neighbors
        self.surrounding_tiles = vertex_surrounding_tiles
        
    def toString(self): #'{:5}' '{:20}' '{:12}' '{:10}' '{:11}' '{:6}'
        s = '{:5}'.format(self.name_string) + '{:20}'.format(str(self.location)) + '{:10}'.format(str(self.playable)) + '{:12}'.format(self.player_on) + '{:10}'.format(str(self.property_type)) + '{:12}'.format(str(self.property_color)) + '{:15}'.format(str(self.port_type))  + '{:6}'.format(str(self.dock_heading))
        return s
    
    def withNeighborsString(self):
        neighborsString = '{:<7}'.format(self.name_string)
        for i in range(len(self.neighbors)):
            neighborsString += '{:<5}'.format(self.neighbors[i])
        return neighborsString