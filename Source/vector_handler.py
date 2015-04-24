
class vector_holder (object):
    def __init__(self,vectors_in,stats_in):
        self.vectorArr = []
        self.statArr = []
        for i in range(0,43347):
            self.vectorArr.append(vector_obj(vectors_in[i]))
        for i in range(0,len(stats_in)):
            self.statArr.append(vector_obj(stats_in[i]))

    def getVectorFromIndx(self,indx):
        return self.vectorArr[indx].vector_data

    def setVectorFromIndx(self,indx,x):
        self.vectorArr[indx].vector_data = x

    def getVectorHolderLen(self):
        return len(self.vectorArr)

    def addVectorObj(self,vector):
        self.vectorArr.append(vector)
            
    def addStatsObj(self,stats):
        self.vectorArr.append(stats)

    def getActiveMean(self):
        return self.statArr[0].vector_data

    def getNonActiveMean(self):
        return self.statArr[1].vector_data

    def getActiveStd(self):
        return self.statArr[2].vector_data

    def getNonActiveStd(self):
        return self.statArr[3].vector_data
        
    def getActiveFromIndx(self,indx):
        return self.vectorArr[indx].active

class vector_obj (object):#I had plans for this but they were redundant. Right now it just holds the list. For some reason moving lists of lists was being weird
    def __init__(self,vector_data = []):
        self.vector_data = vector_data
    

