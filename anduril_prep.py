# Anduril Interview Prep

# Problem: Max Profit from Cutting Rods into Equal Sale Length
# You are given a list of rod lengths lengths. You may choose an integer saleLength (saleLength >= 1)
# and cut rods into smaller pieces of length saleLength to sell.
#
# Each cut costs costPerCut.
# Each produced piece of length saleLength earns revenue saleLength * salePrice.
# For an original rod of length L:
#   You can obtain k = floor(L / saleLength) sellable pieces.
#   The leftover L % saleLength is discarded and yields no revenue.
#   If k = 0, the rod yields nothing.
#   If L % saleLength == 0 (exactly divisible), producing k pieces requires k - 1 cuts.
#   Otherwise, producing k pieces requires k cuts.
# You may discard any rod entirely if using it would reduce total profit.
# Choose saleLength to maximize total profit:
#
#   total profit = total revenue − total cutting cost
#
# Implement:
#   def maxProfit(costPerCut: int, salePrice: int, lengths: list[int]) -> int:
#       """Return the maximum achievable profit."""
#
# Constraints (reasonable interview assumptions)
#   1 <= len(lengths) <= 2e5
#   1 <= lengths[i] <= 1e5 (or larger; justify complexity)
#   0 <= costPerCut <= 1e9
#   1 <= salePrice <= 1e9
#
# Sample Tests
#   costPerCut=1,   salePrice=10, lengths=[5]         → 50
#   costPerCut=2,   salePrice=1,  lengths=[4,4,4]     → 12
#   costPerCut=100, salePrice=1,  lengths=[10,20]     → 20
#   costPerCut=1,   salePrice=2,  lengths=[1,2,3,4,5] → 20


def maxProfit(costPerCut: int, salePrice: int, lengths: list[int]):
    maxLength = getMaxLength(lengths)
    currentMaxProfit = 0
    for saleLength in range(1, maxLength + 1):
        maxProfit = maxProfitHelper(costPerCut, salePrice, lengths, saleLength)
        if maxProfit > currentMaxProfit:
            currentMaxProfit = maxProfit
    return currentMaxProfit

def maxProfitHelper(costPerCut, salePrice, lengths, saleLength):
    profitSoFar = 0
    lengthsList = list(lengths)
    while len(lengthsList) != 0:
        currentLength = lengthsList[0]
        print("current length is: " + str(currentLength))        
        print("current salelength is: " + str(saleLength))
        if (currentLength == 0):
            lengthsList.pop(0)
            continue
        if (currentLength == saleLength):
            estimatedProfit = saleLength * salePrice
            profitSoFar += estimatedProfit
            lengthsList.pop(0)
            continue
        if (currentLength < saleLength):
            print ("skipping")
            lengthsList.pop(0)
            continue
        else:
            print(" valid length")
            estimatedProfit = (saleLength * salePrice) - costPerCut
            print("estimated profit = " + str(estimatedProfit))

            if (estimatedProfit < 0):
                lengthsList.pop(0)
                continue
            else:
                profitSoFar += estimatedProfit
                print("profitFarsofar = " + str(profitSoFar))
                lengthsList[0] = currentLength - saleLength
                continue
    return profitSoFar
                

def getMaxLength(lengths):
    currentMax = 0
    for length in lengths:
        if length > currentMax:
            currentMax = length
    return currentMax
