#AOC Day 5
import math

# returns an array of file lines
def retrieveInput(file):
  return open(file, "r").read().splitlines()

input = retrieveInput("input.txt")

# while there are directions, narrow down the range of possibles
def binaryFind(directions, possibles):
    if directions == "":
        return possibles[0]
    else:
        low = possibles[0]
        high = possibles[1]
        direction = directions[0]
        if direction == 'F' or direction == 'L':
            possibles = [low, math.floor((low + high) / 2)]
        else:
            possibles = [math.ceil((low + high) / 2), high]
        return binaryFind(directions[1:], possibles)

# find every seat ID and return the max
def maxSeatID(passes):
    maxID = 0
    for bPass in passes:
        if len(bPass) == 10:
            rows = bPass[:7]
            cols = bPass[7:]
            row = binaryFind(rows, [0, 127])
            col = binaryFind(cols, [0, 7])
            bPassID = row * 8 + col 
            if bPassID > maxID:
                maxID = bPassID 
    return maxID

# if the plane is full, find the single unfilled seat
def findSeatID(passes):
    allSeats = []
    for bPass in passes:
        if len(bPass) == 10:
            rows = bPass[:7]
            cols = bPass[7:]
            row = binaryFind(rows, [0, 127])
            col = binaryFind(cols, [0, 7])
            bPassID = row * 8 + col 
            allSeats.append(bPassID)
    allSeats = sorted(allSeats)
    allFilled = sum(s for s in range(allSeats[0], allSeats[-1] + 1))
    return allFilled - sum(allSeats)     

print(findSeatID(input))