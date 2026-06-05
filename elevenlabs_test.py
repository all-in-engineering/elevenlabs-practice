# ElevenLabs Interview Prep

# We consider the sequence of numbers where a number is followed by the same number plus the sum of its digits.
# For example 34 is followed by 41 (as 41 = 34 + (3 + 4)). 41 is itself followed by 46 (46 = 41 + (4 + 1)).
# Two sequences which start from different numbers may join at a given point, for example, the sequence
# starting from 471 and the sequence starting from 480 share the number 519 (the join point) in their sequence.
# After the join point, the sequences are equal.
#
# Implement the function
# compute_join_point(s1: int, s2: int) -> int
#
# which takes the starting points of two sequences and then returns the join point of these sequences.
# You are guaranteed that the two given sequences always join, at a joining point lower than 20,000,000.


#print("Debug messages...", file=sys.stderr, flush=True)

def compute_join_point(input1, input2):
    input1Map = set()
    input2Map = set()
    input1Map.add(input1)
    input2Map.add(input2)
    input1sequence = input1
    input2sequence = input2
    while True:
        input1string = list(str(input1sequence))
        input2string = list(str(input2sequence))
        input1sum = 0
        input2sum = 0
        for i in input1string:
            input1sum += int(i)
        for j in input2string:
            input2sum += int(j)
        input1sum += input1sequence
        input2sum += input2sequence

        input1Map.add(input1sum)
        input2Map.add(input2sum)
        if (input1sum in input2Map):
            return input1sum
        if (input2sum in input1Map):
            return input2sum
        input1sequence = input1sum
        input2sequence = input2sum

print(compute_join_point(471, 480))  # expected: 519

# The goal of this exercise is to find the endpoint node of a simple network, or find the loop if there is one.
# In this simple network, each node is linked to at most one outgoing node in a one way forward direction.
# Implement the function
# compute(start_node_id, from_ids, to_ids)
#
# which should return the last node id of the network found when starting from the node with id
# start_node_id and following the links of the network.

def compute(start_node_id, from_ids, to_ids):
    seenPaths = set()
    currentNode = start_node_id
    while True:
        if (currentNode in seenPaths):
            return "Loop detected"
        if (currentNode not in from_ids):
            return currentNode
        from_ids_index = from_ids.index(currentNode)
        nextNode = to_ids[from_ids_index]
        seenPaths.add(currentNode)
        currentNode = nextNode

# Test: A → B → C → D, start from A, expected endpoint: D
print(compute('A', ['A', 'B', 'C'], ['B', 'C', 'D']))  # expected: D

# Test: loop A → B → C → B, start from A, expected: "Loop detected"
print(compute('A', ['A', 'B', 'C'], ['B', 'C', 'B']))  # expected: Loop detected

# Wind and Leaves Grid Problem
#
# Given:
# A grid of integers representing a field with leaves.
# Each integer represents the number of leaves in that cell.
# The grid size is m x n (m rows and n columns).
# A string representing wind directions.
# Each character in the string is one of 'U', 'D', 'L', or 'R'.
# U = Up, D = Down, L = Left, R = Right
# The length of this string represents the number of wind events.
#
# Rules:
# For each wind event (each char in the wind string):
#   All leaves move one cell in the direction of the wind.
#   Leaves that move off the grid are lost and removed from the count.
#
# Task:
# Write a function that takes the grid and the wind string as input, and returns the total number
# of leaves remaining on the grid after all wind events have occurred.
#
# Example:
# Input:  grid = [[1, 0, 2], [4, 1, 0], [0, 3, 1]], wind = "RR"
# Output: 4


#there was a Test case where they giv eyou a long string of UDUDUDUDUD

def sum_leaves(grid, windString):
    currentGridState = grid
    for windDirection in windString:
        if windDirection == "U":
            for i in range(len(currentGridState)):
                row = currentGridState[i - 1]
                if i == len(currentGridState) - 1:
                    emptyRow = []
                    for column in row:
                        emptyRow.append(0)
                    currentGridState[len(currentGridState) - 1] = emptyRow
                else:
                    currentGridState[i] = currentGridState[i+1]
            print("grid is " + str(grid))
            continue
        elif windDirection == "D":
            for i in range(len(currentGridState) - 1, -1, -1):
                row = currentGridState[i - 1]
                if i == 0:
                    emptyRow = []
                    for column in row:
                        emptyRow.append(0)
                    currentGridState[0] = emptyRow
                else:
                    currentGridState[i] = currentGridState[i-1]
            print("grid is " + str(grid))
            continue
        elif windDirection == "R":
            for i in range(len(currentGridState)):
                currentRow = currentGridState[i]
                for i in range(len(currentRow) - 1, -1, -1):
                    if i == 0:
                        currentRow[0] = 0
                    else:
                        currentRow[i] = currentRow[i-1]
            print("grid is " + str(grid))
            continue
        elif windDirection == "L":
            for i in range(len(currentGridState)):
                currentRow = currentGridState[i]
                for i in range(len(currentRow)):
                    if i == len(currentRow) - 1:
                        currentRow[i] = 0
                    else:
                        currentRow[i] = currentRow[i+1]
            print("grid is " + str(grid))
            continue

    sum = 0
    for row in currentGridState:
        for i in range(len(row)):
            sum += row[i]
    return sum

print(sum_leaves([[1, 0, 2], [4, 1, 0], [0, 3, 1]], "RR"))  # expected: 4

grid = [[1, 0, 2], [4, 1, 0], [0, 3, 1]]
print(sum_leaves([row[:] for row in grid], "R"))  # expected: 9
print(sum_leaves([row[:] for row in grid], "L"))  # expected: 7
print(sum_leaves([row[:] for row in grid], "U"))  # expected: 9
print(sum_leaves([row[:] for row in grid], "D"))  # expected: 8


