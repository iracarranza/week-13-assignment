# i forgot it was no methods

def findMaxInList(numList):
    numList.sort(reverse = True)
    return numList[0]

exampleList = [1, 1.1, 1.2, 1.3, 14, 1.5]
print(findMaxInList(exampleList))

###

def findMaxInList2(numbers):
    maxValue = numbers[0]
    for eachNum in numbers:
        if eachNum > maxValue:
            maxValue = eachNum
    return maxValue

exList2 = [-10, -11, 59, -60, 100]
print (findMaxInList2(exList2))
