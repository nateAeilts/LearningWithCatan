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

def printIfVerbose(String, verbose=True):
    if verbose:
        print(String)

############################################################################################################################
def addCatanTurtleToBoardObj(boardObj, verbose=False):
    boardObj.catan_turtle = CatanTurtle()

def addSuppliesToBoardObj(boardObj, verbose=False):
    boardObj.supplies = Supplies()
    
def addPlayersToBoardObj(boardObj, verbose=False):
    pColors = PLAYER_COLORS
    random.shuffle(pColors)
    sl = boardObj.side_length
    c2c = boardObj.center_to_center
    for i in range(boardObj.number_of_players):
        newPlayer = Player(player_color=pColors[i])
        boardObj.players[i+1] = newPlayer #Players are 1-indexed for the players' sakes

    boardObj.players[1].corner = (0 -sl*11, 0 +c2c*3 +c2c//2)
    boardObj.players[2].corner = (0 +sl*4, 0 +c2c*3 +c2c//2)
    boardObj.players[3].corner = (0 -sl*11, 0 -c2c*2 -5)
    boardObj.players[4].corner = (0 +sl*4, 0 -c2c*2 -5)

    for p in boardObj.players:
        currentPlayer = boardObj.players[p]
        currentCorner = currentPlayer.corner
        cX = currentCorner[0]
        cY = currentCorner[1]
        currentPlayer.wood_position = (cX+sl*0.5, cY-c2c*0.3)
        currentPlayer.brick_position = (cX+sl*1.5, cY-c2c*0.3)
        currentPlayer.sheep_position = (cX+sl*2, cY-c2c*0.3)
        currentPlayer.wheat_position = (cX+sl*2.5, cY-c2c*0.3)
        currentPlayer.ore_position = (cX+sl*3, cY-c2c*0.3)
        currentPlayer.settlement_position = (0,0)
        currentPlayer.city_position = (0,0)
        currentPlayer.road_position = (0,0)
        



def setNumberOfTilesPerSideOnBoard(boardObj, board_number_of_tiles_per_side=NUM_TILES_SIDE, verbose=False):
    docString = "Inside setNumberOfTilesPerSideOnBoard():"
    docString += "\nFirst, we must determine how large the board will be. (The default is 4 tiles to a side.)"
    # if board_number_of_tiles_per_side:
        # docString += "\nThe default size was overridden with " + str(board_number_of_tiles_per_side) + " tiles to a side."
        # boardObj.number_of_tiles_per_side = board_number_of_tiles_per_side
    # else:
        # docString += "\nThe default was used, so there will be " + str(NUM_TILES_SIDE) + " tiles per side."
        # boardObj.number_of_tiles_per_side = NUM_TILES_SIDE
    boardObj.number_of_tiles_per_side = NUM_TILES_SIDE #I'm not sure why the above code wasn't working, so I just hardcoded it for now.
    docString += "\nSo the boardObj.number_of_tiles_per_side = " + str(boardObj.number_of_tiles_per_side) + "."
    docString += "\n\n"
    printIfVerbose(docString, verbose=verbose) #I don't understand why I can't pass "verbose" instead of "verbose=verbose"
    
def getNumTiles(boardObj, verbose=False):
    docString = "Inside getNumTiles():"
    docString += "\nThe total number of tiles on the board is a function of the number of tiles per side."
    docString += "\n   That function is 1 + summation(6 * (x - 1)), where x is the range from 0 to the number of tiles per side."
    sum = 1
    for x in range(2,boardObj.number_of_tiles_per_side +1):
        sum += 6*(x - 1)
    printIfVerbose(docString, verbose)
    docString += "\n\n"
    printIfVerbose(docString, verbose=verbose)
    return sum
    
def setBoardNumbersOfTiles(boardObj, verbose=False):
    docString = "Inside setBoardNumbersOfTiles():"
    docString += "\nBecause the total number of tiles on the board and the number of playable tiles"
    docString += "\n   (the land tiles with playable vertices) are used many times, they are made attributes"
    docString += "\n   of the board itself."
    boardObj.number_of_tiles_on_board = getNumTiles(boardObj)
    docString += "\nThe number of playable (land) tiles is equal to y - (6 * (x - 1)), where"
    docString += "\n   x is the number of tiles per side, and y is the total number of tiles."
    boardObj.number_of_playable_tiles = boardObj.number_of_tiles_on_board - (6*(boardObj.number_of_tiles_per_side-1))
    docString += "\nSo the boardObj.number_of_tiles_on_board = " + str(boardObj.number_of_tiles_on_board) + ", and"
    docString += " the boardObj.number_of_playable_tiles = " + str(boardObj.number_of_playable_tiles) + "."
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def primeTheBoard(boardObj, verbose=False):
    addCatanTurtleToBoardObj(boardObj, verbose)
    addSuppliesToBoardObj(boardObj, verbose)
    addPlayersToBoardObj(boardObj, verbose)
    setNumberOfTilesPerSideOnBoard(boardObj, verbose)
    setBoardNumbersOfTiles(boardObj, verbose)
    
####################################################################################################################################
    
def setListOfTileNames(boardObj, verbose=False):
    docString = "Inside setListOfTileNames():"
    tileNames = boardObj.tile_names
    docString += "\nIt's easier to build the tile objects from an ordered list of the tiles' names."
    docString += "\n   This list of tile names is also helpful in just about every function that addresses the tile objects."
    tileNames.append("0-0")
    docString += "\nThe names are generated so that the index of each \"ring\" of the board's tiles is the first number of the name,"
    docString += "\n   and each tile in that ring is named sequentially in the second number of the name."
    
    for i in range(1, boardObj.number_of_tiles_per_side):   # For each of the board's rings (not including the center).
        tCounter = 0
        for j in range(6):                                  # For each of the sides of that ring
            for k in range(i):                              # For each tile in that side
                newTileName = str(i) + '-' + str(tCounter)
                tCounter += 1
                tileNames.append(newTileName)
    docString += "\nThe tile names are:"
    for n in range(len(boardObj.tile_names)):
        if n % 7 == 0:
            docString += "\n"
        docString += '{:10}'.format(boardObj.tile_names[n])
    docString += "\n\n"
    printIfVerbose(docString, verbose)
                
def addNamesToTileMap(boardObj, verbose=False):
    docString = "Inside addNamesToTileMap():"
    docString += "\nWe start the boardObj.tile_map with names from the boardObj.tile_names."
    docString += "\n   LandTile and SeaTile objects have different attributes, so"
    docString += "\n   playable tiles are created as LandTile objects,"
    for i in range(boardObj.number_of_playable_tiles):
        newTile = LandTile()
        newTile.name = boardObj.tile_names[i]
        boardObj.tile_map[newTile.name] = newTile
    
    docString += "\n   and ocean tiles are created as SeaTile objects."
    for i in range(boardObj.number_of_playable_tiles, boardObj.number_of_tiles_on_board): # For tile in the outer ring (ocean tiles).
        newTile = SeaTile()
        newTile.name = boardObj.tile_names[i]
        boardObj.tile_map[newTile.name] = newTile
    docString += "\nTile names are also their keys in the boardObj.tile_map."
    docString += "\n\n"
    printIfVerbose(docString, verbose)
        
def addCentersToTileMap(boardObj, verbose=False):
    docString = "Inside addCentersToTileMap():"
    docString += "\nIn order to add centers to the tile objects in the boardObj.tile_map, we"
    docString += "\n   use a catanTurtle object to travel in it's window by an algorithm identical to the"
    docString += "\n   one used in generating the tile names: per tile, per side, per ring."
    
    catanTurtle = boardObj.catan_turtle
    t = catanTurtle.turtle
    hdg = t.heading()
    tileNames = boardObj.tile_names
    tileNamesIndex = 0
    
    docString += "\nWe index into the boardObj.tile_names for the name keys into the boardObj.tile_map"
    docString += "\n   because they are ordered in the tile_names in the same order the turtle will travel."
    docString += "\n   Technically, this function and the creation of the names list could have been done together,"
    docString += "\n   but for compartmentalization's sake, they are tackled separately."
    docString += "\nBecause the geometry involved in finding the centers tends to make comparing coordinates difficult,"
    docString += "\n   it's important to use the custom catanTurtle.getPosition(), not the position() of cTurtle objects."
    
    boardObj.tile_map[tileNames[tileNamesIndex]].center = catanTurtle.getPosition() #Use catanTurtle.getPosition(), not t.position()
    for i in range(1,boardObj.number_of_tiles_per_side):
        t.left(90)
        t.forward(boardObj.center_to_center*i)
        t.right(120)
        for j in range(6):
            for k in range(i):
                tileNamesIndex += 1
                currentTile = boardObj.tile_map[tileNames[tileNamesIndex]]
                currentTile.center = catanTurtle.getPosition()
                t.forward(boardObj.center_to_center)
            t.right(60)
        t.goto(boardObj.tile_map["0-0"].center)
        t.setheading(hdg)
    t.goto(boardObj.tile_map["0-0"].center)
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
    
def getVertexList(boardObj, verbose=False):
    docString = "Inside getVertexList():"
    docString += "\nAs with the boardObj.tile_map, the boardObj.vertex_map is much easier to generate"
    docString += "\n   from a list of vertex locations."
    docString += "\nAgain, we use the boardObj.catan_turtle to gather the vertex locations around each"
    docString += "\n   of the tile centers already found. Some \"fudging\" has to be done with the"
    docString += "\n   AisWithinDofB() function to make sure the same vertex, having been found from"
    docString += "\n   different centers with slightly different positions, do not get added to the"
    docString += "\n   vertex_list more than once."
    catanTurtle = boardObj.catan_turtle
    t = catanTurtle.turtle
    hdg = t.heading()
    tmpVList = []
    
    for n in boardObj.tile_names:
        t.goto(boardObj.tile_map[n].center)
        tmpVList = catanTurtle.getHexVertices()
        for v1 in tmpVList:             # I'm trying to account for the minor rounding/positional discrepencies of
            oneCloseEnough = False      #   where the vertices "truly" are located since we're working with sqrt(3)
            if not v1 in boardObj.vertex_list:
                for v2 in boardObj.vertex_list:
                    if AisWithinDofB(v1,v2, 2):
                        oneCloseEnough = True
                if not oneCloseEnough:
                    boardObj.vertex_list.append(v1)
                
    t.goto(boardObj.tile_map["0-0"].center)
    t.setheading(hdg)
    docString += "\n\n"
    printIfVerbose(docString, verbose)
    
def addNamesAndLocationsToVertexMap(boardObj, verbose=False):
    docString = "Inside addNamesAndLocationsToVertexMap():"
    docString += "\nHaving set up the boardObj.vertex_list, we can easily enter the starter information"
    docString += "\n   for each vertex object (location) into the boardObj.vertex_map."
    docString += "\nVertex objects track and name themselves, and give themselves a name_string attribute"
    docString += "\n   for easily writing the names when we draw the board or place pieces. Since we're"
    docString += "\n   progressing through the vertex_list, and it contains the vertex locations in the"
    docString += "\n   we need anyway, the names are properly generated."
    docString += "\nThe vertex names, which are the integer indices of the vertex_list, are also the keys"
    docString += "\n   in the vertex_map."
    tmpVList = []
    tmpVObjList = []
    
    for i in range(len(boardObj.vertex_list)):
        newV = Vertex()
        newV.location = boardObj.vertex_list[i]
        newV.name_position = (newV.location[0] + (boardObj.side_length * 0.03), newV.location[1] - (boardObj.side_length * 0.1))
        boardObj.vertex_map[i] = newV
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def addVertexNamesToTileMap(boardObj, verbose=False):
    docString = "Inside addVertexNamesToTileMap():"
    docString += "\nIt's probably obvious that it's very helpful to look at a tile and know"
    docString += "\n   it's vertices, so we add the names (which are, again, the index numbers"
    docString += "\n   of it's vertices in the vertex_list) to each tile objects .vertices."
    
    testRadius = boardObj.side_length + 2
    for tileName in boardObj.tile_names:
        currentTile = boardObj.tile_map[tileName]
        currentCenter = currentTile.center
        currentTile.vertices = []
        for i in range(len(boardObj.vertex_list)):
            vLoc = boardObj.vertex_map[i].location
            if len(currentTile.vertices) < 6:   #This is just to prevent further searching if we've already found the six
                if AisWithinDofB(currentCenter, vLoc, testRadius):
                    currentTile.vertices.append(i)
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def addPlayableToVertexMap(boardObj, verbose=False):
    docString = "Inside addPlayableToVertexMap():"
    docString += "\nFor convenience's sake, it's nice if each vertex 'knows' if it is playable or not,"
    docString += "\n   and to have a list of the playable vertices. Each vertex object has a"
    docString += "\n   'playable' bool attribute for this purpose."
    
    for tileName in boardObj.tile_names:
        currentTile = boardObj.tile_map[tileName]
        if currentTile.kind == "LandTile":
            for vName in currentTile.vertices:
                targetV = boardObj.vertex_map[vName]
                targetV.playable = True
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def getPlayableVertices(boardObj, verbose=False):
    docString = "Inside getPlayableVertices():"
    docString += "\nHere, we simply build the boardObj's .playable_vertices list."
    
    pvList = []
    for i in range(len(boardObj.vertex_list)):
        currentVertex = boardObj.vertex_map[i]
        if currentVertex.playable == True and not i in pvList:
            pvList.append(i)
    # pvList.sort() #I don't think this is necessary
    boardObj.playable_vertices = pvList
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def addSurroundingTilesToVertexMap(boardObj, verbose=False): #I'm always second guessing what's returned to an iterator when looping through a dictionary
    docString = "Inside addSurroundingTilesToVertexMap():"
    docString += "\nIt's helpful in building certain data for a vertex to know which tiles surround it."
    
    for vertex in boardObj.vertex_map: # vertex = int
        sTiles = []
        currentVertex = boardObj.vertex_map[vertex]
        for tile in boardObj.tile_map: # tile = a tile's name, not the object itself (though that's how I wish it worked)
            currentTile = boardObj.tile_map[tile]
            if vertex in currentTile.vertices: 
               sTiles.append(tile)
        currentVertex.surrounding_tiles = sTiles
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
    
def addResourcesAndTradeTypesToTileMap(boardObj, verbose=False):
    docString = "Inside addResourceAndTradeTypesToTileMap():"
    docString += "\nEach of the playable tiles needs a resource type, and each of the sea tiles"
    docString += "\n   needs a trade type. Resource types are one of the following: 'Wood', 'Brick',"
    docString += "\n   'Wheat', 'Sheep', or 'Ore'. Trade types are either 'Water', 'Trade', or a"
    docString += "\n   hyphenation of 'Trade' and one of the resource types. These are added in"
    docString += "\n   random order to the respective tile objects in the tile_map."
    
    resourceTiles = RESOURCE_TILES[:]
    random.shuffle(resourceTiles)
    portsTemp = PORTS[:]
    random.shuffle(portsTemp)
    waterTiles = []
    ports = []
    for i in range(9):
        waterTiles.append("Water")
    if random.choice([True,False]):#Randomizing the order of the trade/non-trade tiles around the board
        for i in range(9):
            ports.append(waterTiles.pop())
            ports.append(portsTemp.pop())
    else:
        for i in range(9):
            ports.append(portsTemp.pop())
            ports.append(waterTiles.pop())
            
    for tile in boardObj.tile_map: #setting LandTile resource_type
        currentTile = boardObj.tile_map[tile]
        if currentTile.kind == "LandTile":
            currentTile.resource_type = resourceTiles.pop()
        
    for i in range(boardObj.number_of_playable_tiles, boardObj.number_of_tiles_on_board): #setting SeaTile trade_type, which must be done in order
        currentTile = boardObj.tile_map[boardObj.tile_names[i]]
        currentTile.trade_type = ports.pop()
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
    
def addResourcePositionsAndBackgroundColorsAndTradeRatiosToTileMap(boardObj, verbose=False): #Perhaps there's a better way to do this. I don't know
    docString = "Inside addResourcePositionsAndBackgroundColorsToTileMap():"
    docString += "\nEach tile resource/trade type has it's own background color and position"
    docString += "\n   within the tile for drawing the respective resource's symbol."
    docString += "\nThe trade and special trade tiles also have separate trade ratios used"
    docString += "\n    in the game, so that is set here, too."
    
    for tileName in boardObj.tile_names:
        currentTile = boardObj.tile_map[tileName]
        cx = currentTile.center[0]
        cy = currentTile.center[1]
        currentTile.name_position = (cx, cy + (boardObj.side_length * 0.58))
        
        if currentTile.kind == "LandTile":
            rt = currentTile.resource_type
            if rt == "Wood":
                currentTile.background_color = "#6BCF0C"
                rx = cx - (boardObj.side_length * currentTile.wood_x_trans)
                ry = cy + (boardObj.side_length * currentTile.wood_y_trans)
            elif rt == "Brick":
                currentTile.background_color = "#E88577"
                rx = cx - (boardObj.side_length * currentTile.brick_x_trans)
                ry = cy + (boardObj.side_length * currentTile.brick_y_trans)
            elif rt == "Sheep":
                currentTile.background_color = "Light Green"
                rx = cx - (boardObj.side_length * currentTile.sheep_x_trans)
                ry = cy + (boardObj.side_length * currentTile.sheep_y_trans)
            elif rt == "Wheat":
                currentTile.background_color = "#E8E47A"
                rx = cx - (boardObj.side_length * currentTile.wheat_x_trans)
                ry = cy + (boardObj.side_length * currentTile.wheat_y_trans)
            elif rt == "Ore":
                currentTile.background_color = "#AEAFB0"
                rx = cx - (boardObj.side_length * currentTile.ore_x_trans)
                ry = cy + (boardObj.side_length * currentTile.ore_y_trans)
            elif rt == "Desert":
                currentTile.background_color = "#6E6D6D"
                currentTile.resource_position = currentTile.center
            else:
                print("Something went wrong with addResourcePositionsAndBackgroundColorsAndTradeRatiosToTileMap()")
            
            if not rt == "Desert":
                currentTile.resource_position = (rx, ry)
        
        else: #currentTile.kind == "SeaTile"
            currentTile.background_color = "cornflower blue"
            currentTile.ratio_position = (currentTile.center[0], currentTile.center[1] - (boardObj.side_length * 0.84))
            tradeType = currentTile.trade_type.split('-')
            if tradeType[0] == "Trade":
                if len(tradeType) == 2:
                    currentTile.trade_ratio = 2
                    currentTile.trade_ratio_label = "2 : 1"
                    if tradeType[1] == "Wood":
                        rx = cx + (boardObj.side_length * currentTile.wood_x_trans)
                        ry = cy + (boardObj.side_length * currentTile.wood_y_trans)
                    elif tradeType[1] == "Brick":
                        rx = cx + (boardObj.side_length * currentTile.brick_x_trans)
                        ry = cy + (boardObj.side_length * currentTile.brick_y_trans)
                    elif tradeType[1] == "Sheep":
                        rx = cx + (boardObj.side_length * currentTile.sheep_x_trans)
                        ry = cy + (boardObj.side_length * currentTile.sheep_y_trans)
                    elif tradeType[1] == "Wheat":
                        rx = cx + (boardObj.side_length * currentTile.wheat_x_trans)
                        ry = cy + (boardObj.side_length * currentTile.wheat_y_trans)
                    elif tradeType[1] == "Ore":
                        rx = cx + (boardObj.side_length * currentTile.ore_x_trans)
                        ry = cy + (boardObj.side_length * currentTile.ore_y_trans)
                else:
                    currentTile.trade_ratio = 4
                    currentTile.trade_ratio_label = "4 : 1"
                    rx = cx
                    ry = cy
            if not tradeType[0] == "Water":
                currentTile.resource_position = (rx, ry)
            # tt = currentTile.trade_type.split('-')
            # if len(tt) == 2:
                # currentTile.trade_ratio = 2
                # currentTile.trade_ratio_label = "2 : 1"
                # if tt[1] == "Wood":
            # elif tt[0] == "Trade":
                # currentTile.trade_ratio = 4
                # currentTile.trade_ratio_label = "4 : 1"
                # currentTile.resource_position = currentTile.center
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def addDiceNumbersAndPositionsToTileMap(boardObj, verbose=False):
    docString = "Inside addDiceNumbersAndPositionsToTileMap():"
    docString += "\nEach playable tile needs a dice value, and we give it a random one from"
    docString += "\n   [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]."
    diceValues = DICE_VALUES[:]
    random.shuffle(diceValues)
    
    for i in range(boardObj.number_of_playable_tiles):
        currentTile = boardObj.tile_map[boardObj.tile_names[i]]
        cX = currentTile.center[0]
        cY = currentTile.center[1]
        if not currentTile.resource_type == "Desert":
            currentTile.dice_number = diceValues.pop()
            currentTile.dice_position = (cX + (boardObj.side_length * currentTile.dice_number_x_trans), cY - (boardObj.side_length * currentTile.dice_number_y_trans) )
        else:
            currentTile.dice_number = 7
            currentTile.has_robber = True
            boardObj.robber_tile = currentTile.name
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
            
def addNeighborsToTileMap(boardObj, verbose=False):
    docString = "Inside addNeighborsToTileMap():"
    for tileName in boardObj.tile_names:
        currentTile = boardObj.tile_map[tileName]
        currentTile.neighbors = []
        for lookAtTileName in boardObj.tile_names:
            if not lookAtTileName in currentTile.neighbors:
                if not tileName == lookAtTileName:
                    lookAtTile = boardObj.tile_map[lookAtTileName]
                    if AisWithinDofB(currentTile.center, lookAtTile.center, boardObj.center_to_center + 2):
                        currentTile.neighbors.append(lookAtTileName)
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def addNeighborsToVertexMap(boardObj, verbose=False):
    docString = "Inside addNeighborsToVertexMap():"
    for i in range(len(boardObj.vertex_list)):
        currentV = boardObj.vertex_map[i]
        currentV.neighbors = []
        for j in range(len(boardObj.vertex_list)):
            lookAtV = boardObj.vertex_map[j]
            if len(currentV.neighbors) < 3: #this is just to shorten search if the three neighbors have already been found
                if not i == j:
                    if AisWithinDofB(currentV.location, lookAtV.location, boardObj.side_length + 2):
                        currentV.neighbors.append(lookAtV.name) 
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def getCoastLine(boardObj, verbose=False): #I'm not sure anything needs this
    docString = "Inside getCoastLine():"
    coastLine = []
    for i in range(boardObj.number_of_playable_tiles - 6*(boardObj.number_of_tiles_per_side-2), boardObj.number_of_playable_tiles):
        currentTile = boardObj.tile_map[boardObj.tile_names[i]]
        for n in currentTile.neighbors:
            neighbor = boardObj.tile_map[n]
            if neighbor.kind == "SeaTile":
                for v in neighbor.vertices:
                    if v in currentTile.vertices:
                        if not v in coastLine:
                            coastLine.append(v)                            
    # coastLine.sort() #not sure this is necessary 
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
    return coastLine
    
def checkProperPortSpacing(boardObj, verbose=False):
    docString = "Inside checkProperPortSpacing():"
    for i in range(boardObj.number_of_playable_tiles - 6*(boardObj.number_of_tiles_per_side-2), boardObj.number_of_playable_tiles): #Should be looping through outer ring of playable tiles...
        check = 0
        currentTile = boardObj.tile_map[boardObj.tile_names[i]]
        for v in currentTile.vertices:
            if not boardObj.vertex_map[v].port_type == "Not A Port":
                check += 1
        if check > 3:
            print("ports still not working")
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)

def findCenterBeachVertex(boardObj, vertTriplet, verbose=False):
    docString = "Inside findCenterBeachVertex():"
    for v in vertTriplet:
        landCount = 0
        curV = boardObj.vertex_map[v]
        for tileName in curV.surrounding_tiles:
            if boardObj.tile_map[tileName].kind == "LandTile":
                landCount += 1
        if landCount == 2:
            centerV = curV.name
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
    return centerV

def findSecondPort(boardObj, vertDouble, verbose=False):
    portCount = 0
    v1 = vertDouble.pop(vertDouble.index(random.choice(vertDouble)))
    v2 = vertDouble.pop()
    lookFirstV = boardObj.vertex_map[v1]
    lookSecondV = boardObj.vertex_map[v2]
    for v in lookFirstV.neighbors:
        possibleV = boardObj.vertex_map[v]
        if not possibleV.port_type == "Not A Port":
            portCount += 1
    if portCount == 1:
        return lookFirstV.name
    elif portCount == 2:
        return lookSecondV.name
    elif portCount == 3:
        print("What happened at the beach?")
    elif portCount == 0:
            print("The universe is broken")
    else:
        print("Seriously, what the heck.")
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
    
def identifyPorts(boardObj, verbose=False):
    docString = "Inside identifyPorts():"
    portCount = 0
    
    for i in range(boardObj.number_of_playable_tiles, boardObj.number_of_tiles_on_board):
        currentTile = boardObj.tile_map[boardObj.tile_names[i]]
        if not currentTile.trade_type == "Water":
            beachFront = []
            for v in currentTile.vertices:
                currentV = boardObj.vertex_map[v]
                if currentV.playable:
                    beachFront.append(v)
            if len(beachFront) == 2:
                firstPort = boardObj.vertex_map[beachFront[0]]
                secondPort = boardObj.vertex_map[beachFront[1]]
                firstPort.port_type = currentTile.trade_type
                secondPort.port_type = currentTile.trade_type                
            elif len(beachFront) == 3:
                fpName = findCenterBeachVertex(boardObj, beachFront, verbose)
                firstPort = boardObj.vertex_map[beachFront.pop(beachFront.index(fpName))]
                firstPort.port_type = currentTile.trade_type
                spName = findSecondPort(boardObj, beachFront, verbose)
                secondPort = boardObj.vertex_map[spName]
                secondPort.port_type = currentTile.trade_type
            else:
                print("What happened on the beach?")                
    
    checkProperPortSpacing(boardObj)
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)
   
