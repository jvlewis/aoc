from collections import deque

tickets = deque(open("input.txt", "r").read().splitlines())

def returnTicketDetails():
    ticketFields = {}
    allTickets = {'you': [], 'near': []}
    section = 0

    while len(tickets) > 0:
        temp = tickets.popleft()

        if temp == "":
            section += 1
            tickets.popleft()
            temp = tickets.popleft()
        
        if section == 0:
            temp = temp.split(": ")
            tempBound = temp[1].split(" or ")
            tempArr = []
            for bound in tempBound:
                tempArr.append(tuple(map(int, bound.split('-'))))
                ticketFields[temp[0]] = tempArr  
        elif section == 1:
            allTickets['you'] = list(map(int, temp.split(",")))
        else:
            allTickets['near'].append(list(map(int, temp.split(","))))       
    return ticketFields, allTickets

def validTicket(val, values):
    for rule in values:
        lowerRange = val >= rule[0][0] and val <= rule[0][1]
        higherRange = val >= rule[1][0] and val <= rule[1][1]
        if lowerRange or higherRange:
            return True 
    return False

def removeInvalidTickets(ticketRules, allTickets):
    invalidValuesSum = 0
    invalidTickets = []
    values = ticketRules.values()

    for ticket in allTickets['near']:
        valTicket = True 
        for val in ticket:
            if not validTicket(val, values):
                valTicket = False
                invalidValuesSum += val
        if not valTicket:
            invalidTickets.append(ticket)
    for ticket in invalidTickets:
        allTickets['near'].remove(ticket)
    return invalidValuesSum, allTickets

def findRuleOrder(rules, near):
    actualOrder = {}
    actual = [False] * len(rules)
    
    while len(actualOrder) < len(rules):
        for col, rule in rules.items():
            if col in actualOrder:
                continue 

            possible = []

            for i, pos in enumerate(actual):
                valid = True 
                if pos is not False:
                    continue 
                for temp in near:
                    if not ((temp[i] >= rule[0][0] and temp[i] <= rule[0][1]) or (temp[i] >= rule[1][0] and temp[i] <= rule[1][1])):
                        valid = False 
                if valid:
                    possible.append(i)
            if len(possible) == 1:
                found = possible.pop()
                actual[found] = col 
                actualOrder[col] = found
            
    return actualOrder

def translateFields(rules, order):
    final = [''] * len(order)
    for rule, pos in order.items():
        final[pos] = rule
    return final

if __name__ == '__main__':
    rules, tickets = returnTicketDetails()    
    invalidValueSum, tickets = removeInvalidTickets(rules, tickets)
    ruleOrder = findRuleOrder(rules, tickets['near'])
    departProd = 1  

    for i, rule in enumerate(translateFields(rules, ruleOrder)):
        if 'departure' in rule:
            departProd *= tickets['you'][i]

    print("The ticket scanning error rate is: %d" % invalidValueSum)
    print("The product of the departure values is: %d" % departProd)