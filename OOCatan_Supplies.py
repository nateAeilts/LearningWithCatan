from OOCatan_Resources import *

class Supplies():
    def __init__(self):
        self.wood = 19
        self.brick = 19
        self.sheep = 19
        self.wheat = 19
        self.ore = 19
        
        #RESOURCE_TYPES = ["Wood", "Brick", "Sheep", "Wheat", "Ore"]
        self.resource_cards = {}
        self.resource_cards["Wood"] = self.wood
        self.resource_cards["Brick"] = self.brick
        self.resource_cards["Sheep"] = self.sheep
        self.resource_cards["Wheat"] = self.wheat
        self.resource_cards["Ore"] = self.ore
        
        development = []
        soldiers = []
        for i in range(14):
            soldiers.append("Soldier")
        progress = PROGRESS
        victoryPoints = []
        for i in range(5):
            victoryPoints.append("VictoryPoint")
        development.append(soldiers)
        development.append(progress)
        development.append(victoryPoints)
        random.shuffle(development)
        self.development_cards = development
        
        self.longest_road = "Empty"
        self.largest_army = "Empty"
        
        self.dice1 = 1
        self.dice2 = 1
        
        self.base_corner = (0,0)