def addDockHeadingsToVertexMap(boardObj, verbose=False): #return_list probably helpful here, but didn't add it til later
    docString = "Inside addDockHeadingsToVertexMap():"
    slope = round(1/sqrt(3), 2)
    for v in boardObj.vertex_map:
        currentVert = boardObj.vertex_map[v]
        if not currentVert.port_type == "Not A Port":
            x = currentVert.location[0]
            y = currentVert.location[1]
            if x > 0:
                if y > (slope * x):
                    currentVert.dock_heading = 60
                elif y < (slope*-1 * x):
                    currentVert.dock_heading = 300
                else:
                    currentVert.dock_heading = 0
            else:
                if y > (slope*-1 * x):
                    currentVert.dock_heading = 120
                elif y < (slope * x):
                    currentVert.dock_heading = 240
                else:
                    currentVert.dock_heading = 180
    
    docString += "\n\n"
    printIfVerbose(docString, verbose)


def buildTileMapAndVertexMap(boardObj, verbose=False):
    setListOfTileNames(boardObj)#, verbose)
    addNamesToTileMap(boardObj)#, verbose)
    addCentersToTileMap(boardObj)#, verbose)
    getVertexList(boardObj)#, verbose)
    addNamesAndLocationsToVertexMap(boardObj)#, verbose)
    addVertexNamesToTileMap(boardObj)#, verbose)
    addPlayableToVertexMap(boardObj)#, verbose)
    getPlayableVertices(boardObj)#, verbose)
    addSurroundingTilesToVertexMap(boardObj)#, verbose)
    addResourcesAndTradeTypesToTileMap(boardObj)#, verbose)
    addResourcePositionsAndBackgroundColorsAndTradeRatiosToTileMap(boardObj)#, verbose)
    addDiceNumbersAndPositionsToTileMap(boardObj)#, verbose)
    addNeighborsToTileMap(boardObj)#, verbose)
    addNeighborsToVertexMap(boardObj)#, verbose)
    identifyPorts(boardObj)#, verbose)
    addDockHeadingsToVertexMap(boardObj)#, verbose)
    
