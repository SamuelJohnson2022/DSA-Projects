# Collaborators: Samuel Johnson, Nikita Petrenko, Jason Novillo
import sys
import math


def FindSmallestIndex(yList):

    smallestPoint = yList[0]
    smallestPointIndex = 0

    for i in range(len(yList)):
        if yList[i] < smallestPoint:
            smallestPoint = yList[i]
            smallestPointIndex = i

    return smallestPointIndex


def FindLargestIndex(yList):

    largestPoint = yList[0]
    largestPointIndex = 0

    for i in range(len(yList)):
        if yList[i] > largestPoint:
            largestPoint = yList[i]
            largestPointIndex = i

    return largestPointIndex


def IsTurningLeft(pBX, pBY, pAX, pAY, pKX, pKY):  # fLIPPED A AND B AND IT WORKED

    xA = pAX - pBX
    yA = pAY - pBY
    xB = pKX - pAX
    yB = pKY - pAY

    if (xA*yB - xB*yA) >= 0:
        return True
    else:
        return False


def upper_envelope(xList, yList):

    # Find p*
    pStar = FindSmallestIndex(yList)
    pStarX = xList[pStar]
    pStarY = yList[pStar]
    # Sort x and y list in the increasing order of angle with p*
    # math.atan(Y/X)
    sortedXArray, sortedYArray = merge_sort(xList, yList, pStarX, pStarY)

    stackX = []
    stackX.append(sortedXArray[0])
    stackX.append(sortedXArray[1])
    stackX.append(sortedXArray[2])

    stackY = []
    stackY.append(sortedYArray[0])
    stackY.append(sortedYArray[1])
    stackY.append(sortedYArray[2])

    for i in range(3, len(sortedXArray)):
        while len(stackX) > 2:
            pAX = stackX[-1]
            pBX = stackX[-2]
            pAY = stackY[-1]
            pBY = stackY[-2]

            pKX = sortedXArray[i]
            pKY = sortedYArray[i]

            if IsTurningLeft(pAX, pAY, pBX, pBY, pKX, pKY):
                stackX.pop()
                stackY.pop()
            else:
                break
        stackX.append(pKX)
        stackY.append(pKY)

    leftIndex = FindSmallestIndex(stackX)
    leftMostX = stackX[leftIndex]
    leftMostY = stackY[leftIndex]

    rightIndex = FindLargestIndex(stackX)
    rightMostX = stackX[rightIndex]
    rightMostY = stackY[rightIndex]

    upperHalfNum = 0
    lowerHalfNum = 0

    rotateLeftX = stackX[leftIndex:] + stackX[:leftIndex]
    rotateLeftY = stackY[leftIndex:] + stackY[:leftIndex]

    rotateRightX = stackX[rightIndex:] + stackX[:rightIndex]
    rotateRightY = stackY[rightIndex:] + stackY[:rightIndex]

    for i in range(len(stackX)):
        if(rotateLeftX[i] == rightMostX and rotateLeftY[i] == rightMostY):
            upperHalfNum += 1
            break
        else:
            upperHalfNum += 1

    for i in range(len(stackX)):
        if(rotateRightX[i] == leftMostX and rotateRightY[i] == leftMostY):
            lowerHalfNum += 1
            break
        else:
            lowerHalfNum += 1

    return upperHalfNum, lowerHalfNum


def merge_sorted(firstXArray, secondXArray, firstYArray, secondYArray, pStarX, pStarY):

    finalXArray = []
    finalYArray = []

    # Initialize the index values
    firstIndex = 0
    secondIndex = 0

    # Loops through both arrays and add the values in ascending order by comparison
    while((firstIndex + secondIndex) < len(firstXArray) + len(secondXArray)):
        if firstIndex == len(firstXArray):
            finalXArray.append(secondXArray[secondIndex])
            finalYArray.append(secondYArray[secondIndex])
            secondIndex += 1
        elif secondIndex == len(secondXArray):
            finalXArray.append(firstXArray[firstIndex])
            finalYArray.append(firstYArray[firstIndex])
            firstIndex += 1
        elif firstYArray[firstIndex] == pStarY and firstXArray[firstIndex] == pStarX:
            finalXArray.append(firstXArray[firstIndex])
            finalYArray.append(firstYArray[firstIndex])
            firstIndex += 1
        elif secondYArray[secondIndex] == pStarY and secondXArray[secondIndex] == pStarX:
            finalXArray.append(secondXArray[secondIndex])
            finalYArray.append(secondYArray[secondIndex])
            secondIndex += 1
        else:
            firstAngle = math.acos(
                (firstXArray[firstIndex] - pStarX)/math.sqrt((firstXArray[firstIndex] - pStarX)**2 + (firstYArray[firstIndex] - pStarY)**2))
            secondAngle = math.acos(
                (secondXArray[secondIndex] - pStarX)/math.sqrt((secondXArray[secondIndex] - pStarX)**2 + (secondYArray[secondIndex] - pStarY)**2))

            if firstAngle <= secondAngle:
                finalXArray.append(firstXArray[firstIndex])
                finalYArray.append(firstYArray[firstIndex])
                firstIndex += 1
            else:
                finalXArray.append(secondXArray[secondIndex])
                finalYArray.append(secondYArray[secondIndex])
                secondIndex += 1
    return finalXArray, finalYArray


def merge_sort(xArray, yArray, pStarX, pStarY):
    arrayLength = len(xArray)

    # Base case for recursion
    if arrayLength <= 1:
        return xArray, yArray

    firstHalfXArray, firstHalfYArray = merge_sort(
        xArray[:int(arrayLength / 2)], yArray[:int(arrayLength / 2)], pStarX, pStarY)
    secondHalfXArray, secondHalfYArray = merge_sort(
        xArray[int(arrayLength / 2):], yArray[int(arrayLength / 2):], pStarX, pStarY)

    primedXArray, primedYArray = merge_sorted(
        firstHalfXArray, secondHalfXArray, firstHalfYArray, secondHalfYArray, pStarX, pStarY)

    return primedXArray, primedYArray


aList = []
bList = []

numOfLines = int(input())
for i in range(numOfLines):
    abPair = list(map(float, input().split()))
    aList.append(abPair[0])
    bList.append(abPair[1]*(-1))

upperHalfNum, lowerHalfNum = upper_envelope(aList, bList)

print(str(upperHalfNum) + " " + str(lowerHalfNum))
