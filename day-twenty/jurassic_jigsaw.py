from collections import defaultdict
from functools import reduce
from operator import mul
import math

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

def returnTileEdges(tiles):
    edges = defaultdict(int)
    for tile in tiles:
        grid = tiles[tile]
        edge1 = edge2 = edge3 = edge4 = ''
        for i in range(len(grid)):
            edge1 += grid[0][i]
            edge2 += grid[i][0]
            edge3 += grid[9][i]
            edge4 += grid[i][9]
        edges[tile] = [edge1, edge2, edge3, edge4]
    return edges

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

def returnCornerProd(matches): 
    return reduce(mul, [id for id, x in matches.items() if x == 2], 1)

# tbc...
def returnTileOrder(matches, edges):
    gridDims = int(math.sqrt(len(matches)))
    order = [[0 for i in range(gridDims)] for j in range(gridDims)]
    print(edges.values())
# ....

if __name__ == '__main__':
    input = open("tiles.txt", "r").read().splitlines()
    tiles = processTileInput(input)
    edges = returnTileEdges(tiles)
    matches = returnEdgeMatches(edges)
    
    print('The product if each corner tile ID is %d' 
        % returnCornerProd(matches))

    

    