import math
import readfile
import vector_handler
import classifier
file1 = open("hw5db1.txt","r")
file2 = open("hw5db2.txt","r")
dataIn = readfile.readFile(file1)
stats = readfile.readStats(file2)

vectors = vector_handler.vector_holder(dataIn,stats)
classifier = classifier.classifier()


result1 = classifier.directClassify(vectors.vectorArr,vectors.statArr,classifier.method_1)
result2 = classifier.directClassify(vectors.vectorArr,vectors.statArr,classifier.method_2)

for i in range(0,15):
    if result1[i]:
        print('A')
    else:
        print('N')
