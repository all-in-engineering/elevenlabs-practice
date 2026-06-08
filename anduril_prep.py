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


# Problem: Nested Transactional Key-Value Store
#
# Implement an in-memory nested transactional key-value store with the following operations:
#
#   PUT key value  - Set the value of a key.
#   GET key        - Get the value of a key.
#   BEGIN          - Start a new transaction.
#   COMMIT         - Commit all changes in the current transaction.
#   ROLLBACK       - Roll back all changes in the current transaction.
#
# Requirements: Support nested transactions where a transaction can start another
# transaction, and can commit or rollback at any level.
#
# Process these operations, ensuring correct commit and rollback functionality.
#
# Example Input:
#   BEGIN
#   PUT a 10
#   PUT b 3
#   GET a
#   ROLLBACK
#   COMMIT
#
# Output Description:
#   Each command is processed by the implemented method in sequence.
#   Ensure methods can immediately output results when commands are received,
#   especially the GET operation should return the current value right away.

class KVStore:

    def __init__(self):
        self.parent = None   #list of parent kvstores
        self.parentKvstore = {} #official commited kv store of parent
        self.uncommittedKvstore = {} #current KV store's uncommitted kvsstore
        self.currentKvstore = {} #nested (current) kv store's official kvstore
        self.currentTransaction = self

    
    def input(self, command):
        if command == "BEGIN":
            childKVstore = KVStore()
            childKVstore.currentKvstore = dict(self.currentTransaction.uncommittedKvstore)
            childKVstore.uncommittedKvstore = dict(self.currentTransaction.uncommittedKvstore)
            childKVstore.parent = self
            self.currentTransaction = childKVstore
            return
        elif command == "COMMIT":
            if self.currentTransaction is None:
                return
            self.currentTransaction.currentKvstore = self.currentTransaction.uncommittedKvstore
            if self.parent is None:
                return
            self.parent.uncommitedKvstore = self.currentTransaction.currentKvstore
            self.parent.currentTransaction = self.parent
            return
        elif command == "ROLLBACK":
            self.currentTransaction.uncommittedKvstore = dict(self.parentKvstore)
            self.currentTransaction.currentKvstore = dict(self.parentKvstore)
            return
        elif command.split()[0] == "GET":
            return self.currentTransaction.uncommittedKvstore.get(command.split()[1])
        elif command.split()[0] == "PUT":
            self.currentTransaction.uncommittedKvstore[command.split()[1]] = command.split()[2]
            return



print("--- Original Example ---")
store = KVStore()
print("BEGIN:", store.input("BEGIN"))
print("PUT a 10:", store.input("PUT a 10"))
print("PUT b 3:", store.input("PUT b 3"))
print("GET a:", store.input("GET a"))       # expected: 10
print("ROLLBACK:", store.input("ROLLBACK"))
print("COMMIT:", store.input("COMMIT"))

print("\n--- Nested Transaction Test ---")
store2 = KVStore()
print("BEGIN:", store2.input("BEGIN"))
print("PUT a 10:", store2.input("PUT a 10"))
print("BEGIN (inner):", store2.input("BEGIN"))
print("PUT a 20:", store2.input("PUT a 20"))
print("GET a:", store2.input("GET a"))        # expected: 20 (inner sees a=20)
print("COMMIT (inner):", store2.input("COMMIT"))
print("GET a:", store2.input("GET a"))        # expected: 20 (merged into outer)
print("ROLLBACK (outer):", store2.input("ROLLBACK"))
print("GET a:", store2.input("GET a"))        # expected: None (outer rolled back)

print("\n--- Inheritance Test ---")
store3 = KVStore()
print("BEGIN:", store3.input("BEGIN"))
print("PUT a 10:", store3.input("PUT a 10"))
print("BEGIN (inner):", store3.input("BEGIN"))
print("GET a:", store3.input("GET a"))        # expected: 10 (inherited from outer)