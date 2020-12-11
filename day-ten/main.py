def processInput(file):
      return sorted(list(map(int, open(file, "r").read().splitlines())))

# solution one
def findOneAndThree(adapters):
  maxAdapter = adapters[-1]
  diff1 = diff2 = diff3 = last = 0
  for x in adapters:
    if x - last == 1:
      diff1 += 1
      last = x
    elif x - last == 2:
      diff2 += 1
      last = x
    elif x - last == 3:
      diff3 += 1
      last = x
    else:
      continue

  diff3 += 1 

  print(diff1 * diff3)

#solution two
def findAllChains(adapters):

    # each adapter will have a possible place for a recorded sum
    result = [0] * (adapters[-1] + 1)

    # summation starts at one, all other indices hold zeros
    # these values may or may not be subsequently filled
    result[0] = 1

    for x in adapters:
        # for each adapter, record a sum of previous sums, 
        # within the acceptable jolt range
        result[x] = sum(result[x - i] for i in range(1, 4))
    # last entry hold the total
    print(result[-1])


adaptersList = processInput("input.txt")
findOneAndThree(adaptersList)
findAllChains(adaptersList)