# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262
stringInput = input()


def findLongestPalindrome(stringInput):
    strLength = len(stringInput)

    # 2d table for our DP algorithm size of the input length squared
    flp = [[0]*strLength for i in range(strLength)]
    # Since we have O(n^2) rutime, we will iterate through the string for each possible length

    # Iterate through strings of length 1 which are all palindromes
    for i in range(strLength):
        flp[i][i] = 1

    # Iterate through for all subsequences to fill the table
    for sub in range(2, strLength + 1):
        for start in range(strLength - sub + 1):
            # Find the corresponding charater on the other side we need to check
            end = start + sub - 1

            if stringInput[start] == stringInput[end] and sub == 2:
                # fill the table for subsequences of length 2
                flp[start][end] = sub
            elif stringInput[start] == stringInput[end]:
                # Case where we can continue the subsequence and add 2 more to the length
                flp[start][end] = flp[start + 1][end - 1] + 2
            else:
                # Recursive case to determine the longest length
                flp[start][end] = max(flp[start][end - 1], flp[start + 1][end])

    # we return the last item in the first row of the dp table as the longest palindrome
    return flp[0][strLength - 1]


print(findLongestPalindrome(stringInput))
