def retrieveInput(file):
      return open(file, "r").read().splitlines()

def createHistory(inp):
    history = []
    for x in inp:
      history.append([x, 0])
    return history

inp = retrieveInput("input.txt")
historyArr = createHistory(inp)

# solution one
def processInstructions(commands):
  sum = 0
  i = 0

  while True: 
    instructions = commands[i][0].split(' ')

    if commands[i][1] > 0:
      return sum

    if instructions[0] == 'acc':
      commands[i][1] += 1
      sum = eval(str(sum) + instructions[1][0] + str(instructions[1][1:]))
      i += 1
    elif instructions[0] == 'jmp':
      commands[i][1] += 1
      i = (eval(str(i) + instructions[1][0] + str(instructions[1][1:]))) % len(commands)
    else:
      commands[i][1] += 1
      i += 1

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
          instructions = changedInstruct.split(' ')
        else:
          instructions = freshTry[i][0].split(' ')

        if freshTry[i][1] > 0:
          break

        if instructions[0] == 'acc':
          freshTry[i][1] += 1
          total = eval(str(total) + instructions[1][0] + str(instructions[1][1:]))
          i += 1
        elif instructions[0] == 'jmp':
          freshTry[i][1] += 1
          i = (eval(str(i) + instructions[1][0] + str(instructions[1][1:])))
        else:
          freshTry[i][1] += 1
          i += 1
        
        if i >= len(commands):
          return total

print(processInstructions(historyArr))
print(correctInstructions(inp))