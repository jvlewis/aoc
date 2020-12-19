input = open("input.txt", "r").read().splitlines()

# returns a list of each space index, with None
# representing the beginning and end of the string
def findSpaces(string: str):
    spaces = [None]
    temp = 0
    while " " in string[temp + 1:]:
        temp = string.index(" ", temp + 1)
        spaces.append(temp)
    spaces.append(None)
    return spaces

# returns a list of each expression in expString
def getExpressions(expString: str):
    length = len(expString)
    spacePos = findSpaces(expString)

    if len(spacePos) == 2:
        return [expString]

    return [expString[spacePos[i]:spacePos[i + 3]].strip() 
        for i in range(0, len(spacePos), 2) 
            if i < len(spacePos) - 2] 

# evaluate a list of expressions from left to right,
# or apply rules to force addition to take precedence,
# and return the integer result 
def evalExp(expressions: list, flipped=False):
    if flipped:
        return applyAdvRules(expressions)
    else:
        curr = eval(expressions[0])
        
        for subexp in expressions[1:len(expressions)]:
            if " " not in subexp:
                break;
            curr = eval(str(curr) + subexp[subexp.index(" "):])
        return curr 

# reduce all addition expressions in the string of expressions
# then eval the final string
def applyAdvRules(exp: str):
    temp = exp
    while '+' in temp:
        temp = str(processPlus(temp))
    return eval(temp)

# reduce an addition operation in an expression string
def processPlus(exp: str):
    space = findSpaces(exp)

    i = exp.index("+")
    end = space[space.index(i + 1) + 1]
    begin = space[space.index(i + 1) - 2]
    result = eval(exp[begin:end])

    if not end and not begin:
        return result
    elif not begin:
        exp = str(result) + exp[end:]
    elif not end:
        exp = exp[:begin] + str(result)
    else:
        exp = exp[:begin + 1] + str(result) + exp[end:]
    return exp

# do each problem, with regular or advanced rules
# return the sum of the result of each problem
def doHomework(input, adv):
    total = 0 
    for exp in input:
        temp = exp 
        while '(' in exp:
            openParen = 0
            closeParen = exp.index(")")
            while '(' in exp[openParen + 1:closeParen]:
                openParen = exp.index('(', openParen + 1)
                closeParen = exp.index(')')

            if adv:
                temp = exp[openParen + 1:closeParen]
                exp = exp[0:openParen] + str(evalExp(temp, adv)) + exp[closeParen+1:]
            else:
                temp = getExpressions(exp[openParen + 1:closeParen])
                exp = exp[0:openParen] + str(evalExp(temp)) + exp[closeParen+1:]
        if adv:
            total += evalExp(exp, adv)
        else:
            exp = getExpressions(exp)
            total += evalExp(exp)
    return total

print('The sum of all result values in part 1: %d' % doHomework(input, False))
print('The sum of all result values in part 2: %d' % doHomework(input, True))