############################################################################################################################
def getRoadList(boardObj, verbose=False):
    docString = "Inside getRoadList():"
    playVs = boardObj.playable_vertices
    for v in range(len(playVs)):
        currentV = boardObj.vertex_map[v]
        for n in currentV.neighbors:
            neighborV = boardObj.vertex_map[n]
            if neighborV.name in playVs:
                cX = currentV.location[0]
                nX = neighborV.location[0]
                if cX < nX:
                    roadName = str(currentV.name_string) + '~' + str(neighborV.name_string)
                else:
                    roadName = str(neighborV.name_string) + '~' + str(currentV.name_string)
                if not roadName in boardObj.road_list:
                    boardObj.road_list.append(roadName)
                    
    boardObj.road_list.sort()
            
def addNamesToRoadMap(boardObj, verbose=False):
    docString = "Inside addNamesToRoadMap():"
    for r in boardObj.road_list:
        newRoad = Road()
        newRoad.name = r
        boardObj.road_map[r] = newRoad
 
def addLocationsAndHeadingsToRoadMap(boardObj, verbose=False):
    docString = "Inside addLocationsAndHeadingsToRoadMap():"
    for r in boardObj.road_map:
        ends = r.split('~')
        v1 = boardObj.vertex_map[int(ends[0])].location
        v2 = boardObj.vertex_map[int(ends[1])].location
        boardObj.road_map[r].location = findMiddleAB(v1,v2)
        
        if v1[1] < v2[1]:
            boardObj.road_map[r].heading = 300
        elif v1[1] > v2[1]:
            boardObj.road_map[r].heading = 60
        else:
            boardObj.road_map[r].heading = 0

