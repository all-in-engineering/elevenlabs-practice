# ============================================================
# Problem: Multi-Step Cargo-to-Ship Assignment
#
# Assign a list of cargo items to a list of ships across three
# progressively harder steps.
#
# Input:
#   cargo  : list of weights, e.g. [10, 20, 30]
#   ships  : list of dicts, e.g. [{"capacity": 50, "overload": 0.2}, ...]
#            where overload is a decimal percentage (0.2 = 20%)
#
# Output:
#   A list of assignments, one per cargo item, where each value
#   is the index of the ship it was assigned to.
#   e.g. [0, 1, 0] means cargo[0] -> ship 0, cargo[1] -> ship 1, cargo[2] -> ship 0
#   Return [] if no valid assignment exists.
#
# ---------------------------------------------------------------
# Step 1: Ignore capacity
#   Assign all cargo to ships in any order, ignoring capacity.
#   Objective: distribute cargo as evenly as possible across ships.
#
#   Example:
#     cargo = [10, 20, 30], ships = [{"capacity": 100}, {"capacity": 100}]
#     Output: [0, 1, 0]  (or any balanced split)
#

def ignoreCapacity(weights, ships):
    assignments = []
    numShips = len(ships)
    for index in range(len(weights)):
        assignments.append(index % numShips)
    return assignments


# ---------------------------------------------------------------
# Step 2: Enforce capacity
#   Each ship has a capacity. Total weight assigned to a ship
#   must not exceed its capacity.
#   - Cargo items cannot be split across ships.
#   - If no valid assignment exists, return [].
#
#   Example:
#     cargo = [10, 20, 30], ships = [{"capacity": 30}, {"capacity": 40}]
#     [0, 0, 1]  => ship 0 gets 10+20=30, ship 1 gets 30 ✓

def enforceCapacity(weights, ships):
    return enforceCapacityHelper(weights, ships, [None] * len(weights), [0] * len(ships))

def enforceCapacityHelper(weights, ships, cargoAssigned, shipContents):
    if (weights == ([0] * len(weights))):
        return cargoAssigned
    else:
        for index in range(len(ships)):
            capacity = ships[index].get("capacity")
            for cargoIndex in range(len(weights)):
                if (weights[cargoIndex] == 0):
                    continue
                if weights[cargoIndex] + shipContents[index] <= capacity:
                    cargoAssigned[cargoIndex] = index
                    modifiedCargo = list(weights)
                    modifiedCargo[cargoIndex] = 0
                    modifiedShipContents = list(shipContents)
                    modifiedShipContents[index] += weights[cargoIndex]
                    answer = enforceCapacityHelper(modifiedCargo, ships, cargoAssigned, modifiedShipContents)
                    if answer == []:
                        continue
                    else:
                        return answer
        return []

# enforceCapacity tests
print(enforceCapacity([10, 20, 30], [{'capacity': 30}, {'capacity': 40}]))   # => [0, 0, 1]
print(enforceCapacity([10, 20, 30], [{'capacity': 10}, {'capacity': 10}]))   # => []
# backtracking test: greedy assigns 30 to ship 0, then can't fit 20 — must backtrack
print(enforceCapacity([30, 20, 10], [{'capacity': 30}, {'capacity': 30}]))   # => [0, 1, 1]

#
# ---------------------------------------------------------------
# Step 3: Per-ship overload with preference rule
#   Each ship has an overload percentage allowing it to carry up to:
#     max_load = capacity * (1 + overload)
#
#   Preference rule:
#     1. Prefer assignments where NO ship exceeds its base capacity.
#     2. Only allow overloaded ships if a non-overload solution is impossible.
#   When overload is necessary, minimize the number of overloaded ships.
#
#   Example:
#     cargo = [10, 40], ships = [{"capacity": 30, "overload": 0.5},
#                                {"capacity": 30, "overload": 0.5}]
#     Non-overload max per ship = 30. cargo[1]=40 exceeds all base capacities.
#     With overload: max = 30 * 1.5 = 45. Assign cargo[1] to any ship.
#     Output: [1, 0]  (1 overloaded ship)
#
# Constraints:
#   1 <= len(cargo) <= 100
#   1 <= len(ships) <= 20
#   1 <= cargo[i] <= 10^4
#   1 <= capacity <= 10^5
#   0.0 <= overload <= 1.0
# ============================================================


def enforceOverloadPreference(weights, ships):
    resultWithoutOverload = enforceWithoutOverload(weights, ships, [None] * len(weights), [0] * len(ships))
    if (resultWithoutOverload[3] == True):
        return resultWithoutOverload[1]
    else:
        newShipCapacity = list(ships)
        for index in range(len(ships)):
            newShipCapacity[index]["capacity"] = ships[index].get("capacity") * (1 + ships[index].get("overload"))
            
        withOverload = enforceWithoutOverload(resultWithoutOverload[0], newShipCapacity, resultWithoutOverload[1], resultWithoutOverload[2])
        if (withOverload[3] == True):
            return withOverload[1]
        else:
            return []

def enforceWithoutOverload(weights, ships, cargoAssigned, shipContents):
    if (weights == ([0] * len(weights))):
        return [weights, cargoAssigned, shipContents, True]
    else:
        for index in range(len(ships)):
            capacity = ships[index].get("capacity")
            for cargoIndex in range(len(weights)):
                if (weights[cargoIndex] == 0):
                    continue
                if weights[cargoIndex] + shipContents[index] <= capacity:
                    cargoAssigned[cargoIndex] = index
                    modifiedCargo = list(weights)
                    modifiedCargo[cargoIndex] = 0
                    modifiedShipContents = list(shipContents)
                    modifiedShipContents[index] += weights[cargoIndex]
                    answer = enforceWithoutOverload(modifiedCargo, ships, cargoAssigned, modifiedShipContents)
                    if answer[2] == False:
                        continue
                    else:
                        return answer
        return [weights, cargoAssigned, shipContents, False]