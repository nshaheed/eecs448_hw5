def readFile(fileVal):
    elements = []
    counter = 0;
    for line in fileVal:
        x = line.split()[3:18]  
        elements.insert(counter, x)
        counter  = counter + 1
    return elements


# file1 = open("hw5db1.txt","r")

# array = readFile(file1)
