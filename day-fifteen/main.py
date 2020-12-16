START_NUMS = list(map(int, open("input.txt", "r").read().split(",")))

def playElvenMemoryGame(firstNums, lastTurn):
    pastRounds = {}
    lastNum = firstNums[-1]
    turn = len(firstNums)

    for i, k in enumerate(firstNums):
        pastRounds[k] = i + 1 

    while turn <= lastTurn:
        if turn == lastTurn:
            return lastNum

        lastRound = pastRounds.get(lastNum, 0)
        pastRounds[lastNum] = turn

        if lastRound == 0:
            lastNum = lastRound
        else:
            lastNum = turn - lastRound;

        turn += 1 

if __name__ == '__main__':
    print("The 2020th number of the sequence that begins with [%s] is: %d" % 
        (", ".join(map(str, START_NUMS)), playElvenMemoryGame(START_NUMS, 2020)))
    print("The 30 millionth number of the sequence that begins with [%s] is: %d" % 
        (", ".join(map(str, START_NUMS)), playElvenMemoryGame(START_NUMS, 30000000)))
    
