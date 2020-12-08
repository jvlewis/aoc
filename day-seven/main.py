def retrieveInput(file):
  return open(file, "r").read().splitlines()

input = retrieveInput("input.txt")

# solution one
def countPossibleContainers(contained, regs):
    bags = dict()
    temp = []

    for x in regs:
        x = x.split("bags contain")
        bags[x[0].strip()] = x[1].replace("bags", "").replace("bag", "").replace(".", "").strip()

    for x in bags.keys():
        if contained in bags[x]:
            temp.append(x)

    for x in temp:
        for y in bags.keys():
            if x in bags[y]:
                temp.append(y) 
    print(len(set(temp)))

countPossibleContainers('shiny gold', input)


# solution 2
def bagDict(bagContains):
    temp = {}
    eol = 'no other'
    for container in bagContains.split(','):
        key = container[2:].replace('.', '').replace(' bags', '').replace(' bag', '').strip()
        if eol in container:
            temp[eol] = 0
        else:
            temp[key] = int(container.strip()[0])
    return temp

def processBaggage(bagRegs):
    bagRegDict = {}
    for reg in bagRegs:
        key, value = reg.split(' bags contain ')
        bagRegDict[key] = bagDict(value)
    return bagRegDict

def countContainers(regs):
    sum = 1
    for bag in regs.keys():
        sum += regs[bag]*(0 if bag == 'no other' else countContainers(regulations[bag]))
    return sum

regulations = processBaggage(input)
print(countContainers(regulations['shiny gold']) - 1)