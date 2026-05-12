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


# ============================================================
# Problem: Spreadsheet Cycle Detection (DFS)
#
# A spreadsheet is represented as a 2D grid where:
#   - Rows are labeled by integers (1, 2, 3, ...)
#   - Columns are labeled by letters (a, b, c, ...)
#   - A cell is referenced as "<row><col>", e.g. "1a", "2c"
#
# Each cell contains either:
#   - A raw integer value (e.g. 42)
#   - A reference to another cell (e.g. "2c")
#
# Goal:
#   Determine whether any cell reference creates a cycle.
#   A cycle means following references from a cell eventually
#   leads back to that same cell.
#
# Approach: DFS with cycle detection
#   - Model the spreadsheet as a directed graph where an edge
#     A -> B means cell A references cell B.
#   - Use DFS with a "visited" and "in_stack" set to detect cycles.
#   - If you reach a node that is already in the current DFS path,
#     a cycle exists.
#
# Example:
#   grid = {
#       "1a": "2b",
#       "2b": "3c",
#       "3c": 42       # raw value, no cycle
#   }
#   => No cycle
#
#   grid = {
#       "1a": "2b",
#       "2b": "1a"     # references back to 1a => cycle!
#   }
#   => Cycle detected
#
# Key concepts:
#   - Parse cell reference strings to look up the next cell
#   - DFS traversal following references
#   - Track "in_stack" nodes to distinguish back edges (cycles)
#     from already-fully-explored nodes
# ============================================================



def checkCycle(grid):
    for rowNumber in range(len(grid)):
        for columnNumber in range(len(grid[rowNumber])):
            nextSpot = grid[rowNumber][columnNumber]
            seenSpots = set()
            while (True):
                if isinstance(nextSpot, int):
                    break
                else:
                    if (nextSpot in seenSpots):
                        return True
                    seenSpots.add(nextSpot)
                    nextSpot = grid[int(nextSpot[0])-1][ord(nextSpot[1]) - ord('a')]
    return False

# checkCycle tests
# Test 1: no cycle — 1a -> 2b -> 3c -> 42
grid1 = [
    ['2b', 0,   0 ],
    [0,   '3c', 0 ],
    [0,   0,    42],
]
print('Test 1 (no cycle):', checkCycle(grid1))

# Test 2: cycle — 1a -> 2a -> 1a
grid2 = [
    ['2a', 0],
    ['1a', 0],
]
print('Test 2 (cycle):', checkCycle(grid2))


# ============================================================
# Problem: Implement a Mini Social Network
#
# Implement a SocialNetwork class with follow relationships
# and a user feed. You must also write your own unit tests.
#
# Required Methods:
#
#   post(user_id, post_id, timestamp)
#     - user publishes a post
#
#   follow(follower_id, followee_id)
#     - create a follow relationship
#
#   unfollow(follower_id, followee_id)
#     - remove a follow relationship
#
#   get_feed(user_id, k)
#     - return up to k most recent posts from:
#         * the user themselves
#         * anyone they follow
#     - sorted by timestamp descending (newest first)
#
# Edge Cases to Handle & Test:
#   - get_feed for a user who has never posted
#   - get_feed for a user who follows nobody
#   - repeated follow calls (following same person twice)
#   - unfollow a non-existing relationship (should not crash)
#   - following oneself (decide: allow or disallow — be consistent)
#   - equal timestamps (define a tie-breaker: post_id or insertion order)
#
# Deliverables:
#   - Runnable implementation
#   - Unit tests covering: normal flows, empty/missing cases,
#     repeated operations, and equal timestamps
# ============================================================

