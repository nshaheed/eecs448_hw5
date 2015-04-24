""" Returns ratio of true positives to false positives.  This is what we are supposed to graph and maximize.  Expects a list of booleans (True for compounds found to be Active by our test) in the same order as the data in the database."""
def ratio(results):
    numActive = 1347 # the actual number of active compounds. They are listed first in the database.
    truePositives = 0
    falsePositives = 0
    for i in range(len(results)):
        if results[i]: # compounds tested as non-active don't count toward the score
            if i < numActive:
                truePositives += 1
            else:
                falsePositives += 1
    if falsePositives == 0:
        return float("inf")
    return float(truePositives) / float(falsePositives)


# Get ratio of list of bools ([Bool]), where ratio is (number of True)/(number of False)
def getRatio(lst):
    numA = len([i for i in lst if i == "A"])
    numN = len([i for i in lst if i == "N"])

    # returns -1 if the ratio is n/0
    if numN == 0:
        return -1.
    else:
        ratio = float(numA) / float(numN)
        return ratio

# Testing
# test1 = [False, True, True, False, True, True]

# print(getRatio(test1))
