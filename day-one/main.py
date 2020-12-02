# returns an array of file lines
def retrieveInput(file):
  return open(file, "r").read().splitlines()

# brute force
# def sumTwoN(values, n):

#   for i in values:
#     for j in values[1:]:
#       return int(i) * int(j)
#   return -1

# def sumTwoN(values, n):

#   pastVals = []
#   for x in values:
#     val = int(x)
#     temp = n - val  
#     if temp in pastVals:
#       return temp * val 
#     pastVals.append(val)

# find the product of three digits in an array that sum to a target
def productThreeN(values, target):
  pastVals = []

  for i in values:
    firstVal = int(i)
    for j in values:
      secondVal = int(j)
      temp = target - firstVal - secondVal
      # if a previous val could sum to n with the two current nums, 
      # return the product of the three
      if temp in pastVals:
        return temp * firstVal * secondVal 
    pastVals.append(firstVal)
    
def main():
  try:
    print(productThreeN(retrieveInput("account.txt"), 2020))
  except ValueError:
    print("Only integers allowed.")
  except:
    print("Something else happened...")

# this could be greatly improved...but it's getting late
main()