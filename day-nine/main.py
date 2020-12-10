from itertools import combinations

def retrieveInput(file):
  return open(file, "r").read().splitlines()

def searchStream(preamble, num):
  for x in combinations(preamble, 2):
    if sum(x) == num:
      return True
  return None

# solution one
def findOutlier(stream, pre):
  for x in range(pre + 1, len(stream)):
    if not searchStream(stream[x - pre - 1: x], stream[x]):
      return stream[x] 
  return None

#solution two
def findWeakness(stream, pre):
    outlier = findOutlier(stream, pre)

    for i in range(0, len(stream) - 2):
        j = i + 2
        total = 0
        temp = []
        while total < outlier:
            temp = stream[i:j]
            total = sum(temp)
            j += 1
        if total == outlier:
            return min(temp) + max(temp)
    return None

        
digitStream = list(map(int, retrieveInput("input.txt")))
print(findOutlier(digitStream, 25))
print(findWeakness(digitStream, 25))