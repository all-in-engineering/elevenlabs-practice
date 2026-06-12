
#questions from nimble:
#1. implement function for both getting minimum and sorting a v array, 
#which is when numbers are guaranteed to be equal/descending and then ascending after
#2. implement summing of linkedlists: https://leetcode.com/problems/add-two-numbers/description/


# Getting minimum in varray:
# returns [minimum, index of minimum]

def getMinimum(v_array):

    #1. No elements in array? if length is 0, return none

    if (len(v_array) == 0):
        return [None, None]
    
    #2. Only 1 element in array? covered by 1

    if (len(v_array) == 1):
        return [v_array[0], 0]
    
    for index in range(len(v_array)):
        #3. all ascending? -> if next index is not >= len(array) and element is larger, return current element

        if (index+1 != len(v_array) and v_array[index+1] > v_array[index]):
            return [v_array[index], index]
        else:
            #2. If nextindex not >= len of list and next integer is <= current element, continue
            continue
    
    #1. Edge cases 1) all descending? -> if nextindex >= lenght of array, return last element of array
    return [v_array[len(v_array)-1], len(v_array)-1]


v_array1 = []
v_array2 = [1]
v_array3 = [1, 2]
v_array4 = [2, 1]
v_array5 = [2, 1, 3]

print(getMinimum(v_array1))
print(getMinimum(v_array2))
print(getMinimum(v_array3))
print(getMinimum(v_array4))
print(getMinimum(v_array5))

"""
Main algorithm:
1. Initialize an answerList which is the final answer = []
2. Call getMinimum()
3. If getMinimum returns [None, None], return the answerList
4. Else append the results of 2) to answerList
5. Pop the result at index
6. repeat until getMinimum returns an emptyList

"""

def sortVArray(v_array):
    answerList = []
    while(True):
        minimum = getMinimum(v_array)
        if (minimum[0] == None):
            return answerList
        else:
            answerList.append(minimum[0])
            v_array.pop(minimum[1])

print(sortVArray(v_array1))
print(sortVArray(v_array2))
print(sortVArray(v_array3))
print(sortVArray(v_array4))
print(sortVArray(v_array5))


#2. implement summing of linkedlists: https://leetcode.com/problems/add-two-numbers/description/

"""
Edge Cases:
1. If list A node is none but listB node is valid, perform sum as if it's 0 + value, increment listB and continue
2. If list B node is none but list A node is valid, perform same sum as 1) but reversed


Main Algorithm:
1. Create an empty starting node that is the answerHead
2. Create a currentNode starting off as answerHead
3. Create a carryover variable = 0
2. Take two node values:
3. sum = Sum together + carryover
4. If sum >= 10, create a new node with that sum as value, set it as the next to currentNode, then change currentNode = currentNode.next, change carryover = 1
5. If sum < 10, create new node with sum as value, set it as next to current node, change currentNode = currentNode.next, change carryover = 0
6. Terminate when both listA node = none and listB node value = Non
7. Return answerHead.next
"""

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def sumLinkedList(listA, listB):
    #1. Create an empty starting node that is the answerHead
    answerHead = Node(None, None)
    currentHead = answerHead
    carryOver = 0
    while(True):
        if (listA.value == None and listB.value == None):
            break
        listAvalue = listA.value if listA.value != None else 0
        listBvalue = listB.value if listB.value != None else 0
        sum = listAvalue + listBvalue + carryOver

        if (sum >= 10):
            newNode = Node(sum % 10, None)
            carryOver = 1
        else:
            newNode = Node(sum, None)
            carryOver = 0

        currentHead.next = newNode
        currentHead = newNode

        if listA.value != None:
            listA = listA.next
        if listB.value != None:
            listB = listB.next
    
    if carryOver == 1:
        currentHead.next = Node(1, None)

    return answerHead.next




def numberToLinkedList(n):
    digits = [int(d) for d in str(n)]
    digits.reverse()  # LSB first
    head = Node(digits[0], None)
    current = head
    for d in digits[1:]:
        node = Node(d, None)
        current.next = node
        current = node
    current.next = Node(None, None)
    return head

def emptyLinkedList():
    return Node(None, None)

def linkedListToList(node):
    result = []
    while node and node.value is not None:
        result.append(node.value)
        node = node.next
    return result

# Test Cases:
# 1) ListA = [], ListB = []
# 2) ListA = [1], ListB = []
# 3) ListA = [], ListB = [1]
# 4) ListA = [9], ListB = [9]
# 5) ListA = [9], ListB = [999]
# 6) ListA = [999], ListB = [9]
# 7) ListA = [11], ListB = [11]
# 8) ListA = [9119], ListB = [9119]

tests = [
    (emptyLinkedList(), emptyLinkedList(), []),
    (numberToLinkedList(1), emptyLinkedList(), [1]),
    (emptyLinkedList(), numberToLinkedList(1), [1]),
    (numberToLinkedList(9), numberToLinkedList(9), [8, 1]),
    (numberToLinkedList(9), numberToLinkedList(999), [8, 0, 0, 1]),
    (numberToLinkedList(999), numberToLinkedList(9), [8, 0, 0, 1]),
    (numberToLinkedList(11), numberToLinkedList(11), [2, 2]),
    (numberToLinkedList(9119), numberToLinkedList(9119), [8, 3, 2, 8, 1]),
]

for i, (listA, listB, expected) in enumerate(tests, 1):
    result = linkedListToList(sumLinkedList(listA, listB))
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {i}: {status} | got {result}, expected {expected}")