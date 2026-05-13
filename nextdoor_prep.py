# ============================================================
# Problem: Compare Version Numbers
#
# Given two version strings version1 and version2, each consisting
# of one or more numeric revisions separated by dots '.', compare them.
#
# Return:
#    1 if version1 > version2
#   -1 if version1 < version2
#    0 if version1 == version2
#
# Notes:
#   - Revisions are compared numerically (not lexicographically)
#   - Leading zeros are ignored: "1.01" == "1.001" == "1.1"
#   - Missing revisions are treated as 0: "1.0" == "1.0.0"
#   - Version strings support any number of segments
#
# Examples:
#   version1 = "1.0.1", version2 = "1"       => 1
#   version1 = "7.5.2.4", version2 = "7.5.3" => -1
#   version1 = "1.01", version2 = "1.001"    => 0
#   version1 = "1.0", version2 = "1.0.0"     => 0
# ============================================================

def compareVersions(version1, version2):
    splitVersion1 = version1.split(".")
    splitVersion2 = version2.split(".")

    while (True):
        if (len(splitVersion1) == 0 and len(splitVersion2) == 0):
            return 0
        elif (len(splitVersion1) == 0):
            version2 = splitVersion2.pop(0)
            if version2 == "0":
                continue
            else: 
                return -1
        
        elif (len(splitVersion2) == 0):
            version1 = splitVersion1.pop(0)
            if version1 == "0":
                continue
            else: 
                return 1
     
        else: 
            currentVersion1 = int(splitVersion1[0])
            currentVersion2 = int(splitVersion2[0])
            if currentVersion1 > currentVersion2:
                return 1
            elif currentVersion1 < currentVersion2:
                return -1
            splitVersion1.pop(0)
            splitVersion2.pop(0)

print(compareVersions("1.0.1", "1" ))
print(compareVersions("7.5.2.4", "7.5.3" ))
print(compareVersions("1.01", "1.001" ))
print(compareVersions("1.0", "1.0.0" ))


# ============================================================
# Problem: Comment Tree
#
# Given a list of comments, each with an id and a parentId,
# build and print the comment tree structure.
#
# Print format:
#   - Each "level" of depth is printed on its own line.
#   - Siblings at the same level are comma-separated, sorted by id ascending.
#
# Constraints:
#   - Each comment has at most one parent (or no parent — root comment).
#   - There may be multiple root comments.
#   - Children of the same parent are sorted by id ascending.
#
# Comment class:
#   class Comment:
#       def __init__(self, id, parentId):
#           self.id = id
#           self.parentId = parentId
#
# Example:
#   comments = [
#       Comment(1, None),
#       Comment(2, 1),
#       Comment(3, None),
#       Comment(4, 2),
#       Comment(5, 2)
#   ]
#
#   Output:
#     1
#     2
#     4,5
#     3
#
#   Explanation:
#     - 1 and 3 are root comments (no parent)
#     - 2 is a child of 1
#     - 4 and 5 are children of 2
#     - Print DFS order: root 1, then its subtree (2, then 4,5), then root 3
# ============================================================


class Comment:
    def __init__(self, id, parentId):
        self.id = id
        self.parentId = parentId

class Head:
    def __init__(self, headValue, childrenList):
        self.headValue = headValue
        self.childrenList = childrenList

def printTree(commentList):
    treeHeadList = []
    for comment in commentList:
        if comment.parentId is None:
            newHead = constructTree(comment, commentList)
            treeHeadList.append(newHead)

    for tree in treeHeadList:
        print(tree.headValue)
        printTreeHelper(tree)


def constructTree(parent, commentList):
    parentId = parent.id
    childrenList = []
    for comment in commentList:
        if comment.parentId == parent.id:
            child = constructTree(comment, commentList)
            childrenList.append(child)    
    parentNode = Head(parentId, childrenList)
    return parentNode

def printTreeHelper(head):
    childrenList = ""
    for child in head.childrenList:
        childrenList += str(child.headValue) + ","
    childrenList = childrenList[:-1]
    if childrenList != "":
        print(childrenList)
    for child in head.childrenList:
        printTreeHelper(child)


printTree([
    Comment(1, None),
    Comment(2, 1),
    Comment(3, None),
    Comment(4, 2),
    Comment(5, 2)
])