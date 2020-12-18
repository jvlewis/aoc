path = open("input.txt", "r").read().splitlines()

def countTrees(right, down):
    count = 0
    currDistance = right
    for i in range(down, len(path), down):
        if path[i][currDistance % len(path[i])] == '#':
            count += 1 
        currDistance += right 
    return count

print("P1-Trees encountered in path R3D1: %d" % countTrees(3, 1))
print("P2-Trees encountered in all given paths : %d" %
    (countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * 
        countTrees(7, 1) * countTrees(1, 2)))