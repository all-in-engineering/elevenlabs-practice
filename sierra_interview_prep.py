# Given a list of time intervals with corresponding text, output the text in chronological order.
# Note if there is any overlap or gap between intervals. Intervals are represented as tuples of
# start and end times.
#
# Input: A list of multiple time intervals with corresponding text,
# e.g., [(1, 3, "text1"), (2, 6, "text2"), (8, 10, "text3"), (15, 18, "text4")]
#
# Requirement: Output the text in sequence, and determine if there is any overlap or gap
# between intervals.
#
# Example:
#
# Input: [(1, 3, "text1"), (2, 6, "text2"), (8, 10, "text3"), (15, 18, "text4")]
#
# Output: "text1", "text2"
#
# Overlap/Gap: [(1, 6), (8, 10), (15, 18)]

def calculate_overlaps(time_intervals):

    print_text_master_list = list(time_intervals)
    print_overlap_master_list = list(time_intervals)
   
    textListSoFar = []
    overlapListSoFar = []

    while (len(print_text_master_list) > 0):
        earliest_interval_so_far = None
        earliest_time_so_far = None
        for interval in print_text_master_list:
            if (earliest_interval_so_far == None):
                earliest_interval_so_far = interval
                earliest_time_so_far = interval[0]
                continue
            if interval[0] <= earliest_time_so_far:
                earliest_interval_so_far = interval
                earliest_time_so_far = interval[0]

        textListSoFar.append(earliest_interval_so_far[2])
        print_text_master_list.remove(earliest_interval_so_far)
        earliest_interval_so_far = None
        earliest_time_so_far = None

    while (len(print_overlap_master_list) > 0):
        earliest_time = None
        latest_end = None
        temporaryList = list(print_overlap_master_list)

        for interval in print_overlap_master_list:
            if (earliest_time == None):
                earliest_time = interval[0]
                latest_end = interval[1]
                temporaryList.remove(interval)
                continue
            else:
                if (interval[0] <= latest_end):
                    if (interval[1] >= latest_end):
                        latest_end = interval[1]
                    temporaryList.remove(interval)
        overlapListSoFar.append([earliest_time, latest_end])
        earliest_time = None
        latest_end = None
        print_overlap_master_list = list(temporaryList)

    return textListSoFar, overlapListSoFar


    #3. first calculating all overlaps and gaps
    #4. start with the smallest start time and its end time,
    #5. check if there iss any start times <= to the end time in other intervals
    #6. if this end time is greater than the curent time, update end time to this, and look for other start times <= to it
    #7. if you can find any. end interval, and try from the next highest start time <= the most recent end time.
    #6. if s

if __name__ == "__main__":
    intervals = [(1, 3, "text1"), (2, 6, "text2"), (8, 10, "text3"), (15, 18, "text4")]
    result = calculate_overlaps(intervals)
    print(result)


# ============================================================
# Problem: Implement an OrderedIntStream
#
# Given an integer list nums of length n, implement a data structure
# that streams elements from left to right.
#
# The constructor takes nums.
# Provide method next():
#   - If there are remaining elements, return the next element.
#   - If all elements have been output, return string "END".
#
# Constraints:
#   1 <= n <= 2*10^5
#   nums[i] fits in 32-bit signed integer
#   Total number of next() calls is at most n + 1
#
# Test Cases:
#   nums = [3,1,4], call next() 4 times  => 3, 1, 4, END
#   nums = [10],    call next() 2 times  => 10, END
#   nums = [-1,-2], call next() 3 times  => -1, -2, END
#   nums = [5,5,5], call next() 4 times  => 5, 5, 5, END
#   nums = [],      call next() once     => END
# ============================================================

class OrderedIntStream:

    def __init__(self, integerList):
        self.integerList = integerList
        self.currentIndex = 0
    
    def next(self):
        if self.currentIndex == len(self.integerList):
            return "END"
        else:
            answer = self.integerList[self.currentIndex]
            self.currentIndex += 1
            return answer


# ============================================================
# Problem: Implement a MultiplesStream
#
# Initialize with:
#   base  - the base integer
#   k     - how many values to output
#
# Method next():
#   1st call returns base * 1
#   2nd call returns base * 2
#   ...
#   k-th call returns base * k
#   After k outputs, further calls return "END"
#
# Constraints:
#   -10^9 <= base <= 10^9
#   0 <= k <= 2*10^5
#   Total next() calls <= k + 1
#
# Test Cases:
#   base=3,  k=5 => 3, 6, 9, 12, 15, END
#   base=-2, k=3 => -2, -4, -6, END
#   base=10, k=0 => END
#   base=0,  k=4 => 0, 0, 0, 0, END
#   base=7,  k=1 => 7, END
# ============================================================

class MultipleStream:

    def __init__(self, base, k):
        self.base = base
        self.k = k
        self.currentCall = 1
    
    def next(self):
        if self.currentCall == self.k + 1:
            return "END"
        else:
            answer = self.base * self.currentCall
            self.currentCall += 1
            return answer


# ============================================================
# Problem: Implement a MergeStream
#
# Each stream supports next():
#   - returns the next integer
#   - returns "END" when exhausted
#
# Given streams: List[Stream], implement MergeStream.next():
#   - Read from streams[0] until it returns "END"
#   - Then move to streams[1], and so on
#   - After all streams are exhausted, return "END"
#
# Constraints:
#   0 <= m <= 2*10^5 (number of streams)
#   Total items across all streams is T; total calls to
#   MergeStream.next() <= T + 1
#
# Test Cases:
#   streams = [[1,2],[3],[4,5]]  => 1, 2, 3, 4, 5, END
#   streams = [[],[7]]           => 7, END
#   streams = []                 => END
#   streams = [[-1,-1],[]]       => -1, -1, END
#   streams = [[10]]             => 10, END
# ============================================================



class MergeStream:

    def __init__(self, listOfStreams):
        self.listOfStreams = listOfStreams
        self.currentStream = 0
    
    def next(self):
        if len(self.listOfStreams) == self.currentStream:
            return "END"
        else:
            currentStream = self.listOfStreams[self.currentStream]
            answer = currentStream.next()
            if (answer == "END"):
                self.currentStream += 1
                return self.next()
            else:
                return answer