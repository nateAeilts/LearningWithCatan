from OOCatan_Resources import *

class Player():
    __PLAYER_ID = 1
    wood_size = SIZE*0.1
    brick_size = SIZE*0.27
    sheep_size = SIZE*0.2
    wheat_size = SIZE*0.1
    ore_size = SIZE*0.15
    def __init__(self, player_color="White"):
        self.name = "Player " + str(Player.__PLAYER_ID)
        Player.__PLAYER_ID += 1
        self.wood_position = (0,0)
        self.brick_position = (0,0)
        self.sheep_position = (0,0)
        self.wheat_position = (0,0)
        self.ore_position = (0,0)
        self.road_position = (0,0)
        self.settlement_position = (0,0)
        self.city_position = (0,0)
        self.corner = (0,0)
        self.cities = 4
        self.settlements = 5
        self.roads = 15
        self.color = player_color
        self.largest_army = False
        self.longest_road = False
        self.victory_points = 0
        self.owned_vertices = []
        self.owned_roads = []
        self.hand = {"Wood": 0, "Brick": 0, "Sheep": 0, "Wheat": 0, "Ore": 0}