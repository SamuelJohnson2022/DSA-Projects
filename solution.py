import sys

# Take the two input arrays and saves them to a and b respectively
firstArray = input().split()
secondArray = input().split()
firstArray.append(sys.maxsize)
secondArray.append(sys.maxsize)
finalArray = []

# Initialize the index values
firstIndex = 1
secondIndex = 1
twoIndex = 0

# Loops through both arrays and add the values in ascending order by comparison
for twoIndex in range(len(firstArray) + len(secondArray) - 4):
    if firstArray[firstIndex] <= secondArray[secondIndex]:
        finalArray.append(firstArray[firstIndex])
        firstIndex += 1
    else:
        finalArray.append(secondArray[secondIndex])
        secondIndex += 1

print(finalArray)