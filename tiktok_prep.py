# Problem: Print Execution Order in a DAG and Detect Cycles
#
# You are given n tasks numbered from 0 to n-1, and m dependency relations.
# Each dependency is a directed edge u -> v, meaning task u must be executed before task v.
#
# Print a valid execution order such that for every dependency u -> v, u appears before v.
# If the dependency graph contains a cycle, print IMPOSSIBLE.
#
# Input Format:
#   n m
#   u1 v1
#   u2 v2
#   ...
#   n: number of tasks
#   m: number of dependency relations
#
# Output Format:
#   If valid, print one line containing n integers.
#   If cycle exists, print: IMPOSSIBLE
#
# Constraints:
#   1 <= n <= 2 * 10^5
#   0 <= m <= 2 * 10^5
#   0 <= u, v < n
#   The graph may be disconnected
#   The graph may contain a cycle
#
# Example 1:
#   Input:  4 4 / 0 1 / 0 2 / 1 3 / 2 3
#   Output: 0 1 2 3
#
# Example 2:
#   Input:  3 3 / 0 1 / 1 2 / 2 0
#   Output: IMPOSSIBLE
import copy

def detectCycle(numTasks, edges):

    adjacencyMap = {}
    for edge in edges:
        if edge[0] in adjacencyMap:
            adjacencyMap[edge[0]].append(edge[1])
        else:
            adjacencyMap[edge[0]] = [edge[1]]

    listPaths = []
    for edge in edges:
        onePath = []
        seenEdges = set()
        currentEdge = edge
        adjacencyMapCopy = copy.deepcopy(adjacencyMap)
        while (True):
            if tuple(currentEdge) in seenEdges:
                return "IMPOSSIBLE"
            onePath.append(currentEdge)
            seenEdges.add(tuple(currentEdge))
            if (currentEdge[0] in adjacencyMapCopy):
                adjacencyMapCopy[currentEdge[0]].remove(currentEdge[1])
            nextEdge = adjacencyMapCopy.get(currentEdge[1], [])
            if not nextEdge:
                listPaths.append(onePath)
                adjacencyMap = adjacencyMap.copy()
                break
            else:
                currentEdge = [currentEdge[1], nextEdge[0]]
    return listPaths