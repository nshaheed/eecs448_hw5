
# classify.py
# Andrei Elliott 2015/04/19
# EECS 448 HW5
# 

import math
import ratio

# Euclidean distance between two vectors
def euclidVec(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Input vectors must have the same length: ", v1, v2)
    return math.sqrt(sum([(v2[i] - v1[i])**2 for i in range(len(v1))]))

def euclid(v, stats):
    pass # return euclidVec(v, stats.mean)

# calculate Mahalanobis distance of v from distribution with given stats
# type/format for stats TBD
def mahalanobis(v, stats):
    pass #todo: implement

# classifies based on distance in all dimensions
# method should be :: v -> Stats -> Bool, e.g. euclid, mahalanobis
def directClassify(v, statsActive, statsInactive, method):
    return method(v, statsActive) < method(v, statsInactive)

# classifies based on voting method: compares dimensions separately and votes
def votingClassify(v, statsActive, statsInactive, method):
    length = len(v)
    activeCount = 0
    for i in range(length):
        if method([v[i]],statsActive.getDimension(i)) < method([v[i]],statsInactive.getDimension(i)):
            activeCount += 1
    return activeCount > length / 2

# custom classification method based off of the given four.  Assume True = Active, False = NonActive
#    currently: A simple majority vote
def customClassify(euclid, mahal, euclidVote, mahalVote):
    lst = [euclid, mahal, euclidVote, mahalVote]
    numTrue = len([i for i in lst if i])
    if numTrue >= 2:
        return True
    else:
        return False


# calculate stats object for given set of vectors
def getStats(vs):
    pass #todo: implement
