import math

class classifier(object):
    
    # Euclidian distance method
    def method_1(self,v1,statA,statStd):
        if len(v1) != len(statA):
            raise ValueError("Input vectors must have the same length: ", v1, statA)
        return math.sqrt(sum([(float(statA[i]) - float(v1[i]))**2 for i in range(len(v1))]))
                
    # Mahalanobis distance method
    def method_2(self,v1,statA,statStd):
        if len(v1) != len(statA):
            raise ValueError("Input vectors must have the same length: ", v1, statA)
        return math.sqrt(sum([((float(statA[i]) - float(v1[i]))/float(statStd[i]))**2 for i in range(len(v1))]))

    # Euclidian voting method
    def method_3(self,v1,stats):
        self.Active=0
        self.N_Active=0
        for i in range(0,len(v1)):
            if math.sqrt((float(v1[i])-float(stats[0].vector_data[i]))**2) < math.sqrt((float(v1[i])-float(stats[1].vector_data[i]))**2):#this is biased toward N_Active in the event of a tie
                self.Active = self.Active+1
            else:
                self.N_Active = self.N_Active+1
        return self.Active > self.N_Active

    # Mahalanobis distance method
    def method_4(self,v1,stats):
        self.Active=0
        self.N_Active=0
        for i in range(0,len(v1)):
            if math.sqrt(((float(v1[i])-float(stats[0].vector_data[i]))/float(stats[2].vector_data[i]))**2) < math.sqrt(((float(v1[i])-float(stats[1].vector_data[i]))/float(stats[3].vector_data[i]))**2):#this is biased toward N_Active in the event of a tie
                self.Active = self.Active+1
            else:
                self.N_Active = self.N_Active+1
        return self.Active > self.N_Active
    
    #recieves a list of vectors, the list of mean std vectors, and a method to send them too. Gives back a string of
    #  ANANANNANNANANA in order of chemicals. A = active N = Not Active
    def directClassify(self,vector,stats,method):
        self.A_N_Vector = []
        for i in range(0,len(vector)):
            self.A_N_Vector.append(method(vector[i].vector_data, stats[0].vector_data,stats[2].vector_data) < method(vector[i].vector_data,stats[1].vector_data,stats[3].vector_data))
        return self.A_N_Vector

    #recieves a list of vectors, the list of mean std vectors, and a method to send them too. Gives back a string of
    # ANANANNANNANANA in order of chemicals. A = active N = Not Active
    def votingClassify(self,vector,stats,method):
        self.A_N_Vector = []
        for i in range(0,len(vector)):
            self.A_N_Vector.append(method(vector[i].vector_data, stats))
        return self.A_N_Vector

    # custom classification method based off of the given four.  Assume True = Active, False = NonActive
    #    currently: A simple majority vote
    def customClassify(euclid, mahal, euclidVote, mahalVote):
        lst = [euclid, mahal, euclidVote, mahalVote]
        numTrue = len([i for i in lst if i])
        if numTrue >= 2:
            return True
        else:
            return False
