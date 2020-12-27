import copy

def scoreWinner(player):
    score = 0
    for i in range(len(player)):
        score += int(int(player[i]) * abs(i - len(player)))
    return score

def recursiveCombat(player1, player2):
    past1 = past2 = set()

    while len(player1) != 0 and len(player2) != 0:
        
        if " ".join(player1) in past1 or " ".join(player2) in past2:
            return player1, []

        past1.add(" ".join(player1))
        past2.add(" ".join(player2))

        draw1 = int(player1.pop(0))
        draw2 = int(player2.pop(0))


        if len(player1) >= draw1 and len(player2) >= draw2:
            subGame = recursiveCombat(player1[:draw1], player2[:draw2])[0]
            recurseWin = player1 if subGame else player2
        else:
            recurseWin = player1 if draw1 > draw2 else player2

        if recurseWin == player1:
            player1.extend([str(draw1), str(draw2)])
        else:
            player2.extend([str(draw2), str(draw1)])
    return player1, player2

def playCombat(player1, player2):
    while len(player1) != 0 and len(player2) != 0:
        draw1 = int(player1.pop(0))
        draw2 = int(player2.pop(0))

        if draw1 > draw2:
            player1.append(draw1)
            player1.append(draw2)
        else:
            player2.append(draw2)
            player2.append(draw1)
    print(scoreWinner(player1 if len(player1) != 0 else player2))


if __name__ == '__main__':
    cards = open("cards.txt", "r").read().split('\n\n')
    draw1 = cards[0].split('\n')[1:]
    draw2 = cards[1].split('\n')[1:]
    
    playCombat(copy.copy(draw1), copy.copy(draw2))

    results = recursiveCombat(copy.copy(draw1), copy.copy(draw2))
    print(scoreWinner(results[0]) if results[0] else scoreWinner(results[1]))