def addNeighborsToRoadMap(boardObj, verbose=False):
    docString = "Inside addNeighborsToRoadMap():"
    for r in boardObj.road_list:
        homeRoad = boardObj.road_map[r]
        homeRoad.neighbors = []
        ends = r.split('~')
        backVert = boardObj.vertex_map[int(ends[0])]
        frontVert = boardObj.vertex_map[int(ends[1])]
        for nV in backVert.neighbors:
            neighborV = boardObj.vertex_map[nV]
            if neighborV.playable:
                if not nV == frontVert.name:
                    bVX = backVert.location[0]
                    nVX = neighborV.location[0]
                    if bVX < nVX:
                        nRName = backVert.name_string + "~" + neighborV.name_string
                    else:
                        nRName = neighborV.name_string + "~" + backVert.name_string
                    homeRoad.neighbors.append(nRName)
        for nV in frontVert.neighbors:
            neighborV = boardObj.vertex_map[nV]
            if neighborV.playable:
                if not nV == backVert.name:
                    fVX = frontVert.location[0]
                    nVX = neighborV.location[0]
                    if fVX < nVX:
                        nRName = frontVert.name_string + "~" + neighborV.name_string
                    else:
                        nRName = neighborV.name_string + "~" + frontVert.name_string
                    homeRoad.neighbors.append(nRName)
    
