v_array_test1 = [10, 9, 9, 8, 7, 8, 9, 12]
v_array_test2 = []
v_array_test3 = [1]
v_array_test4 = [10, 9]
v_array_test5 = [9, 10]
v_array_test6= [10, 9, 9, 8, 7, 8, 9, 9, 10]

#questions from nimble:
#1. implement function for both getting minimum and sorting a v array, 
#which is when numbers are guaranteed to be equal/descending and then ascending after
#2. implement summing of linkedlists: https://leetcode.com/problems/add-two-numbers/description/


def getMinimum(v_array):
    if len(v_array) == 0:
        return [-1, -1]
    else:
        currentMin = v_array[0]
        currentIndex = 0
        while (currentIndex < len(v_array)-1):
            if (v_array[currentIndex] >= v_array[currentIndex+1]):
                currentMin = v_array[currentIndex+1]
                currentIndex += 1
            else:
                return [currentMin, currentIndex]
        return [currentMin, currentIndex]
        
        
print(getMinimum(v_array_test1))
print(getMinimum(v_array_test2))
print(getMinimum(v_array_test3))
print(getMinimum(v_array_test4))
print(getMinimum(v_array_test5))

        
def sort_v_array(v_array):
    #1. First find the minimum value in the v_array and its index
    #2. Keep track of pointers to the left and right of array
    #3. If both pointers are == -1 and right counter == len, return array so far
    #3. If they are equal, add both to the new array and increment right counter, decrement left counter
    #4. If the left index is <0 add the right value to array and increment right counter
    #5. If right index is >= input.len, add left value to array and decrement left counter

    #edge cases
    #1. v_array len == 0 or 1 return v_array

    if len(v_array) == 0 or len(v_array) == 1:
        return v_array
    else:
        minimum = getMinimum(v_array)
        minimumValue = minimum[0]
        minimumIndex = minimum[1]
        leftIndex = minimumIndex-1
        rightIndex = minimumIndex
        leftValue = v_array[leftIndex]
        rightValue = v_array[rightIndex]
        sortedArray = []
        v_array_test1 = [10, 9, 9, 8, 7, 8, 9, 12]

        while(True):
            if (leftIndex == -1 and rightIndex == len(v_array)):
                return sortedArray
            elif (leftIndex == -1):
                sortedArray.append(rightValue)
                rightIndex += 1
                if (rightIndex != len(v_array)):
                   rightValue = v_array[rightIndex]
            elif (rightIndex == len(v_array)):
                sortedArray.append(leftValue)
                leftIndex -= 1
                if (leftIndex != -1):
                    leftValue = v_array[leftIndex]
            elif (leftValue == rightValue):
                sortedArray.append(leftValue)
                sortedArray.append(leftValue)
                leftIndex -= 1
                rightIndex += 1
                if (leftIndex != -1):
                    leftValue = v_array[leftIndex]
                if (rightIndex != len(v_array)):
                    rightValue = v_array[rightIndex]
            elif (leftValue > rightValue):
                sortedArray.append(rightValue)
                rightIndex += 1
                if (rightIndex != len(v_array)):
                    rightValue = v_array[rightIndex]
            else:
                sortedArray.append(leftValue)
                leftIndex -= 1
                if (leftIndex != -1):
                    leftValue = v_array[leftIndex]
        return sortedArray


print(sort_v_array(v_array_test1))
print(sort_v_array(v_array_test2))
print(sort_v_array(v_array_test3))
print(sort_v_array(v_array_test4))
print(sort_v_array(v_array_test5))
print(sort_v_array(v_array_test6))

class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

def sumTwoLists(node1, node2):
    #1. get the current values of the nodes
    #2. sum them up
    #3. return the first node of the summed linked list
    #4. if there is carryover and keep track in the next call
    #5. if carryover is used return it back to 0
    carryover = 0
    currentSummedNode = Node(-1, None)
    answer = currentSummedNode

    while node1 != None or node2 != None:
        if (node1 == None):
            sum = node2.value + carryover
            nextNode = Node(sum % 10, None)
            currentSummedNode.nextNode = nextNode
            currentSummedNode = currentSummedNode.nextNode
            node2 = node2.nextNode
            if (sum < 10):
                carryover = 0
            else:
                carryover = 1
            continue
        if (node2 == None):
            sum = node1.value + carryover
            nextNode = Node(sum % 10, None)
            currentSummedNode.nextNode = nextNode
            currentSummedNode = currentSummedNode.nextNode
            node1 = node1.nextNode
            if (sum < 10):
                carryover = 0
            else:
                carryover = 1
            continue
        node1value = node1.value
        node2value = node2.value
        sum = node1value + node2value + carryover
        nextNode = Node(sum % 10, None)
        if (sum < 10):
            carryover = 0
        else:
            carryover = 1
        currentSummedNode.nextNode = nextNode
        currentSummedNode = currentSummedNode.nextNode
        node1 = node1.nextNode
        node2 = node2.nextNode
    if (carryover == 1):
        nextNode = Node(1, None)
        currentSummedNode.nextNode = nextNode
    return answer.nextNode


def list_to_nodes(values):
    if not values:
        return None
    head = Node(values[0], None)
    current = head
    for v in values[1:]:
        current.nextNode = Node(v, None)
        current = current.nextNode
    return head

def nodes_to_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.nextNode
    return result

print(nodes_to_list(sumTwoLists(list_to_nodes([1]), list_to_nodes([2]))))
print(nodes_to_list(sumTwoLists(list_to_nodes([9]), list_to_nodes([9]))))
print(nodes_to_list(sumTwoLists(list_to_nodes([9, 9, 9]), list_to_nodes([9]))))
print(nodes_to_list(sumTwoLists(list_to_nodes([1]), list_to_nodes([9]))))
print(nodes_to_list(sumTwoLists(list_to_nodes([9]), list_to_nodes([9, 9, 9, 9]))))

