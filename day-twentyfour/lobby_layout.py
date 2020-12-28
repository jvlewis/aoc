from collections import defaultdict
import re

tilesToFlip = open('tiles.txt', 'r').read().splitlines()
flipped = defaultdict(int)
days = 100
regex = 'e|se|sw|w|nw|ne'
blackTiles = 0

for tile in tilesToFlip:
    directions = re.findall(regex, tile)
    q = r = 0
    for direction in directions:
        if direction == 'e':
            q += 1
        if direction == 'se':
            r += 1
        if direction == 'sw':
            q -= 1
            r += 1
        if direction == 'w':
            q -= 1
        if direction == 'nw':
            r -= 1
        if direction == 'ne':
            q += 1
            r -= 1 
    
    flipped[(q, r)] += 1

for tile, flipCount in flipped.items():
    if flipCount % 2 == 1:
        blackTiles += 1

# Solution 1
print('There are initially %d black tiles.' % blackTiles)

adjPoints = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]

for _ in range(days):
    adjBlack = defaultdict(int)
    
    for tile, count in flipped.items():
        if count % 2 == 0:
            continue

        for pt in adjPoints:
            adjBlack[(tile[0] + pt[0], tile[1] + pt[1])] += 1

    nextState = {}

    for tile, count in flipped.items():
        if count % 2 == 1:
            if adjBlack.get(tile, 0) in (1, 2):
                nextState[tile] = 1
        
    for tile, count in adjBlack.items():
        if count == 2 and flipped.get(tile, 0) % 2 == 0:
            nextState[tile] = 1 
    flipped = nextState 

blackTiles = 0
for tile, flipCount in flipped.items():
    if flipCount % 2 == 1:
        blackTiles += 1

#Solution 2
print('After %d days, there are %d black tiles.' % (days, blackTiles))