def buildRoadMap(boardObj, verbose=False):
    getRoadList(boardObj, verbose)
    addNamesToRoadMap(boardObj, verbose)
    addLocationsAndHeadingsToRoadMap(boardObj, verbose)
    addNeighborsToRoadMap(boardObj, verbose)
    
#################################################################################################################
def addRoadsToTileMap(boardObj, verbose=False):
    for tileName in boardObj.tile_names:
        currentTile = boardObj.tile_map[tileName]
        if currentTile.kind == "LandTile":
            currentTile.roads = []
            for roadName in boardObj.road_list:
                ends = roadName.split('~')
                backVert = int(ends[0])
                frontVert = int(ends[1])
                if backVert in currentTile.vertices and frontVert in currentTile.vertices:
                    currentTile.roads.append(roadName)

#################################################################################################################


#################################################################################################################

def buildData(boardObj, verbose=False):
    primeTheBoard(boardObj)#, verbose)
    buildTileMapAndVertexMap(boardObj)#, verbose)
    buildRoadMap(boardObj)#, verbose)
    addRoadsToTileMap(boardObj)#, verbose=False)
    
    
    # getVertexList(boardObj)
    # addNamesAndLocationsToVertexMap(boardObj)
    # addVertexObjsToTileMap(boardObj)
    # addPlayableToVertexMap(boardObj)
    # getPlayableVertices(boardObj)
    # addSurroundingTilesToVertexMap(boardObj)
    # addResourceAndTradeTypesToTileMap(boardObj)
    # addResourcePositionsAndBackgroundColorsToTileMap(boardObj)
    # addDiceNumbersAndPositionsToTileMap(boardObj)
    # addNeighborsToTileMap(boardObj)
    # addNeighborsToVertexMap(boardObj)
    # identifyPorts(boardObj)
    # addSurroundingTilesToVertexMap(boardObj)
    # addDockHeadingsToVertexMap(boardObj)
    # getRoadList(boardObj)
    # addNamesToRoadMap(boardObj)
    # addLocationsAndHeadingsToRoadMap(boardObj)
    # #addNeighborsToRoadMap(boardObj)