class SocialNetwork:

    def __init__(self):
        self.followerTable = {}
        self.feedTable = {}
        self.postTable = {}
    
    def post(self, userId, postId, timestamp):
        userPostList = self.postTable[userId]
        newPostEntry = {"userId": userId, "postId": postId, "timestamp": timestamp}
        followers = self.followerTable[userId]
        for follower in followers:
            currentFeed = self.feedTable.get(follower, [])
            if (len(currentFeed) == 0):
                currentFeed.append(newPostEntry)
                self.feedTable[follower] = currentFeed
                break

            masterFeedList = list(currentFeed)
            for index in range(len(masterFeedList)):
                if currentFeed[index].get("timestamp") > timestamp:
                    continue
                elif currentFeed[index].get("timestamp") <= timestamp:
                    currentFeed.insert(index, newPostEntry)
            self.feedTable[follower] = currentFeed

        if (len(userPostList) == 0):
                userPostList.append(newPostEntry)

        masterUserPostList = list(userPostList)

        for post in masterUserPostList:
            for index in range(len(userPostList)):
                if userPostList[index].get("timestamp") > timestamp:
                    continue
                elif userPostList[index].get("timestamp") <= timestamp:
                    userPostList.insert(index, newPostEntry)
        self.postTable[userId] = userPostList

    def follow(self, follower_id, followee_id):
        followerList = self.followerTable.get(followee_id)
        if (followerList is None):
            followerList = set()
        followerList.add(follower_id)
        self.followerTable[followee_id] = followerList

        followeePosts = self.postTable.get(followee_id)
        followerFeed = self.feedTable.get(follower_id)

        if followerFeed is None:
            followerFeed = []

        if (followeePosts is None):
            self.postTable[followee_id] = []
            return

        for post in followeePosts:
            for index in range(len(followerFeed)):
                if index == 0 and post.get("timestamp") >= followerFeed[index+1]:
                    followerFeed.insert(0, post)
                    break
                if index == len(followerFeed) - 1 and post.get("timestamp") <= followerFeed[index]:
                    followerFeed.append(post)
                    break
                elif post.get("timestamp") <= followerFeed[index] and post.get("timestamp") >= followerFeed[index+1]:
                    followerFeed.insert(index, post)
                    break
        self.feedTable[followee_id] = followerFeed


    def unfollow(self, follower_id, followee_id):
        followerList = self.followerTable.get(followee_id)
        if (followerList is None):
            return
        if (followee_id in followerList):
            followerList.remove(follower_id)
            self.followerTable[followee_id] = followerList
        followerFeedList = self.feedTable.get(follower_id)
        masterFollowerFeedList = list(followerFeedList)
        for post in masterFollowerFeedList:
            if post.get("userId") == followee_id:
                followerFeedList.remove(post)
        self.feedTable[follower_id] = followerFeedList

    def getFeed(self, userId, k):
        return self.feedTable.get(userId, [])[:k]
    
    def getFollowers(self, userId):
        followerList = self.followerTable.get(userId)
        if followerList == None:
            return []
        else: 
            return followerList


testSocialNetwork1 = SocialNetwork()

print(testSocialNetwork1.getFollowers(1))
print(testSocialNetwork1.getFollowers(2))
testSocialNetwork1.follow(1, 2)
testSocialNetwork1.follow(2, 1)
print(testSocialNetwork1.getFollowers(1))
print(testSocialNetwork1.getFollowers(2))

testSocialNetwork1.post(1, "postId1", 12)
testSocialNetwork1.post(2, "postId2", 13)

print(testSocialNetwork1.getFeed(1, 10))
print(testSocialNetwork1.getFeed(2, 10))

testSocialNetwork1.unfollow(2, 1)

print(testSocialNetwork1.getFeed(1, 10))
print(testSocialNetwork1.getFeed(2, 10))





#1. Test follow and unfollow returns null
#2. Test following two people returns two for that person
#3. Test following two people for two seeparate people returns two for each of those
#4. Test following two peoplee for two separate people followed by two unfollows returns 1 follwower each
#5. Test unfollow someone when they don't follow returns same person

#1. Create two users, h ave one follow the other, have two posts with same timestamp appear and getFeed - should be in same order
#2. Same as 1, now add in one more epost, amke sure it shows up first (in same timestamp)
#3. Then add another post that is in the past, make sure it shows up last
#4. Then test add a newer post, show that it is first.

#1. 