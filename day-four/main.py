# AOC Day 4

# returns an array of passport credentials
def retrieveInput(file):
    temp = ""
    passports = []
    for x in open(file, "r").read().splitlines():
        temp += x + " "
        if x == "":
            passports.append(temp.rstrip())
            temp = ""
    passports.append(temp.rstrip())
    return passports

#solution one
# def numMaybeValidPassports(creds):
#     valid = 0

#     for x in creds:
#         letEmSlide = False
#         x = x.split(" ")
#         print(x)
#         length = len(x)
#         if length == 8:
#             valid += 1
#         elif length == 7:
#             letEmSlide = True
#             for field in x:
#                 if field.split(":")[0] == 'cid':
#                     letEmSlide = False 
#         if letEmSlide:
#             valid += 1 

#     print(valid)

# determine if one of the eight given fields are valid
def validField(type, val):
    def validBirthY():
        if len(val) == 4 and 1920 <= int(val) and int(val) <= 2002:
            return True 
        return False

    def validIssueY():
        if len(val) == 4 and 2010 <= int(val) and int(val) <= 2020:
            return True
        return False
    
    def validExpireY():
        if len(val) == 4 and 2020 <= int(val) and int(val) <= 2030:
            return True
        return False

    def validHeight():
        ending = val[-2:]
        num = val[:-2]
        if ending == 'cm' and 150 <= int(num) and int(num) <= 193:
            return True
        elif ending == 'in' and 59 <= int(num) and int(num) <= 76:
            return True
        return False

    def validHexHair():
        octoQ = val[0]
        if octoQ == '#':
            temp = list(val[1:])
            if len(temp) == 6:
                for i in list(val[1:]):
                    temp = ord(i)
                    if (48 <= temp and temp <= 57) or (97 <= temp and temp <= 102):
                        continue 
                    else:
                        return False 
                return True 
        return False

    def validEyeWeDecide():
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return val in colors

    def validID():
        return len(val) == 9

    # shhh...
    def validCID():
        return False

    # err of the side of safety
    def default():
        return False

    dict = {
        'byr' : validBirthY,
        'iyr' : validIssueY,
        'eyr' : validExpireY,
        'hgt' : validHeight,
        'hcl' : validHexHair,
        'ecl' : validEyeWeDecide,
        'pid' : validID ,
        'cid' : validCID
    }
    
    return dict.get(type,default)()

def passportDict(passportFields):
    dict = {}
    for field in passportFields:
        pair = field.split(":")
        dict[pair[0]] = pair[1]
    return dict

def meetsRequiredFields(passport, fields):
    req = 0
    for field in passport:
        if field in fields:
            req += 1
    return req == len(fields)

def numValidPassports(creds):
    valid = 0
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for cred in creds:
        count = 0
        cred = passportDict(cred.split(" "))
        keys = cred.keys()
        values = list(cred.values())
        if meetsRequiredFields(keys, requiredFields):
            for i, key in enumerate(keys):
                if validField(key, values[i]):
                    count += 1 
        if count == len(requiredFields):
            valid += 1 
    print(valid) 
            
numValidPassports(retrieveInput("input.txt"))


