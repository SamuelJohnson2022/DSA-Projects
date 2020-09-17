# Collaborators: Samuel Johnson, Nikita Petrenko, Jason Novillo
import sys

numOfSwaps = 0


def merge_sorted(firstArray, secondArray):
    global numOfSwaps
    firstArray.append(sys.maxsize)
    secondArray.append(sys.maxsize)
    finalArray = []

    # Initialize the index values
    firstIndex = 0
    secondIndex = 0

    # Loops through both arrays and add the values in ascending order by comparison
    for num in range(len(firstArray) + len(secondArray) - 2):
        if firstArray[firstIndex] <= secondArray[secondIndex]:
            finalArray.append(firstArray[firstIndex])
            firstIndex += 1
        else:
            finalArray.append(secondArray[secondIndex])
            secondIndex += 1
            if firstArray[firstIndex] != sys.maxsize:
                numOfSwaps += 1
    return finalArray


def merge_sort(anotherArray):
    arrayLength = len(anotherArray)

    # Base case for recursion
    if arrayLength <= 1:
        return anotherArray

    firstHalfArray = merge_sort(anotherArray[:int(arrayLength / 2)])
    secondHalfArray = merge_sort(anotherArray[int(arrayLength / 2):])

    primedArray = merge_sorted(firstHalfArray, secondHalfArray)

    return primedArray


anotherInput = input()
arrayToSort = list(map(int, input().split()))
finalArray = merge_sort(arrayToSort)

print(numOfSwaps)
