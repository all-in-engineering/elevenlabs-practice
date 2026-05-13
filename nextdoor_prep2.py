# ============================================================
# Problem: Merge Weekly Time Intervals
#
# Given a list of time intervals, each with a start and end time
# in the format "Weekday HH:MM" (e.g. "Sat 13:00", "Mon 09:30"),
# merge all overlapping or adjacent intervals and return them
# sorted from earliest to latest.
#
# Weekdays: Mon, Tue, Wed, Thu, Fri, Sat, Sun
#
# Two intervals should be merged if they overlap OR are adjacent
# (one ends exactly when the other begins).
#
# Input:
#   n intervals, each as a pair of time strings: start end
#   e.g. "Sat 13:00 Sat 14:00"
#
# Output:
#   m (number of merged intervals)
#   m lines, each with a merged interval: start end
#
# Constraints:
#   - All intervals are within a single week (Mon 00:00 to Sun 23:59)
#   - No interval crosses into the next week
#   - Minute-level precision
#   - Zero-length intervals (start == end) are allowed
#   - 1 <= n <= 2*10^5
#
# Example:
#   Input:
#     Sat 13:00 Sat 14:00
#     Sat 13:30 Sat 15:00
#     Sat 15:00 Sat 16:00
#
#   Output:
#     1
#     Sat 13:00 Sat 16:00
#
#   Explanation:
#     - Interval 1 and 2 overlap (13:00-14:00 and 13:30-15:00) -> merge to 13:00-15:00
#     - Result is adjacent to interval 3 (ends at 15:00, starts at 15:00) -> merge to 13:00-16:00
# ============================================================

def mergeIntervals(intervals):
    #1. find the earliest start time interval by first looking for earliest day, then looking for earliest start time
    #2. set that as earliest time so far
    #3. and set that intervals latest end time to a variable
    #4. then iterate through list without that interval and look for a start time <= end time
    #5. if the end time < end time, remove that interval from the list and continue
    #6. if the end time > current end time, set current end time to this one, remove interval from the list
    #7. this is the first interval, store in a list and then repeat until the list is empty.
    #8. return len(result), result

    result = []
    while (len(intervals) != 0):
        earliestInterval = getEarliestInterval(intervals)
        earliestStartTime = getStartTime(earliestInterval)
        currentIntervalEndTime = getEndTime(earliestInterval)
        intervalCopy = list(intervals)
        for interval in intervalCopy:
            intervalStart = getStartTime(interval)
            if (earlierTime(intervalStart, currentIntervalEndTime)):
                if (earlierTime(currentIntervalEndTime, getEndTime(interval))):
                    currentIntervalEndTime = getEndTime(interval)
                intervals.remove(interval)
        oneInterval = earliestStartTime + " " + currentIntervalEndTime
        result.append(oneInterval)
    return len(result), result

def getEarliestInterval(intervals):
    currentEarliestInterval = intervals[0]
    earliestStartTime = getStartTime(currentEarliestInterval)
    for interval in intervals:
        intervalStart = getStartTime(interval)
        if (earlierTime(intervalStart, earliestStartTime)):
            currentEarliestInterval = interval
            earliestStartTime = intervalStart
    return currentEarliestInterval

def getStartTime(interval):
    parts = interval.split(" ")
    day = parts[0]
    time = parts[1]
    return day + " " + time


def getEndTime(interval):
    parts = interval.split(" ")
    day = parts[2]
    time = parts[3]
    return day + " " + time

def earlierTime(time1, time2):
    daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    time1day = time1.split(" ")[0]
    time1hour = time1.split(" ")[1].split(":")[0]
    time1minute = time1.split(" ")[1].split(":")[1]

    time2day = time2.split(" ")[0]
    time2hour = time2.split(" ")[1].split(":")[0]
    time2minute = time2.split(" ")[1].split(":")[1]

    if (daysOfWeek.index(time1day) < daysOfWeek.index(time2day)):
        return True
    if (daysOfWeek.index(time1day) > daysOfWeek.index(time2day)):
        return False
    if (time1hour < time2hour):
        return True
    if (time1hour > time2hour):
        return False
    if (time1minute < time2minute):
        return True
    if (time1minute > time2minute):
        return False
    return True


print(mergeIntervals(["Sat 13:00 Sat 14:00", "Sat 13:30 Sat 15:00", "Sat 15:00 Sat 16:00"]))


def mergeIntervals2(intervals):
    #1. sort intervals into increasing order (nlog(n))
    #2. get the current earliest
    #3. keep going down list and check if the next start time is <= current earliest end time
    #4. if yes, set current end time to this intervals end timee
    #5. else, output this as an interval and repeat loop starting at beginning (this is an O(n) operation)
    result = []
    sortedIntervals = sortIntervals(intervals)
    intervalCopy = list(sortedIntervals)
    currentInterval = intervalCopy.pop(0)
    earliestStartTime = getStartTime(currentInterval)
    currentIntervalEndTime = getEndTime(currentInterval)
    newInterval = False

    for interval in intervalCopy:
       
        intervalStart = getStartTime(interval)
        if (earlierTime(intervalStart, currentIntervalEndTime)):
            if (earlierTime(currentIntervalEndTime, getEndTime(interval))):
                currentIntervalEndTime = getEndTime(interval)
                continue 
        else:
            oneInterval = earliestStartTime + " " + currentIntervalEndTime
            result.append(oneInterval)
            earliestStartTime = getStartTime(interval)
            currentIntervalEndTime = getEndTime(interval)
        
    oneInterval = earliestStartTime + " " + currentIntervalEndTime
    result.append(oneInterval)

    return len(result), result

def sortIntervals(intervals):
    if (len(intervals) == 1):
        return intervals
    if (len(intervals) == 2):
        earliest = getEarliestInterval(intervals)
        if (intervals.index(earliest) == 0):
            return [earliest, intervals[1]]
        else:
            return [intervals[0], earliest]
    else: 
        sortedFirstHalf = sortIntervals(intervals[0:len(intervals)//2])
        sortedSecondHalf = sortIntervals(intervals[len(intervals)//2:])
        return mergeSortedLists(sortedFirstHalf, sortedSecondHalf)

def mergeSortedLists(sortedFirstHalf, sortedSecondHalf):
    mergedList = []
    while (True):
        if sortedFirstHalf == [] and sortedSecondHalf == []:
            break
        if sortedFirstHalf == []:
            mergedList.extend(sortedSecondHalf)
            break
        if sortedSecondHalf == []:
            mergedList.extend(sortedFirstHalf)
            break
        earliest = getEarliestInterval([sortedFirstHalf[0], sortedSecondHalf[0]])
        if earliest == sortedFirstHalf[0]:
            mergedList.append(sortedFirstHalf.pop(0))
        else:
            mergedList.append(sortedSecondHalf.pop(0))
    return mergedList

print(mergeIntervals2(["Sat 13:00 Sat 14:00", "Sat 13:30 Sat 15:00", "Sat 15:00 Sat 16:00"]))


        