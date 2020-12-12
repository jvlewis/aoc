# must refactor...no time...

def retrieveInput(file):
    temp = open(file, "r").read().splitlines()
    for i in range(len(temp)):
      temp[i] = list(temp[i])
    return temp 

def returnChart(seatingChart):
    for i in range(len(seatingChart)):
        seatingChart[i] = ''.join(seatingChart[i])
    return '\n'.join(map(str, seatingChart))


def returnAdjacentSeats(seatList, row, col):
    seats = []

    # check orthogonal seats
    if col > 0:
        seats.append(seatList[row][col - 1])
    if col < len(seatList[row]) - 1:
        seats.append(seatList[row][col + 1])
    if row > 0:
        seats.append(seatList[row - 1][col])
    if row < len(seatList) - 1:
        seats.append(seatList[row + 1][col])

    # check diagonals
    if col > 0 and row > 0:
        seats.append(seatList[row - 1][col - 1])
    if row > 0 and col < len(seatList[row]) - 1:
        seats.append(seatList[row - 1][col + 1])
    if row < len(seatList) - 1 and col > 0:
        seats.append(seatList[row + 1][col - 1])
    if row < len(seatList) - 1 and col < len(seatList[row]) - 1:
        seats.append(seatList[row + 1][col + 1])

    return seats

def returnSeatsInSight(seatList, row, col):
    seats = []
    tempRow = row
    tempCol = col

    # check orthogonal seats

    # left
    while tempCol > 0:
        tempSeat = seatList[row][tempCol - 1]
        if tempSeat == '.':
            tempCol -= 1
        else:
            seats.append(tempSeat)
            break 

    tempCol = col
    
    # right
    while tempCol < len(seatList[row]) - 1:
        tempSeat = seatList[row][tempCol + 1]
        if tempSeat == '.':
            tempCol += 1
        else:
            seats.append(tempSeat)
            break 
    
    tempCol = col

    # up
    while tempRow > 0:
        tempSeat = seatList[tempRow - 1][col]
        if tempSeat == '.':
            tempRow -= 1
        else:
            seats.append(tempSeat)
            break

    tempRow = row 

    # down
    while tempRow < len(seatList) - 1:
        tempSeat = seatList[tempRow + 1][col]
        if tempSeat == '.':
            tempRow += 1 
        else:
            seats.append(tempSeat)
            break 

    tempRow = row 

    # check diagonal seats

    # top left
    while tempCol > 0 and tempRow > 0:
        tempSeat = seatList[tempRow - 1][tempCol - 1]
        if tempSeat == '.':
            tempCol -= 1
            tempRow -= 1 
        else:
            seats.append(tempSeat)
            break 

    tempRow = row
    tempCol = col 

    # top right
    while tempRow > 0 and tempCol < len(seatList[row]) - 1:
        tempSeat = seatList[tempRow - 1][tempCol + 1] 
        if tempSeat == '.':
            tempRow -= 1
            tempCol += 1 
        else:
            seats.append(tempSeat)
            break 

    tempRow = row 
    tempCol = col

    # bottom left
    while tempRow < len(seatList) - 1 and tempCol > 0:
        tempSeat = seatList[tempRow + 1][tempCol - 1]
        if tempSeat == '.':
            tempRow += 1
            tempCol -= 1
        else:
            seats.append(tempSeat)
            break

    
    tempRow = row
    tempCol = col 

    # bottom right
    while tempRow < len(seatList) - 1 and tempCol < len(seatList[row]) - 1:
        tempSeat = seatList[tempRow + 1][tempCol + 1]
        if tempSeat == '.':
            tempRow += 1
            tempCol += 1 
        else:
            seats.append(tempSeat)
            break

    return seats

def processBoard(seatList, tolerance):
    newList = []
    for row in range(len(seatList)):
        tempList = []
        for col in range(len(seatList[row])):
            adjSeats = returnSeatsInSight(seatList, row, col) # returnAdjacentSeats(seatList, row, col) 
            currentSeat = seatList[row][col]
            temp = 0
            if currentSeat == 'L':
                for seat in adjSeats:
                    if seat == '#':
                        temp += 1
                        break 
                if temp == 0:
                    currentSeat = '#'
            elif currentSeat == '#':
                for seat in adjSeats:
                    if seat == '#':
                        temp += 1
                if temp >= tolerance:
                    currentSeat = 'L'
            tempList.append(currentSeat)
        newList.append(tempList)
    return newList

def stableSeating(seatList, tolerance):
    stillSeating = True
    seats = 0
    while stillSeating:
        newSeating = processBoard(seatList, tolerance)
        numSame = 0
        for i in range(len(newSeating)):
            temp = "".join(newSeating[i])
            if temp == "".join(seatList[i]):
                numSame += 1
            if numSame == len(seatList):
                stillSeating = False
        seatList = newSeating
    
    for row in range(len(seatList)):
        for col in range(len(seatList[row])):
            if seatList[row][col] == '#':
                seats += 1 
    return seats
                        

rawChart = retrieveInput("input.txt")

# solution one
# print(stableSeating(rawChart, 4))

#solution two
print(stableSeating(rawChart, 5))




