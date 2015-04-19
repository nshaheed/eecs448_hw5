
# classify.py
# Andrei Elliott 2015/04/19
# EECS 448 HW5
# 

# Euclidean distance between two vectors
def euclidVec(v1, v2):
    if length(v1) != length(v2):
        except ValueError("Input vectors must have the same length: ", v1, v2)
    return sqrt(reduce((lambda x,y: x + y), 0, [(v2[i] - v1[i])^2 for i in range(length(v1))]))

def euclid(v, stats):
    pass # return euclidVec(v, stats.mean)

# calculate Mahalanobis distance of v from distribution with given stats
# type/format for stats TBD
def mahalanobis(v, stats):
    pass #todo: implement

# classifies based on distance in all dimensions
# method should be :: v -> stats -> Bool, e.g. euclid, mahalanobis
def directClassify(v, statsActive, statsInactive, method):
    pass #todo: implement

# classifies based on voting method: compares dimensions separately and votes
def votingClassify(v, statsActive, statsInactive, method):
    pass #todo: implement

# calculate stats object for given set of vectors
def getStats(vs):
    pass #todo: implement
