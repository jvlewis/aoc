from itertools import chain
circle = '135468729'

def cupOrder(startingOrder, cups):
    cupLabels = list(map(int, startingOrder))

    if cups > len(cupLabels):
        cupLabels.extend(range(len(cupLabels) + 1, cups + 1))

    cupList = {}
    start = curr = cupLabels[0]

    for label in cupLabels:
        cupList[curr] = label
        curr = label 
    cupList[curr] = start

    return cupList, start 

def play(start, cups, rounds):
    order, cur = cupOrder(start, cups)
    length = len(order)

    for round in range(rounds):
        removed = [
            one := order[cur],
            two := order[one],
            three := order[two]
        ]
    
        order[cur] = order[three]

        dest = cur - 1 if cur > 1 else length 
        while dest in removed:
            dest = dest - 1 if dest > 1 else length 
        
        order[three] = order[dest]
        order[dest] = one

        cur = order[cur]
    return order, cur

lastState, lastCurr = play(circle, len(circle), 100)
cup = 1
ending = []
for _ in range(len(circle) - 1):
    cup = lastState[cup]
    ending.append(str(cup))
print(''.join(ending))

lastState, lastCurr = play(circle, 1000000, 10000000)
print(lastState[1] * lastState[lastState[1]])

