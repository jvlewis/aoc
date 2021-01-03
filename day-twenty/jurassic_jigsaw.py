import re
from collections import Counter, namedtuple, defaultdict
from functools import reduce
from itertools import chain, groupby
from math import prod
import math
from operator import add, mul

T, R, B, L = 0, 1, 2, 3

def reverse_string(string):
    return ''.join(reversed(string))

# grid conversion methods
# def gridStringToArray(grid):
#     new = grid.copy()
#     for i, string in enumerate(new):
#         new[i] = list(string)
#     return new

# def gridArrayToString(grid):
#     new = grid.copy()
#     for i, row in enumerate(new):
#         new[i] = "".join(row)
#     return new

# # grid movement methods

# # top becomes bottom
# def xFlipTile(tile):
#     newTile = []
#     length = len(tile)
#     temp = length - 1
    
#     for i in range(length):
#         newTile.append(tile[temp])
#         temp -= 1
    
#     return newTile 

# # flip then reverse
# def xyFlipTile(tile):
#     return yFlipTile(xFlipTile(tile))

# # left becomes right
# def yFlipTile(tile):
#     length = len(tile)
#     tempTile = gridStringToArray(tile)
#     newTile = []
#     temp = length - 1

#     for i in range(length):
#         newTile.append([])
#         temp = length - 1
#         for j in range(length):
#             newTile[i].append(tempTile[i][temp])
#             temp -= 1
    
#     return gridArrayToString(newTile)  

# # rows -> columns, columns -> rows
# def shiftTile(tile):
#     length = len(tile)
#     tile = gridStringToArray(tile)
#     newTile = []
#     temp = length - 1

#     for i in range(length):
#         newTile.append([])
#         for j in range(length):
#             newTile[i].append(tile[j][temp])
#         temp -= 1
    
#     return gridArrayToString(newTile[::-1]) 

# def returnAllVariations(tile):
#     result = []
    
#     result.append(tile)
#     result.append(xFlipTile(tile))
#     result.append(yFlipTile(tile))
#     result.append(xyFlipTile(tile))
#     tile = shiftTile(tile)
#     result.append(tile)
#     result.append(xFlipTile(tile))
#     result.append(yFlipTile(tile))
#     result.append(xyFlipTile(tile))
#     return result


# # return list of 4 edges for all tiles
# def returnTileEdges(tiles):
#     edges = defaultdict(int)
    
#     for tile in tiles:
#         grid = tiles[tile]
#         edge1 = edge2 = edge3 = edge4 = ''
#         length = len(grid)

#         for i in range(length):
#             edge1 += grid[0][i]
#             edge2 += grid[i][0]
#             edge3 += grid[length-1][i]
#             edge4 += grid[i][length-1]
#         edges[tile] = [edge1, edge2, edge3, edge4]
#     return edges

# # doing the same thing w/ sep data types...must refactor
# def returnAnonEdges(tiles):
#     edges = []
    
#     for grid in tiles:
#         edge1 = edge2 = edge3 = edge4 = ''
#         length = len(grid)

#         for i in range(length):
#             edge1 += grid[0][i]
#             edge2 += grid[i][0]
#             edge3 += grid[length-1][i]
#             edge4 += grid[i][length-1]
#         edges.append([edge1, edge2, edge3, edge4])
#     return edges

# # return number of edges that match with at least 
# # one other edge from another tile that may or 
# # # may not be shifted/reversed, for each tile
# def returnEdgeMatches(edges):
#     matches = defaultdict(int)
    
#     for edge in edges:
#         match = 0
#         matches[edge] = match
#         thisEdges = edges[edge]
        
#         for entry in edges:
#             if entry != edge:
#                 for own in thisEdges:
#                     if own in edges[entry] or ''.join(reversed(own)) in edges[entry]:
#                         matches[edge] += 1 
#     return matches

# # solution to part 1
# def returnCornerProd(matches): 
#     return reduce(mul, [id for id, x in matches.items() if x == 2], 1)

# # sorts tiles into type based on matches
# def sortTileTypes(matches):
#     types = {
#         'corner': [],
#         'border': [],
#         'body': []
#     }

#     for id, match in matches.items():
#         if match == 2:
#             types['corner'].append(id)
#         elif match == 3:
#             types['border'].append(id)
#         else:
#             types['body'].append(id)
    
#     return types

# # return list of the tiles that border id
# def findTileNeighbors(id, edges, types):
#     curr = edges[id]
#     temp = { id: [] }

#     for tile in types:
#         if tile != id:
#             pos = edges[tile]
#             for edge in curr:
#                 if edge in pos or "".join(reversed(edge)) in pos:
#                     temp[id].append(tile)
#     return temp

# # return list of tile ids at corresponding grid location
# def returnTileNeighbors(matches, edges, dim):
#     # each tile type w/ their neighbors
#     neighbors = {
#         'corner' : [],
#         'border' : [],
#         'body' : []
#     }
    
#     for x in matches['corner']:
#         neighbors['corner'].append(findTileNeighbors(x, edges, matches['border']))
#     for x in matches['border']:
#         neighbors['border'].append(findTileNeighbors(x, edges, matches['corner'] + matches['body'] + matches['border']))
#     for x in matches['body']:
#         neighbors['body'].append(findTileNeighbors(x, edges, matches['border'] + matches['body']))
    
