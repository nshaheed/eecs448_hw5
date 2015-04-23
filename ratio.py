

# Get ratio of list of bools ([Bool]), where ratio is (number of True)/(number of False)
def getRatio(lst):
    numTrue = len([i for i in lst if i])
    numFalse = len([i for i in lst if not i])

    if numFalse == 0:
        return 0.
    else:
        ratio = float(numTrue) / float(numFalse)
        return ratio

# Testing
# test1 = [False, True, True, False, True, True]

# print(getRatio(test1))
