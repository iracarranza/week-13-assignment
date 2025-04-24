def findMaxInList(numList):
    numList.sort(reverse = True)
    return numList[0]

exampleList = [1, 1.1, 1.2, 1.3, 14, 1.5]
print(findMaxInList(exampleList))