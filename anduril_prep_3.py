# Given an interval list `intervals` sorted by start time and a target interval `target`,
# where target can be any range like [3, 10], insert `target` into `intervals` such that
# the list remains sorted and any overlapping intervals are merged.
# Return the resulting interval list.
#
# Example:
#   intervals = [[1, 3], [6, 9]], target = [2, 5]
#   Output: [[1, 5], [6, 9]]


#Edge cases:


def insertInterval(intervals, target):
    ''' 

    1. If we find an interval where target is inside that interval, return intervals immediately.
    2. If we find an interval where target start is after interval end, continue.
    3. If we find an interval where target end is before interval start, insert target at this index in interavals and return intervals immediately.

    in merging case:

    1. Find the first interval where the start is less than or equal to target start time AND end time is <= target end time. This is when merging begins
    2. Set the end time of this interval to the target end time
    3. Go down the list and find the first interval's start time that is after the target's end time
    4. This is the index where merging ends, delete all items between the interval when merging began and now, and return intervals.
    
    '''
    
    merging = False
    currentIndex = 0
    mergeIndex = 0

    while (currentIndex != len(intervals)):
        currentInterval = intervals[currentIndex]
        if not merging:
            if currentInterval[0] <= target[0] and currentInterval[1] >= target[1]:
                return intervals
            elif target[0] > currentInterval[1]:
                    currentIndex += 1
                    continue
            elif target[1] < currentInterval[0]:
                    intervals.insert(currentIndex, target)
                    return intervals
            elif target[0] >= currentInterval[0] and target[1] >= currentInterval[1]:
                    merging = True
                    currentInterval[1] = target[1]
                    mergeIndex = currentIndex
                    currentIndex += 1
            elif target[0] <= currentInterval[0]:
                 merging = True
                 currentInterval[0] = target[0]
                 if target[1] >= currentInterval[1]:
                      currentInterval[1] = target[1]
                 mergeIndex = currentIndex
                 currentIndex += 1
        else:
            if intervals[mergeIndex][1] >= currentInterval[1] and currentInterval[1]:
                intervals.pop(currentIndex)
                continue
            elif intervals[mergeIndex][1] >= currentInterval[0] and currentInterval[1] >= intervals[mergeIndex][1]:
                 intervals[mergeIndex][1] = currentInterval[1]
                 intervals.pop(currentIndex)
                 continue
            elif intervals[mergeIndex][1] < currentInterval[0]:
                return intervals
    if not merging:
         intervals.append(target)
    return intervals

       
        


      



tests = [
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),           # basic overlap merge
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),  # merge multiple
    ([[5,7],[9,12]], [1,3], [[1,3],[5,7],[9,12]]),    # insert at beginning
    ([[1,3],[5,7]], [10,15], [[1,3],[5,7],[10,15]]),  # insert at end
    ([[1,2],[3,4],[5,6]], [0,10], [[0,10]]),           # target swallows all
    ([], [3,10], [[3,10]]),                            # empty list
    ([[1,3],[5,8]], [3,5], [[1,8]]),                   # touching boundaries
    ([[1,2],[8,10]], [4,6], [[1,2],[4,6],[8,10]]),    # no overlap, insert middle
]

for i, (intervals, target, expected) in enumerate(tests):
    result = insertInterval(intervals, target)
    if result != expected:
        print(f"FAIL test {i+1}: intervals={intervals}, target={target}")
        print(f"  expected: {expected}")
        print(f"  got:      {result}")
    else:
        print(f"PASS test {i+1}")
