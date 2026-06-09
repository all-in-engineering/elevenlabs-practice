# Anduril Interview Prep 4
#
# Given two lists vecA and vecB, and a rank(a, b) function that returns a rank value
# for a pair (a, b), find a set of pairs that maximizes the total sum of their ranks.
#
# Constraints:
#   - Each element of vecA can be used at most once across all pairs.
#   - Each element of vecB can be used at most once across all pairs.
#   - If multiple optimal solutions exist, returning any one is fine.
#
# Signature (C++ equivalent in Python):
#   def highest_rank_sum_pairs(vecA, vecB) -> list of (a, b) pairs


def highest_rank_sum_pairs(vectorA, vectorB):
    return highest_rank_helper(vectorA, vectorB, 0, 0)


def highest_rank_helper(vectorA, vectorB, sumSoFar, highestSumSeen):
    highestSum = highestSumSeen
    sum = sumSoFar
    
    if (len(vectorA) == 0 or len(vectorB) == 0):
        if (sumSoFar > highestSumSeen):
            return sumSoFar
        else:
            return highestSumSeen
    
    for indexA in range(len(vectorA)):
        vectorACopy = list(vectorA)
        currentANumber = vectorA[indexA]
        vectorACopy.pop(indexA)
        for indexB in range(len(vectorB)):
            vectorBCopy = list(vectorB)
            currentBNumber = vectorB[indexB]
            vectorBCopy.pop(indexB)
            oneSum = highest_rank_helper(vectorACopy, vectorBCopy, sum + (currentANumber * currentBNumber), highestSum)
            if (oneSum > highestSum):
                highestSum = oneSum
    return highestSum