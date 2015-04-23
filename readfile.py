# functions build for reading hw5db1.txt & hw5db2.txt and returning their elements as [[]]

# reading hw5db1.txt
def readFile(fileVal):
    elements = []
    counter = 0;
    for line in fileVal:
        x = line.split()[3:19]  
        elements.insert(counter, x)
        counter  = counter + 1
    return elements

# reading hw5db2.txt
def readStats(fileVal):
    elements = []
    counter = 0;
    for line in fileVal:
        x = line.split()  
        elements.insert(counter, x)
        counter  = counter + 1
    return elements

#file1 = open("hw5db1.txt","r")
#array = readFile(file1)
