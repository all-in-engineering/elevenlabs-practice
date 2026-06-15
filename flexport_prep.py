# Flexport Interview Prep

'''
Problem: House Robber I

You are a professional robber planning to rob houses along a street. Each house
contains some amount of money, represented by the array nums.

Adjacent houses have connected security systems. If two adjacent houses are robbed
on the same night, the alarm will be triggered.

Return the maximum amount of money you can rob without triggering the alarm.

Input:
    - First line: integer n, the number of houses
    - Second line: n non-negative integers representing nums

Output:
    - One integer, the maximum amount of money that can be robbed

Constraints:
    - 1 <= n <= 10^5
    - 0 <= nums[i] <= 10^9

Example:
    Input:
        4
        1 2 3 1
    Output:
        4
    Explanation: Rob the 1st and 3rd houses for a total of 1 + 3 = 4.
'''

"""
Test Cases:
1 2 3 1 -> 4

1 3 2 1 -> 4

2 1 1 2 -> 4

1 5 1 2 4

Edge Cases:
1) If array size is just 1 return that value
2) If array size is 2, return the larger of the two values
3) If array size > 3, use main algorithm


Main Algorithm:

1. Calculate how much could be made if:
2. We included the first value in the array + robHouses(moneyPerhouse starting at index + 2 )
3. We don't include the first value in the array = robhouses(moneyPerHouse[1:])
4. Whichever one is bigger return that


"""

def robhouses(numHouses, moneyPerHouse):
    return robHousesHelper(moneyPerHouse, 0, {}, numHouses)[0]

#memoizedDictionary is O(N) because when we've computed optimal value starting at an index, we just keep looking it up, and there are N positions to calculate

def robHousesHelper(moneyPerHouse, memoizedDictionary, originalLength):
    if originalLength - len(moneyPerHouse) in memoizedDictionary:
        return [memoizedDictionary[originalLength - len(moneyPerHouse)], memoizedDictionary]
    if (len(moneyPerHouse) == 0):
        memoizedDictionary[originalLength - len(moneyPerHouse)] = sumSoFar
        return [sumSoFar, memoizedDictionary]
    if (len(moneyPerHouse) == 1):
        memoizedDictionary[originalLength - len(moneyPerHouse)] = sumSoFar + moneyPerHouse[0]
        return [sumSoFar + moneyPerHouse[0], memoizedDictionary]
    if (len(moneyPerHouse) == 2):
        largerSum = moneyPerHouse[1] if moneyPerHouse[1] > moneyPerHouse[0] else moneyPerHouse[0]
        memoizedDictionary[originalLength - len(moneyPerHouse)] = largerSum + sumSoFar
        return [largerSum + sumSoFar, memoizedDictionary]

    #For the case where we use the first value:
    includeFirstValue = robHousesHelper(moneyPerHouse[2:], moneyPerHouse[0] + sumSoFar, memoizedDictionary, originalLength)
    skipFirstValue = robHousesHelper(moneyPerHouse[1:], sumSoFar, memoizedDictionary, originalLength)

    if includeFirstValue[0] > skipFirstValue[0]:
        memoizedDictionary[originalLength - len(moneyPerHouse)] = includeFirstValue[0]
        return [includeFirstValue[0], memoizedDictionary]
    else:
        memoizedDictionary[originalLength - len(moneyPerHouse) + 1] = skipFirstValue[0]
        return [skipFirstValue[0], memoizedDictionary]


'''
Problem: House Robber III

The robber has found a new neighborhood. There is only one entrance to this area,
called root.

Except for the entrance, each house has exactly one parent house connected to it.
All houses form a binary tree.

If two directly connected houses are robbed on the same night, the alarm will be
triggered.

Given the root of the binary tree, return the maximum amount of money the robber
can rob without triggering the alarm.

Input:
    - One line representing the level-order traversal of the binary tree
    - Null nodes are represented by null

Output:
    - One integer, the maximum amount of money that can be robbed

Constraints:
    - 0 <= n <= 10^4
    - 0 <= Node.val <= 10^9

Example:
    Input:
        3 2 3 null 3 null 1
    Output:
        7
    Explanation: Rob root (3), right child of left subtree (3), and right child
                 of right subtree (1), for a total of 3 + 3 + 1 = 7.
'''

def robTree(treeList):
    head = convertToTree(treeList)
    return robTreeNode(head, 0)

    
def robTreeNode(head, sumSoFar):
    if head == None:
        return sumSoFar
    if head != None and head.left == None and head.right == None:
        return sumSoFar + head.value
    
    robGrandChildren = head.value

    if (head.left != None):
        if head.left.left != None:
            robGrandChildren += robTreeNode(head.left.left, sumSoFar)
        if head.left.right != None:
            robGrandChildren += robTreeNode(head.left.right, sumSoFar)
    if (head.right != None):
        if head.right.right != None:
            robGrandChildren += robTreeNode(head.right.right, sumSoFar)
        if head.right.left != None:
            robGrandChildren += robTreeNode(head.right.left, sumSoFar)

    onlyRobChildren = 0

    if (head.left != None):
        onlyRobChildren += robTreeNode(head.left, sumSoFar)
    if (head.right != None):
        onlyRobChildren += robTreeNode(head.right, sumSoFar)

    if robGrandChildren > onlyRobChildren:
        return robGrandChildren
    else:
        return onlyRobChildren
        

class Node:
    def __init__(self, value):
       
        self.value = value
        self.left = None
        self.right = None


def convertToTree(treeList):
    if len(treeList) == 0:
        return None
    if len(treeList) == 1:
        return Node(treeList[0])
    
    head = Node(treeList[0])

    treeList.pop(0)

    nodesToAddChildrenTo = []

    if (len(treeList) > 0):
        if treeList[0] != None:
            leftChild = Node(treeList.pop(0))
            head.left = leftChild
            nodesToAddChildrenTo.append(leftChild)
        else:
            head.left = treeList.pop(0) #None
            nodesToAddChildrenTo.append(leftChild)
    
    if (len(treeList) > 0):
        if treeList[0] != None:
            rightChild = Node(treeList.pop(0))
            head.right = rightChild
            nodesToAddChildrenTo.append(rightChild)
        else:
            head.right = treeList.pop(0) #None
            nodesToAddChildrenTo.append(rightChild)

    while (len(treeList) != 0):
        currentHead = nodesToAddChildrenTo[0]
        leftChild = treeList.pop(0)
        rightChild = treeList.pop(0)

        if leftChild != None:
            leftChild = Node(leftChild)
        if rightChild != None:
            rightChild = Node(rightChild)

        if currentHead == None:
            nodesToAddChildrenTo.pop(0)
            continue
        else:
            currentHead.left = leftChild
            currentHead.right = rightChild
            nodesToAddChildrenTo.append(currentHead.left)
            nodesToAddChildrenTo.append(currentHead.right)
            nodesToAddChildrenTo.pop(0)

    return head
