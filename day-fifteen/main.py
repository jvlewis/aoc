START_NUMS = list(map(int, open("input.txt", "r").read().split(",")))

def playElvenMemoryGame(lastTurn):
    pastRounds = {}
    lastNum = START_NUMS[-1]
    turn = len(START_NUMS)

    for i, k in enumerate(START_NUMS):
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
    nums = ", ".join(map(str, START_NUMS))
    print("The 2020th number of the sequence that begins with [%s] is: %d" % 
        (nums, playElvenMemoryGame(2020)))
    print("The 30 millionth number of the sequence that begins with [%s] is: %d" % 
        (nums, playElvenMemoryGame(30000000)))
    
