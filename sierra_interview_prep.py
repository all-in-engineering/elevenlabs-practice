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