
# classify.py
# Andrei Elliott 2015/04/19
# EECS 448 HW5
# 

# Euclidean distance between two vectors
def euclid(v1, v2):
    if length(v1) != length(v2):
        except ValueError("Input vectors must have the same length: ", v1, v2)
    return sqrt(reduce((lambda x,y: x + y), 0, [(v2[i] - v1[i])^2 for i in range(length(v1))]))

# calculate Mahalanobis distance of v from distribution with given stats
# type/format for stats TBD
def mahalanobi(v, stats):
    
