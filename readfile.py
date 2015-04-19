def readFile(fileVal):
    elements = []
    counter = 0;
    for line in fileVal:
        elements.insert(counter, line.split(','))
        counter  counter + 1
    return elements
