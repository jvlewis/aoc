from collections import defaultdict
from functools import reduce
from operator import mul
import math

# process initial input
def processTileInput(inp):
    tiles = defaultdict(int)
    key = 0
    temp = []
    
    for line in inp:
        if 'Tile' in line:
            key = int(line[line.index(' ') + 1:line.index(':')])
        elif len(line) > 0:
            temp.append(line)
        else:
            tiles[key] = temp
            temp = []
    tiles[key] = temp
    return tiles

# grid conversion methods
def gridStringToArray(grid):
    new = grid.copy()
    for i, string in enumerate(new):
        new[i] = list(string)
    return new

def gridArrayToString(grid):
    new = grid.copy()
    for i, row in enumerate(new):
        new[i] = "".join(row)
    return new

# grid movement methods

# top becomes bottom
def xFlipTile(tile):
    newTile = []
    length = len(tile)
    temp = length - 1
    
    for i in range(length):
        newTile.append(tile[temp])
        temp -= 1
    
    return newTile 

# flip then reverse
def xyFlipTile(tile):
    return yFlipTile(xFlipTile(tile))

# left becomes right
def yFlipTile(tile):
    length = len(tile)
    tempTile = gridStringToArray(tile)
    newTile = []
    temp = length - 1

    for i in range(length):
        newTile.append([])
        temp = length - 1
        for j in range(length):
            newTile[i].append(tempTile[i][temp])
            temp -= 1
    
    return gridArrayToString(newTile)  

# rows -> columns, columns -> rows
def shiftTile(tile):
    length = len(tile)
    tile = gridStringToArray(tile)
    newTile = []
    temp = length - 1

    for i in range(length):
        newTile.append([])
        for j in range(length):
            newTile[i].append(tile[j][temp])
        temp -= 1
    
    return gridArrayToString(newTile[::-1]) 

def returnAllVariations(tile):
    result = []
    
    result.append(tile)
    result.append(xFlipTile(tile))
    result.append(yFlipTile(tile))
    result.append(xyFlipTile(tile))
    tile = shiftTile(tile)
    result.append(tile)
    result.append(xFlipTile(tile))
    result.append(yFlipTile(tile))
    result.append(xyFlipTile(tile))
    return result


# return list of 4 edges for all tiles
def returnTileEdges(tiles):
    edges = defaultdict(int)
    
    for tile in tiles:
        grid = tiles[tile]
        edge1 = edge2 = edge3 = edge4 = ''
        length = len(grid)

        for i in range(length):
            edge1 += grid[0][i]
            edge2 += grid[i][0]
            edge3 += grid[length-1][i]
            edge4 += grid[i][length-1]
        edges[tile] = [edge1, edge2, edge3, edge4]
    return edges

# doing the same thing w/ sep data types...must refactor
def returnAnonEdges(tiles):
    edges = []
    
    for grid in tiles:
        edge1 = edge2 = edge3 = edge4 = ''
        length = len(grid)

        for i in range(length):
            edge1 += grid[0][i]
            edge2 += grid[i][0]
            edge3 += grid[length-1][i]
            edge4 += grid[i][length-1]
        edges.append([edge1, edge2, edge3, edge4])
    return edges

# return number of edges that match with at least 
# one other edge from another tile that may or 
# # may not be shifted/reversed, for each tile
def returnEdgeMatches(edges):
    matches = defaultdict(int)
    
    for edge in edges:
        match = 0
        matches[edge] = match
        thisEdges = edges[edge]
        
        for entry in edges:
            if entry != edge:
                for own in thisEdges:
                    if own in edges[entry] or ''.join(reversed(own)) in edges[entry]:
                        matches[edge] += 1 
    return matches

# solution to part 1
def returnCornerProd(matches): 
    return reduce(mul, [id for id, x in matches.items() if x == 2], 1)

# sorts tiles into type based on matches
def sortTileTypes(matches):
    types = {
        'corner': [],
        'border': [],
        'body': []
    }

    for id, match in matches.items():
        if match == 2:
            types['corner'].append(id)
        elif match == 3:
            types['border'].append(id)
        else:
            types['body'].append(id)
    
    return types

# tbc...

