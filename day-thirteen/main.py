def retrieveInput(file):
  return open(file, "r").read().splitlines()

schedule = retrieveInput("input.txt")

# solution one
def earlyBusProdWait(input):
    time = int(input[0])
    busIDs = list(map(int, input[1].replace(",x", "").split(",")))

    earliestBus = min(busIDs)
    mins = earliestBus

    for bus in busIDs:
        temp = bus - (time % bus)
        if temp < mins:
            earliestBus = bus 
            mins = temp 
    return earliestBus * mins

# solution two
def earliestOffsetTimestamp(input):
    busOffsets = [] 
    max = 1
    input = input[1].split(",")
    for x in input:
        if x != 'x':
            busOffsets.append((int(x), input.index(x)))
            max *= int(x)

    timestamp = 0
    found = False
    while not found:
        temp = 1
        for i in range(0, len(busOffsets)):
            if (timestamp + busOffsets[i][1]) % busOffsets[i][0] == 0:
                temp *= busOffsets[i][0]
        if temp == max:
            found = True
            break
        timestamp += temp 
    return timestamp
    
print(earlyBusProdWait(schedule))
print(earliestOffsetTimestamp(schedule))