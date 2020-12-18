# first solution
def productTwoN(values, n):
  pastVals = []
  for x in values:
    val = int(x)
    temp = n - val  
    if temp in pastVals:
      return temp * val 
    pastVals.append(val)

# second solution
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
    input = open("account.txt", "r").read().splitlines()
    print(productTwoN(input, 2020))
    print(productThreeN(input, 2020))
  except ValueError:
    print("Only integers allowed.")
  except:
    print("Something else happened...")

# this could be greatly improved...but it's getting late
main()