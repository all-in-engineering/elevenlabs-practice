# Flexport Interview Prep 3

'''
Problem: Print Company Organizational Tree

Given a company's hierarchical organizational structure, print each level of
employees in a specified traversal order. Assume the input data is a tree-like
structure that includes employee names and the direct reporting relations.
Implement an algorithm to print the organizational structure using in-order
DFS traversal.

Example Input:
    {
        "CEO": {
            "DirectReports": [
                {"VP1": {"DirectReports": [{"Manager1": {}}]}},
                {"VP2": {}}
            ]
        }
    }

Example Output:
    Manager1
    VP1
    CEO
    VP2

Requirements:
    - Implement in-order DFS traversal
    - Output order must match the given traversal order
'''

"""
Test Cases:
  CEO
 /  \
VP1  VP2
output: vp1, ceo, vp2


  CEO
 /  \     \
VP1  VP2.  VP3
output: vp1, ceo, vp2 vp3


Edge Cases:
CEO only -> print CEO




Main Algorithm:


call traverse on left child, print out current node value, then for each remaining child call traverse.

"""


def traverse(orgChart):
    if (len(orgChart.directReports)== 0):
        print(orgChart.head)
    else:
        traverse(orgChart.directReports[0])
        print(orgChart.head)
        for index in range(1, len(orgChart.directReports)):
            traverse(orgChart.directReports[index])

class orgChart:
    def __init__(self, head, directReports):
        self.head = head
        self.directReports = directReports


'''
Problem: Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's
(water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. All four edges of the grid are surrounded by water.

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'

Example 1:
    Input:
        [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]
    Output: 1

Example 2:
    Input:
        [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]
    Output: 3
'''

"""
Test Cases:
[1, 0]
[0, 1] = 2


[1, 1]
[1, 1] = 1


[1, 1]
[0, 0] = 1

Edge Cases:


Main Algorithm:
1) Traverse each starting point in two for loops:
2) If it's 0 just continue since this is just water:
3) If it's a 1, now begin a search where you do BFS with each direction left, right, up, down, acting as a child
4) If a child is a 0 skip, if 1, add all their left, right up downs that are 1's
5) Continue this search until we see no children that are 1's, then increment island count by 1
6) Continue Search


"""
def count_islands(matrix):
    matrix = [[int(cell) for cell in row] for row in matrix]
    islandCount = 0
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[row_index])):
            currentSpot = matrix[row_index][column_index]
            if currentSpot == 0:
                continue
            else:
                spotsToExplore = [[row_index, column_index]]

                while (len(spotsToExplore) != 0):
                    currentSpot = spotsToExplore.pop(0)
                    if matrix[currentSpot[0]][currentSpot[1]] == 0:
                        continue
                    matrix[currentSpot[0]][currentSpot[1]] = 0

                    if currentSpot[0]+1 < len(matrix):
                        spotsToExplore.append([currentSpot[0]+1, currentSpot[1]])
                    if currentSpot[0]-1 >= 0:
                        spotsToExplore.append([currentSpot[0]-1, currentSpot[1]])
                    if currentSpot[1]+1 < len(matrix[row_index]):
                        spotsToExplore.append([currentSpot[0], currentSpot[1]+1])
                    if currentSpot[1]-1 >= 0:
                        spotsToExplore.append([currentSpot[0], currentSpot[1]-1])
                islandCount += 1
    return islandCount


'''
Problem: Flooded Map After Sinking Islands

Given a 2D map where '1' represents land and '0' represents water, the map is
surrounded by water. When a flood occurs, all islands that are not in contact
with the boundary are submerged. Write an algorithm to print the map after
the flood.

Constraints:
    - The size of the input map is m x n, where m and n are in the range [1, 100]

Example Input:
    [['1', '1', '1', '1', '0'],
     ['1', '1', '0', '1', '0'],
     ['1', '1', '0', '0', '0'],
     ['0', '0', '0', '0', '0']]

Example Output:
    [['1', '1', '1', '1', '0'],
     ['1', '1', '0', '1', '0'],
     ['1', '1', '0', '0', '0'],
     ['0', '0', '0', '0', '0']]
'''


"""
Test Cases:

[1, 0, 0, 0]
[0, 1, 1, 0]
[0, 0, 0, 0]

should return a matrix with the 1 in the middle 0'd out


[1, 0, 0]
[0, 1, 0]
[0, 0, 1]

should return a matrix with the 1 in the middle 0'd out

[1, 1, 0]
[0, 1, 0]
[0, 0, 1]

should return itself since the 1 in the middle is connected to the boundary island

[1, 1]
[0, 1]

should return the same thing since there is no middle


Edge Cases:


Main Algorithm:

1) Do a traversal of all border islands by only iterating through all border spots using similar island count algorithm
2) Mark all of those islands as a 2
3) now traverse through entire matrix and anything that's a 1 is a middle island, convert those to 0
4) Now go through entire matrix and convert all 2's back to 1
5) return result


"""

def submerge_island(matrix):
    #1) Do a traversal of all border islands by only iterating through all border spots using similar island count algorithm
    #2) Mark all of those islands as a 2

    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            if (row_index == 0 or row_index == len(matrix) - 1) and (column_index == 0 or column_index == len(matrix[0])-1):
                spotsToExplore = [[row_index, column_index]]
                if matrix[row_index][column_index] == 0 or matrix[row_index][column_index] == 2:
                    continue
                while (len(spotsToExplore) != 0):
                    currentSpot = spotsToExplore.pop(0)
                    if matrix[currentSpot[0]][currentSpot[1]] == 0 or matrix[currentSpot[0]][currentSpot[1]] == 2:
                        continue
                    matrix[currentSpot[0]][currentSpot[1]] = 2
                    if currentSpot[0]+1 < len(matrix):
                        spotsToExplore.append([currentSpot[0]+1, currentSpot[1]])
                    if currentSpot[0]-1 >= 0:
                        spotsToExplore.append([currentSpot[0]-1, currentSpot[1]])
                    if currentSpot[1]+1 < len(matrix[row_index]):
                        spotsToExplore.append([currentSpot[0], currentSpot[1]+1])
                    if currentSpot[1]-1 >= 0:
                        spotsToExplore.append([currentSpot[0], currentSpot[1]-1])

    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            if matrix[row_index][column_index] == 1:
                spotsToExplore = [[row_index, column_index]]
                while (len(spotsToExplore) != 0):
                    currentSpot = spotsToExplore.pop(0)
                    if matrix[currentSpot[0]][currentSpot[1]] == 0 or matrix[currentSpot[0]][currentSpot[1]] == 2:
                        continue
                    matrix[currentSpot[0]][currentSpot[1]] = 0
                    if currentSpot[0]+1 < len(matrix):
                        spotsToExplore.append([currentSpot[0]+1, currentSpot[1]])
                    if currentSpot[0]-1 >= 0:
                        spotsToExplore.append([currentSpot[0]-1, currentSpot[1]])
                    if currentSpot[1]+1 < len(matrix[row_index]):
                        spotsToExplore.append([currentSpot[0], currentSpot[1]+1])
                    if currentSpot[1]-1 >= 0:
                        spotsToExplore.append([currentSpot[0], currentSpot[1]-1])

    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            if matrix[row_index][column_index] == 2:
                matrix[row_index][column_index] = 1
    return matrix
