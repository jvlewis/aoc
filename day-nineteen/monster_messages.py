from collections import defaultdict

def returnRulesAndMessages():
    inp = open("messages.txt", "r").read().splitlines()

    rules = defaultdict(int)
    messages = inp[inp.index("")+1:]

    for x in inp[:inp.index('')]:
        key, value = x.split(": ")
        if '"' in value:
            rules[int(key)] = value.replace('"', '')
        else:
            temp = []
            for val in value.split(' | '):
                temp.append([int(x) for x in val.split()])
            rules[int(key)] = temp 

    return rules, messages

def isMatch(msg, rule):
    
    if len(rule) == 0:
        return len(msg) == len(rule)  
    elif len(rule) > len(msg):
        return False 

    temp = rule.pop()
    
    if type(temp) is str:
        if msg[0] == temp:
            return isMatch(msg[1:], rule)
    else:
        for tmp in rules[temp]:
            if isMatch(msg, rule + list(reversed(tmp))):
                return True 
    return False

def sumValidMessages(messages, rules, swapped=False):
    total = 0

    if swapped:
        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]

    for message in messages:
        if isMatch(message, list(reversed(rules[0][0]))):
            total += 1
    return total

if __name__ == '__main__':
    rules, messages = returnRulesAndMessages()
    print(rules)
    print('There are %d valid messages in the list before changing rules 8 and 11.' 
        % sumValidMessages(messages, rules))
    print('There are %d valid messages in the list after changing rules 8 and 11.'
        % sumValidMessages(messages, rules, True))


