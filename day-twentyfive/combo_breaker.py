"""
Find every loopsize value up to a (currently) arbitrary max size,
and stop after the loopsize for each public key is found.
Returns a list containing two lists -> the key at index 0 and the loopsize at 1,
or an error message if both aren't found
"""
def findLoopsizes(pubKeyOne, pubKeyTwo, maxLoop):
    loopsize = 0
    value = 1
    loopsizes = []
    found = 0

    for i in range(maxLoop):
        value *= subjectNumber
        value %= 20201227

        if value == pubKeyOne or value == pubKeyTwo:
            found += 1
            loopsizes.append([value, i + 1])

        if found == 2:
            return loopsizes
    return "--- both loopsizes not found, increase max or check keys --- "


"""
Setting the subject number to one of the keys and transforming
it with the opposite key's loopsize results in the encryption key.
Testing that this returns the same value for each key validates the result. 
"""
def findEncryptionKey(loopsizes):
    value = 1
    subjectNumber = loopsizes[1][0]
    for _ in range(loopsizes[0][1]):
        value *= subjectNumber
        value %= 20201227 
    firstValue = value

    value = 1
    subjectNumber = loopsizes[0][0]
    for _ in range(loopsizes[1][1]):
        value *= subjectNumber
        value %= 20201227
    secondValue = value

    if firstValue == secondValue:
        return firstValue
    else:
        return "--- failed to find key ---"


if __name__ == "__main__":
    cardPublicKey = 10705932
    doorPublicKey = 12301431

    MAX = 10000000 # arbitrarily set to a range that returns both loopsizes
    subjectNumber = 7 # defined by handshake

    loops = findLoopsizes(cardPublicKey, doorPublicKey, MAX)

    print("Pulic key %d uses a loopsize of %d and public key %d uses a loopsize of %d" % 
        (loops[0][0], loops[0][1], loops[1][0], loops[1][1]))

    print("The handshake is trying to establish an encryption key of %d" % findEncryptionKey(loops))