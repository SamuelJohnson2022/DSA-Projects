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


def upper_envelope(xList, yList):

    lowerHalfCH = []
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
        while len(stackX) > 0:

    return upperHalfNum, lowerHalfNum


def merge_sorted(firstXArray, secondXArray, firstYArray, secondYArray, pStarX, pStarY):
    firstXArray.append(sys.maxsize)
    secondXArray.append(sys.maxsize)
    firstYArray.append(sys.maxsize)
    secondYArray.append(sys.maxsize)

    finalXArray = []
    finalYArray = []

    # Initialize the index values
    firstIndex = 0
    secondIndex = 0

    # Loops through both arrays and add the values in ascending order by comparison
    for i in range(len(firstXArray) + len(secondXArray) - 2):
        if firstYArray[firstIndex] == pStarY and firstXArray[firstIndex] == pStarX:
            finalXArray.append(firstXArray[firstIndex])
            finalYArray.append(firstYArray[firstIndex])
            firstIndex += 1
        elif secondYArray[secondIndex] == pStarY and secondXArray[secondIndex] == pStarX:
            finalXArray.append(secondXArray[secondIndex])
            finalYArray.append(secondYArray[secondIndex])
            secondIndex += 1

        firstAngle = math.atan(
            (firstYArray[firstIndex] - pStarY)/(firstXArray[firstIndex] - pStarX))
        secondAngle = math.atan(
            (secondYArray[secondIndex] - pStarY)/(secondXArray[secondIndex] - pStarX))

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
    bList.append(abPair[1])

print()
