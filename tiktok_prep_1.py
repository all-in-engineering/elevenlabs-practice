# Problem: Longest Subarray of Consecutive 1s (Sliding Window)
#
# Given a binary array nums (containing only 0s and 1s), return the maximum
# length of a subarray of consecutive 1s after flipping at most k zeros to ones.
# If k = 0, no flipping is allowed (pure longest consecutive ones).
#
# Input:
#   n k       <- n: length of array, k: max zeros allowed to flip
#   nums      <- n integers, each 0 or 1
#
# Output:
#   One integer: the maximum length of consecutive 1s
#
# Constraints:
#   1 <= n <= 2 * 10^5
#   0 <= k <= n
#   nums[i] in {0, 1}
#
# Examples:
#   n=7, k=1, nums=[1,1,0,1,1,1,0]  -> 6
#   n=5, k=0, nums=[1,1,0,1,1]      -> 2
#   n=6, k=2, nums=[0,0,1,1,0,1]    -> 5
#   n=1, k=0, nums=[0]              -> 0
#   n=8, k=3, nums=[1,0,1,0,1,0,1,0] -> 7

#0. Initialize a variable to keep track of the longest substring we've found so far at 0
#1. call a helperfunction flipArrayHelper(k, array, startingIndex = 0)
#2. if k = 0, do a count of the longest substring of 1's and iterate, and return the longest one and compare to the longest substringtracker at the beginning. If it's larger replace it.
#3. else find the next 0 starting at starting index. create a copy of array, flip that index to 1, then call helperfunction(k-1, arrayCopy, startingIndexNew Function again)
#4. return the variable in 1


def flipArray(k, array):
    return flipArrayHelper(k, array, 0)

def flipArrayHelper(k, array, startingIndex):
    if startingIndex >= len(array):
        return 0
     
    if (k == 0):
        longestSubstring = countLongestSubstring(array)
        return longestSubstring
    
    nextFlipIndex = getNextFlipIndex(array, startingIndex+1)
    if (nextFlipIndex >= len(array)):
        return 0
    
    arrayCopy = list(array)
    arrayCopy[nextFlipIndex] = 1
    arrayIfIFlip = flipArrayHelper(k-1, arrayCopy, nextFlipIndex + 1)
    arrayIfNoFlip = flipArrayHelper(k, list(array), nextFlipIndex + 1)

    if arrayIfIFlip > arrayIfNoFlip:
        return arrayIfIFlip
    else:
        return arrayIfNoFlip
    
def countLongestSubstring(array):
    longestSubStringSoFar = 0
    inSubString = False
    currentCount = 0

    for index in range(len(array)):
        if not inSubString:
            if array[index] == 1:
                inSubString = True
                currentCount += 1
                continue
            else:
                continue
        else:
            if array[index] == 1:
                currentCount += 1
                continue
            else:
                inSubString = False
                if currentCount > longestSubStringSoFar:
                    longestSubStringSoFar = currentCount
                    currentCount = 0
                    continue
    
    if currentCount > longestSubStringSoFar:
        return currentCount
    return longestSubStringSoFar

def getNextFlipIndex(array, startingIndex):
    currentIndex = startingIndex
    for oneIndex in range(startingIndex, len(array)):
        if array[oneIndex] == 0:
            return oneIndex
        else:
            currentIndex += 1
    return len(array)