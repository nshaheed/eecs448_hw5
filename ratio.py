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
