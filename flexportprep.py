# =============================================================================
# Problem: Road Travel Simulation
# =============================================================================
#
# Design a Road class to simulate a vehicle's journey from a starting point
# to an exit, considering travel time and traffic lights.
#
# Rules:
#   - Each road section takes 1 minute to traverse.
#   - Green light: vehicle passes immediately.
#   - Red light: vehicle waits 1 extra minute, then proceeds.
#
# Parts:
#   1. One car, all green lights, one road.
#      - Vehicle starts at point J and travels through each traffic light to exit.
#
#   2. One car, toggling lights, one road.
#      - Traffic lights alternate between red and green each minute.
#
#   3. Multiple roads.
#      - Roads intersect to form multiple paths; vehicles start from different points.
#
#   4. Multiple vehicles.
#      - Cars start simultaneously from different points and must follow traffic
#        light rules to find the optimal (fastest) path to the exit.
#
# Interface:
#   road = Road()
#   time_taken = road.travel()
#   print(time_taken)  # total minutes from start to exit
#
# Goals:
#   - Extendable design that naturally supports each added part.
# =============================================================================

"""
Test Cases:
road = []

Edge Cases:

Main Algorithm:

1) Construct a road class that has: nextRoad, and greenLight boolean = True/False
2) Traverse down the road and compute how many roads and how many redlights there are
3) Total time is (roads + countRedLights)

"""

class Road:

    def __init__(self):
        self.nextRoad = None
        self.isGreenLight = True
        self.nextRoads = []
    
    def countTimeCase1(self):
        currentRoad = self
        time = 0
        while (True):
            if currentRoad != None:
                extraTime = 1
                if not currentRoad.isGreenLight:
                    extraTime += 1
                time += extraTime
                currentRoad = currentRoad.nextRoad
            else:
                break
        return time
    
    def countTimeCase2(self):
        currentRoad = self
        time = 0
        while (True):
            if currentRoad != None:
                extraTime = 1
                currentLight = currentRoad.isGreenLight
                if time % 2 != 0:
                    currentLight = not currentLight
                if not currentLight:
                    extraTime += 1
                time += extraTime
                currentRoad = currentRoad.nextRoad
            else:
                break
        return time
    

    def countTimeCase3(self):
        roadsToTraverse = [[self, 0]]
        shortestTimeSoFar = float('inf')
        while (len(roadsToTraverse) != 0):
            currentRoad = roadsToTraverse.pop(0)
            if (currentRoad[0] == None):
                if shortestTimeSoFar > currentRoad[1]:
                    shortestTimeSoFar = currentRoad[1]
                    continue
            else:
                timeSoFar = currentRoad[1]
                currentLight = currentRoad[0].isGreenLight
                if timeSoFar % 2 != 0:
                    currentLight = not currentLight
                extraTime = 1  # fix: was missing, caused NameError
                if not currentLight:
                    extraTime += 1
                timeSoFar += extraTime
                for childRoad in currentRoad[0].nextRoads:  # fix: was currentRoad.nextRoads (missing [0])
                    roadsToTraverse.append([childRoad, timeSoFar])

        return shortestTimeSoFar


# =============================================================================
# Test Cases
# =============================================================================

def test_case1():
    # 1 green node → 1 min
    r = Road()
    assert r.countTimeCase1() == 1

    # 3 green nodes → 3 mins
    r1, r2, r3 = Road(), Road(), Road()
    r1.nextRoad, r2.nextRoad = r2, r3
    assert r1.countTimeCase1() == 3

    # 3 nodes, middle is red → 4 mins
    r1, r2, r3 = Road(), Road(), Road()
    r2.isGreenLight = False
    r1.nextRoad, r2.nextRoad = r2, r3
    assert r1.countTimeCase1() == 4

    # All 3 red → 6 mins
    r1, r2, r3 = Road(), Road(), Road()
    r1.isGreenLight = r2.isGreenLight = r3.isGreenLight = False
    r1.nextRoad, r2.nextRoad = r2, r3
    assert r1.countTimeCase1() == 6

    print("Case 1: all tests passed")

def test_case2():
    # 1 green node, arrive t=0 → no flip → pass → 1 min
    r = Road()
    assert r.countTimeCase2() == 1

    # 1 red node, arrive t=0 → no flip → wait → 2 mins
    r = Road()
    r.isGreenLight = False
    assert r.countTimeCase2() == 2

    # 2 green nodes:
    #   node1: arrive t=0, green, no flip → pass → t=1
    #   node2: arrive t=1, green, flip→red → wait → t=3
    r1, r2 = Road(), Road()
    r1.nextRoad = r2
    assert r1.countTimeCase2() == 3

    # 3 green nodes:
    #   node1: arrive t=0 → pass → t=1
    #   node2: arrive t=1, flip→red → wait → t=3
    #   node3: arrive t=3, flip→red → wait → t=5
    r1, r2, r3 = Road(), Road(), Road()
    r1.nextRoad, r2.nextRoad = r2, r3
    assert r1.countTimeCase2() == 5

    print("Case 2: all tests passed")

def test_case3():
    # Linear path A→B→None, both green:
    #   A: t=0, green, pass → t=1
    #   B: t=1, green, flip→red, wait → t=3
    a, b = Road(), Road()
    a.nextRoads = [b]
    b.nextRoads = [None]
    assert a.countTimeCase3() == 3

    # Two paths from A: A→B→None (B green) and A→C→None (C red)
    #   Path via B: A(t=0,green,pass→t=1), B(t=1,green→flip→red,wait→t=3) → exit at 3
    #   Path via C: A(t=0,green,pass→t=1), C(t=1,red→flip→green,pass→t=2) → exit at 2
    #   Shortest: 2
    a, b, c = Road(), Road(), Road()
    c.isGreenLight = False
    a.nextRoads = [b, c]
    b.nextRoads = [None]
    c.nextRoads = [None]
    assert a.countTimeCase3() == 2

    # Single node with no children (immediate exit)
    a = Road()
    a.nextRoads = [None]
    assert a.countTimeCase3() == 1

    print("Case 3: all tests passed")


test_case1()
test_case2()
test_case3()