def findCorner(corner, borders, tiles):
    right = bottom = []

    borderOne = borders[0]
    borderTwo = borders[1]

    thisTile = tiles[corner]
    borderPosOne = tiles[borderOne]
    borderPosTwo = tiles[borderTwo]

    thisVars = returnAllVariations(thisTile)
    borderPosOneVars = returnAllVariations(borderPosOne)
    borderPosTwoVars = returnAllVariations(borderPosTwo)

    thisEdges = returnAnonEdges(thisVars)
    borderPosOneEdges = returnAnonEdges(borderPosOneVars)
    borderPosTwoEdges  = returnAnonEdges(borderPosTwoVars)

    for i in range(len(thisEdges)):
        for j in range(len(borderPosOneEdges)):
            if thisEdges[i][3] == borderPosOneEdges[j][1] or thisEdges[i][3] == "".join(reversed(borderPosOneEdges[j][1])):
                right = [borderOne, i, j]
            elif thisEdges[i][3] == borderPosTwoEdges[j][1] or thisEdges[i][3] == "".join(reversed(borderPosTwoEdges[j][1])):
                right = [borderTwo, i, j]               
            elif thisEdges[i][0] == borderPosOneEdges[j][2] or thisEdges[i][0] == "".join(reversed(borderPosOneEdges[j][2])):
                bottom = [borderOne, i, j]
            elif thisEdges[i][0] == borderPosTwoEdges[j][2] or thisEdges[i][0] == "".join(reversed(borderPosTwoEdges[j][2])):
                bottom = [borderTwo, i, j]

            if len(right) > 0 and len(bottom) > 0 and right[1] == bottom[1]:
                print('thisTile: ' + str(thisVars[0]))
                print('rightTile: ' + str(borderPosOneVars[1]))
                print('bottomTile: ' + str(borderPosTwoVars[2]))
                print('matchedEDgeR: ' + str(thisEdges[0][3]))
                print('matchedEDgeB: ' + str(borderPosOneEdges[1][1]))
                print('matchedEDgeR: ' + str(thisEdges[0][0]))
                print('matchedEDgeB: ' + str(borderPosTwoEdges[2][2]))
                return [right, bottom]
    return False

# return list of the tiles that border id
def findTileNeighbors(id, edges, types):
    curr = edges[id]
    temp = { id: [] }

    for tile in types:
        if tile != id:
            pos = edges[tile]
            for edge in curr:
                if edge in pos or "".join(reversed(edge)) in pos:
                    temp[id].append(tile)
    return temp

# return placement and position of image tiles 
def arrangeTiles(tiles, edges, neighbors, dim):
    assembledGrid = [[[] for i in range(dim)] for j in range(dim)]

    corners = neighbors['corner']

    for i in range(len(corners)):
        thisCorner = list(corners[i].keys())[0]
        thisBorders = corners[i][thisCorner]

        possible = findCorner(thisCorner, thisBorders, tiles)

        if possible:
            print(possible)
            break

# return list of tile ids at corresponding grid location
def returnTileNeighbors(matches, edges, dim):
    # each tile type w/ their neighbors
    neighbors = {
        'corner' : [],
        'border' : [],
        'body' : []
    }
    
    for x in matches['corner']:
        neighbors['corner'].append(findTileNeighbors(x, edges, matches['border']))
    for x in matches['border']:
        neighbors['border'].append(findTileNeighbors(x, edges, matches['corner'] + matches['body'] + matches['border']))
    for x in matches['body']:
        neighbors['body'].append(findTileNeighbors(x, edges, matches['border'] + matches['body']))
    
    return neighbors           
# ....

if __name__ == '__main__':
    input = open("tiles.txt", "r").read().splitlines()
    tiles = processTileInput(input)
    edges = returnTileEdges(tiles)
    gridDims = int(math.sqrt(len(edges)))
    matches = returnEdgeMatches(edges)
    
    print('The product if each corner tile ID is %d' 
        % returnCornerProd(matches))

    tileTypes = sortTileTypes(matches)
    neighbors = returnTileNeighbors(tileTypes, edges, gridDims)
    
    arrangeTiles(tiles, edges, neighbors, gridDims)
    
    