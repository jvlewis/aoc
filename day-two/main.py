# AOC Day 2

# returns an array of file lines
def retrieveInput(file):
  return open(file, "r").read().splitlines()

# solution one - first 
# def processPasswords(rulesAndWords):
#     valid = 0

#     for x in rulesAndWords:
#         x = x.split(':')
#         rule = x[0].split(" ")
#         nums = rule[0].split("-")
#         low = int(nums[0])
#         high = int(nums[1])
#         ch = rule[1]
#         word = x[1].lstrip()
#         count = word.count(ch)
#         if count >= low and count <= high:
#             valid += 1 

#     return valid

# solution two - first
def processPasswords(rulesAndWords):
    valid = 0

    for x in rulesAndWords:
        x = x.split(':')
        rule = x[0].split(" ")
        nums = rule[0].split("-")
        low = int(nums[0])
        high = int(nums[1])
        ch = rule[1]
        word = x[1].lstrip()
        
        try:
            if ((word[low-1] == ch) ^ (word[high-1] == ch)):
                print(word + " - char -> " + ch)
                print(nums)
                valid += 1
        except:
            continue

    return valid


print(processPasswords(retrieveInput("input.txt")))