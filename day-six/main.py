# AOC Day 6
import re

# returns an array of strings of group 'yes' answers
def retrieveInput(file):
    temp = ""
    answers = []
    for x in open(file, "r").read().splitlines():
        temp += x + " "
        if x == "":
            answers.append(temp.rstrip())
            temp = ""
    answers.append(temp.rstrip())
    return answers

responses = retrieveInput("input.txt")

# solution one: for each group, sum # of distinct yes answers from anyone,
#               and return the sum of those sums 
def countAllGroupYes(answers):
    groupSets = []

    for group in answers:
        groupSets.append(set(group.replace(" ", "")))
    return sum(len(group) for group in groupSets) 

# solution two: for each group, sum # of distinct yes answers shared by everyone
#               in the group, and return the sum of those sums 
def countExclusiveGroupYes(answers):
    total = 0

    for group in answers:
        if re.search("\s", group):
            temp = []
            for ans in group.split(" "):
                temp.append(set(ans))
            total += len(set.intersection(*temp))
        else:
            total += len(group)
    return total

print(countExclusiveGroupYes(responses))

