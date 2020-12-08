def retrieveInput(file):
      return open(file, "r").read().splitlines()

def createHistory(inp):
    history = []
    for x in inp:
      history.append([x, 0])
    return history

inp = retrieveInput("input.txt")
historyArr = createHistory(inp)

def processInstruction(cmd, acc, hist, ind, sequential=True):
    if cmd[0] == 'acc':
        hist[ind][1] += 1
        acc = eval(str(acc) + cmd[1][0] + str(cmd[1][1:]))
        ind += 1
    elif cmd[0] == 'jmp':
        hist[ind][1] += 1
        ind = (eval(str(ind) + cmd[1][0] + str(cmd[1][1:])))
        if not sequential:
            ind = ind % len(hist)
    else:
        hist[ind][1] += 1
        ind += 1 

    return acc, hist, ind   

# solution one
def processInstructions(commands):
  total = 0
  i = 0

  while True: 
    instruction = commands[i][0].split(' ')

    if commands[i][1] > 0:
      return total

    total, commands, i = processInstruction(instruction, total, commands, i, False)

#solution two
def correctInstructions(commands):
  tried = 0
  while tried < len(commands) - 1:
      changed = False
      changedInstruct = ''
      while not changed:
        temp, tempEnd = commands[tried].split(' ')
        if temp == 'jmp':
          changedInstruct = 'nop ' + tempEnd 
          tried += 1
          changed = True
        elif temp == 'nop':
          changedInstruct = 'jmp ' + tempEnd
          tried += 1
          changed = True
        else:
          tried += 1 

      freshTry = createHistory(commands)

      total = 0
      i = 0

      while i < len(freshTry):
        if i == tried - 1:
          instruction = changedInstruct.split(' ')
        else:
          instruction = freshTry[i][0].split(' ')

        if freshTry[i][1] > 0:
          break

        total, freshTry, i = processInstruction(instruction, total, freshTry, i)
        
        if i >= len(commands):
          return total

print(processInstructions(historyArr))
print(correctInstructions(inp))