#     return neighbors

class ImageTile:
    def __init__(self, id, image):
        self.id = id
        self.image = image
        self.edges = self.get_edges()
        self.dim = len(self.image)

    def __repr__(self):
        return str(self.id)

    def render(self):
        return '\n'.join(self.image)

    def get_edges(self):
        return [
            self.image[0],
            ''.join(row[-1] for row in self.image),
            self.image[-1],
            ''.join(row[0] for row in self.image)
        ]

    def get_edge(self, dir):
        return self.get_edges()[dir]

    def reverse_edges(self):
        return list(map(reverse_string, self.edges))

    def flip_over_y(self):
        self.image = list(map(reverse_string, self.image))

    def flip_over_x(self):
        self.image.reverse()

    def rotate_clockwise(self):
        self.image = [''.join(self.image[col][row] 
            for col in reversed(range(self.dim)))
            for row in range(self.dim)]

    def rotate_counter_clock(self):
        self.image = [''.join(self.image[col][row] 
            for col in range(self.dim))
            for row in  reversed(range(self.dim))]


# returns the original image
def form_image(tiles, corners, edge_matches):
    image_order = [[]]
    corners = list(reversed(corners))
    current_tile = tiles[corners.pop()]
    print(edge_matches)
    # find borders without neighbors
    no_neighbors = [edge for edge in edge_matches if edge_matches[edge] == {current_tile.id}]
    print(no_neighbors)
    # find first tile orientation
    while current_tile.get_edge(T) not in no_neighbors:
        if reverse_string(current_tile.get_edge(T)) in no_neighbors:
            current_tile.flip_over_y()
        else:
            current_tile.rotate_counter_clock()

    height = 0
    image_order[height].append(current_tile)
    width = 1
    print(image_order)
    while len(corners) > 0:
        while (height == 0 and current_tile.id not in corners) or (len(image_order[height]) < width):
            connect = current_tile.get_edge(R)
            print(connect)
            if connect in edge_matches:
                candidate = next(iter(edge_matches[connect] - {current_tile.id}))
            elif reverse_string(connect) in edge_matches:
                candidate = next(iter(edge_matches[reverse_string(connect)] - {current_tile.id}))

            candidate = tiles[candidate]

            while candidate.get_edge(L) != connect:
                if candidate.get_edge(L) == reverse_string(connect):
                    candidate.flip_over_y() 
                else:
                    candidate.rotate_clockwise() 

            image_order[height].append(candidate)

            if height == 0:
                width += 1
            current_tile = candidate

        if current_tile.id in corners:
            corners.remove(current_tile.id)
            if len(corners) == 0:
                break 
                
        current_tile = image_order[height][0]
        if current_tile.id in corners:
            corners.remove(current_tile.id)
            continue

        connect = current_tile.get_edge(B)
        if connect in edge_matches:
            candidate = next(iter(edge_matches[connect] - {current_tile.id}))
        else:
            candidate = next(iter(edge_matches[reverse_string(connect)] - {current_tile.id}))
        candidate = tiles[candidate]

        while candidate.get_edge(T) != connect:
            if candidate.get_edge(T) == reverse_string(connect):
                candidate.flip_over_y() 
            else:
                candidate.rotate_clockwise() 

        image_order.append([])
        height += 1
        image_order[height].append(candidate)
        current_tile = candidate
    print(image_order)

    return None


# returns list of corner tiles and dict of edges that match other tile edges 
def find_image_corners(tiles):
    edge_matches = {}
    edges = []

    for tile in tiles:
        tile = tiles[tile]
        for edge, reversed_edge in zip(tile.get_edges(), tile.reverse_edges()):
            if edge in edge_matches:
                edge_matches[edge].add(tile.id)
            elif reversed_edge in edge_matches:
                edge_matches[reversed_edge].add(tile.id)
            else:
                edge_matches[edge] = {tile.id}
    
    for edge in edge_matches.values():
        if len(edge) == 1:
            edges.append(*edge)
    
    edges = Counter(edges)
    
    return [id for id in edges if edges[id] == 2], edge_matches
    
# process initial satellite message
def processSatMessage(file):
    tiles = {}
    inp = open(file, "r").read().split('\n\n')
    inp = [tile.split('\n') for tile in inp]
    for tile in inp:
        tile_id = int(tile[0].split(' ')[1].replace(':', ''))
        del tile[0]
        tiles[tile_id] = ImageTile(tile_id, tile) 

    return tiles       

if __name__ == '__main__':
    tiles = processSatMessage("tiles.txt")
    corner_tiles, edge_matches = find_image_corners(tiles)

    # Solution 1
    print('The product if all corner tile IDs is %d' 
         % reduce(mul, corner_tiles))

    image = form_image(tiles, corner_tiles, edge_matches)

    # gridDims = int(math.sqrt(len(tiles)))
    # edges = returnTileEdges(tiles)
    # matches = returnEdgeMatches(edges)
    
    # print('The product if each corner tile ID is %d' 
    #     % returnCornerProd(matches))

    # tileTypes = sortTileTypes(matches)

    # neighbors = returnTileNeighbors(tileTypes, edges, gridDims)

    # print(neighbors)
    
    # arrangeTiles(tiles, edges, neighbors, gridDims)