# AOC Day 3

path = open("input.txt", "r").read().splitlines()

def countAllTrees(right, down):
    count = 0
    currDistance = right 
    for i in range(down, len(path), down):
        if path[i][currDistance % len(path[i])] == '#':
            count += 1 
        currDistance += right 
    return count


print(countAllTrees(1, 1) * countAllTrees(3, 1) * 
countAllTrees(5, 1) * countAllTrees(7, 1) * 
countAllTrees(1, 2))