#function for mean
def mean(listOfNum):
    total = 0
    for num in listOfNum:
        total = total + num
    return total/len(listOfNum)
# function for mode
def mode(listOfNum):
    maxCount = (0,0)
    for num in listOfNum:
        occurences = listOfNum.count(num)
        if occurences>maxCount[0]:
            maxCount =(occurences, num)
    return maxCount[1]

#function for median
def median(listOfNum):
    listOfNum.sort()
    if (len(listOfNum)%2 !=0):
        middleIndex = int((len(listOfNum)-1)/2)
        return listOfNum[middleIndex]
    elif len(listOfNum)%2 ==0:
        middleIndex1 = int(len(listOfNum)/2)
        middleIndex2 = int((len(listOfNum)/2)-1)
        return mean([listOfNum[middleIndex1], listOfNum[middleIndex2]])


print(mean([13,13,13,13,14,14,16,18]))
print(mode([13,13,13,13,14,14,16,18]))
print(median([13,13,13,13,14,14,16,18]))