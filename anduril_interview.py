# Anduril Interview Prep

'''
Implement a class that stores object detections over time.

Each detection has:
- zone: string
- timestamp: integer
- label/object: string

Implement two methods:

store_detection(zone, timestamp, label)
    Records that at this timestamp, this zone detected this label.

get_detection(zone, timestamp) -> label
    Returns the most recent detection label for that zone at or before the given timestamp.

Assume detections arrive in increasing timestamp order.
Different zones are independent.

Example:
tracker.store_detection("zone_alpha", 1, "dog")
tracker.store_detection("zone_beta", 3, "cat")
tracker.store_detection("zone_alpha", 7, "human")

tracker.get_detection("zone_alpha", 6) -> dog

Figure out time complexity of brute force solution, sort solution (Olog(n) space, O(n) time), and fastest time (O(1), O(timestamp range)

'''

'''
Test Cases

tracker.store_detection("zone_alpha", 1, "dog")
tracker.store_detection("zone_beta", 3, "cat")
tracker.store_detection("zone_alpha", 7, "human")

tracker.get_detection("zone_alpha", 6) -> dog DONE
tracker.get_detection("zone_alpha", 7) -> human DONE
tracker.get_detection("zone_alpha", 8) -> human
tracker.get_detection("zone_alpha", 0) -> None


Edge Cases

1) Timestamp is before even the first one in the list:


Main Algorithm

GetDetection(zone, timestamp)
1. Lookup zone in trackerMap
2. If zone doesn't exist return None

List is length 1 case:
if 1) length is == 1 and timestamp < list[0][1]
return None
else if: 
    length is == 1 and timestamp == list[0][1]
    return list[0][0]

Previous = list[0]

3. Now iterate through each item in the list starting at index = 1
4. currentTarget = list[index]
5. Check if the timestamp == item[1]
5. If yes, return item[0]
6. if timestamp < item[1]
else, return previous[0]
previous = currentTarget

6. If we exit out, return previous[0]
'''
import math

class Tracker:

    def __init__(self):
        self.zoneMap = {}

    def store_detection(self, zone, timestamp, object):
        if (self.zoneMap.get(zone) == None):
            newTarget = [[timestamp, object]]
            self.zoneMap[zone] = newTarget
        else:
            currentList = self.zoneMap[zone]
            currentList.append([timestamp, object])
            self.zoneMap[zone] = currentList

    def get_detection(self, zone, timestamp):
        currentZone = self.zoneMap.get(zone)
        if currentZone == None:
            return None
        if len(currentZone) >= 1 and timestamp < currentZone[0][0]:
            return None
        if (len(currentZone) >= 1 and timestamp == currentZone[0][0]):
            return currentZone[0][1]
        previous = currentZone[0]

        for targetIndex in range(1, len(currentZone)):
            currentTarget = currentZone[targetIndex]
            if timestamp == currentTarget[0]:
                return currentTarget[1]
            if timestamp < currentTarget[0]:
                return previous[1]
            else:
                previous = currentTarget
        return previous[1]
    

    """
    Test Cases:
    [1, 3, 5, 7, 10] timestamp 6


    Edge Cases:
    1) if the subzone is 1 in length:
        if subzone target >= timestamp
            return subzone object
        else:
            return null

    Main Algorithm:
    1) Figure out length of the zone, and get the floor(middle index)
    2) Compare the timestamp of this target
    3) If its == timestamp return the object and we are done
    4) If timestamp > targettimestamp, run merge against on the upper half
    5) If timestamp < targettimestamp, keeptrack of this pivot and run merge and compare results between this pivot and merge result.
    6) whichever onee is higher return that
    """

    def get_detection_sort(self, zone, timestamp):
        return self.get_detection_sort_helper(self.zoneMap.get(zone), timestamp)[1]
    
    '''
    This function figures out the pivot, whether the object is in the greater half or lower half of the list
    '''
    def get_detection_sort_helper(self, halfList, timestamp):
        if len(halfList) == 0:
            return None
        
        if len(halfList) == 1 and timestamp >= halfList[0][0]:
            return halfList[0]
        
        if len(halfList) == 1 and timestamp < halfList[0][0]:
            return None
        
        middleIndex = math.floor(len(halfList)/2)
        middleTarget = halfList[middleIndex]
        bestMatchInHalf = None

        if middleTarget[0] == timestamp:
            return middleTarget
        
        if timestamp > middleTarget[0]:
            bestMatchInHalf = self.get_detection_sort_helper(halfList[middleIndex:], timestamp)
        else:
            bestMatchInHalf = self.get_detection_sort_helper(halfList[0:middleIndex], timestamp)

        if bestMatchInHalf == None:
            return middleTarget
        elif bestMatchInHalf[0] >= timestamp:
            return bestMatchInHalf
        else:
            return middleTarget

    def store_detection_sparse(self, zone, timestamp, object):
        if (self.zoneMap.get(zone) == None):
            newTarget = [[timestamp, object]]
            self.zoneMap[zone] = newTarget
        else:
            currentList = self.zoneMap[zone]
            difference = timestamp - currentList[len(currentList)-1][0]
            for index in range(0, difference):
                currentList.append([timestamp, object])
            self.zoneMap[zone] = currentList
            print(currentList)

    def get_detection_sparse(self, zone, timestamp):
        targetList = self.zoneMap[zone]
        return targetList[timestamp][1]    



    
tracker = Tracker()
tracker.store_detection("zone_alpha", 1, "dog")
tracker.store_detection("zone_beta", 3, "cat")
tracker.store_detection("zone_alpha", 3, "human")
tracker.store_detection("zone_alpha", 5, "rat")
tracker.store_detection("zone_alpha", 7, "snake")
tracker.store_detection("zone_alpha", 9, "bird")

print(tracker.get_detection_sort("zone_alpha", 4))



tracker = Tracker()
tracker.store_detection_sparse("zone_alpha", 1, "dog")
tracker.store_detection_sparse("zone_alpha", 3, "human")
tracker.store_detection_sparse("zone_alpha", 5, "rat")

print(tracker.get_detection_sparse("zone_alpha", 4))