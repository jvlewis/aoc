from itertools import product
import copy
INSTRUCTIONS = open("input.txt", "r").read().splitlines()

def countOccurences(ch, strList):
  result = 0
  for x in strList:
    if x == ch:
      result += 1 
  return result

def bitMaskValues(instructions):
    memory = [0] * (2**16)
    mask = ''

    for x in range(len(instructions)):
        ins = instructions[x]
        ins = ins.split(" = ")

        if ins[0] == 'mask':
            mask = list(ins[1])
        else:
            temp = ins[0]
            addr = int(temp[temp.index('[') + 1:temp.index(']')])
            val = list(str(bin(int(ins[1]))[2:].zfill(36)))

            for ch in range(len(mask)):
                if mask[ch] == '1' and val[ch] == '0':
                    val[ch] = '1'
                if mask[ch] == '0' and val[ch] == '1':
                    val[ch] = '0' 
        
            memory[addr] = int("".join(val), 2)

    print(sum(memory))

def bitMaskAddr(instructions):
    memory = {}
    mask = ''

    for x in range(len(instructions)):
        ins = instructions[x]
        ins = ins.split(" = ")

        if ins[0] == 'mask':
            mask = list(ins[1])
        else:
            temp = ins[0]
            addr = list(bin(int(temp[temp.index('[') + 1:temp.index(']')]))[2:].zfill(36))
            val = int(ins[1])

            for ch in range(len(mask)):
                if mask[ch] != '0':
                    addr[ch] = mask[ch]

            addr = list("".join(addr).lstrip("0"))
            
            for bits in list(product([0,1],repeat=countOccurences('X', addr))):
                last = -1
                newAddr = copy.copy(addr)

                for bit in bits:
                    tmpI = newAddr.index('X', last + 1)
                    last = tmpI
                    newAddr[tmpI] = str(bit)

                temp = int("".join(newAddr).lstrip('0'), 2)
                memory[temp] = val
                
    print(sum(memory.values()))

bitMaskValues(INSTRUCTIONS)
bitMaskAddr(INSTRUCTIONS)