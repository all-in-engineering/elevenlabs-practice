# Given a formatted file name string containing braces, such as {a,b}{c,d}.txt,
# generate all possible file name combinations, like ac.txt, ad.txt, bc.txt, bd.txt.
# Write a function to achieve this.
#
# Input
# A formatted file name string, e.g., {a,b}{c,d}.txt
# Output
# A list of strings containing all possible file names.
# Constraints
# The length of the input string does not exceed 100.
# Each pair of braces contains at most 10 items.
# Example
# Input
# {a,b}{c,d}.txt
#
# Output
# ['ac.txt', 'ad.txt', 'bc.txt', 'bd.txt']


def computeFileNames(groupList):
    if (len(groupList) == 1):
        for oneString in groupList[0]:
            print(oneString)
        return
    for oneString in groupList[0]:
        computeFileNamesHelper(oneString, groupList[1], groupList[2:])


def computeFileNamesHelper(prependString, currentGroup, remainingGroup):
    if len(remainingGroup) == 0:
        for oneString in currentGroup:
            print(prependString + oneString + ".txt")
        return
    for oneString in currentGroup:
        computeFileNamesHelper(prependString + oneString, remainingGroup[0], remainingGroup[1:])


print("--- 2 groups: {a,b}{c,d} ---")
computeFileNames([["a", "b"], ["c", "d"]])

print("\n--- 3 groups: {a,b}{c,d}{e,f} ---")
computeFileNames([["a", "b"], ["c", "d"], ["e", "f"]])

print("\n--- 1 group: {x,y,z} ---")
computeFileNames([["x", "y", "z"]])


class Node:

    def __init__(self, value, childrenList):
        self.value = value
        self.childrenList = childrenList


def traverseBFS(self):
    return traverseBFSHelper([self])

def traverseBFSHelper(futureProcessingList):
    if len(futureProcessingList) == 0:
        return
    print(futureProcessingList[0].value)
    currentNode = futureProcessingList.pop(0)
    for child in currentNode.childrenList:
        futureProcessingList.append(child)
    return traverseBFSHelper(futureProcessingList)


print("\n--- BFS Traversal Test ---")
# Tree:
#     1
#    / \
#   2   3
#  / \
# 4   5
node4 = Node(4, [])
node5 = Node(5, [])
node2 = Node(2, [node4, node5])
node3 = Node(3, [])
node1 = Node(1, [node2, node3])
print("Expected: 1, 2, 3, 4, 5")
print("Got:")
traverseBFS(node1)

import math

def inCircle(point, center, radius):
    distanceFromCenter = math.sqrt((point[0] - center[0]) * (point[0] - center[0]) + (point[1] - center[1]) * (point[1] - center[1]))
    if distanceFromCenter <= radius:
        return True
    else:
        return False


print("\n--- inCircle Tests ---")
# point inside circle
print("(1,1) in circle centered (0,0) r=2:", inCircle((1, 1), (0, 0), 2))    # True
# point outside circle
print("(3,3) in circle centered (0,0) r=2:", inCircle((3, 3), (0, 0), 2))    # False
# point exactly on the boundary
print("(2,0) in circle centered (0,0) r=2:", inCircle((2, 0), (0, 0), 2))    # True
# circle not at origin
print("(5,5) in circle centered (4,4) r=2:", inCircle((5, 5), (4, 4), 2))    # True