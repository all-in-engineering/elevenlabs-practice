# Anthropic Interview Prep

# A gym wants to track how long each member spends inside the facility. Members can be added to the system,
# and each visit is recorded by scanning their membership card when they enter and when they leave.
#
# Each scan toggles the member's current status:
#   If the member is outside, the scan means they entered
#   If the member is inside, the scan means they left
#
# Only completed visits count toward the member's total time. Each member stores:
#   membership ID
#   membership tier
#   monthly fee
#   current visit start time
#   total completed visit time
#   whether they are currently inside the gym
#
# Implement the GymAccessSystem class:
#   GymAccessSystem() initializes an empty system.
#   boolean addMember(String memberId, String tier, int monthlyFee) adds a new member with the given tier and monthly fee.
#     Returns true if the member was added successfully.
#     Returns false if the member already exists.
#   String scan(String memberId, int timestamp) registers an entry or exit scan for the member. Returns:
#     "registered" if the scan is valid
#     "invalid_request" if the member does not exist
#   int getTotalTime(String memberId) returns the total time from completed visits only.
#     If the member does not exist, return -1.
#
# Rules:
#   Scan calls are given in increasing timestamp order
#   An unfinished visit does not count until the member scans out
#   memberId and tier contain only English letters and spaces

class GymAccessSystem:

    def __init__(self):
        self.membershipMap = {}
    
    def addMember(self, memberId, tier, monthlyFee):
        if (memberId in self.membershipMap):
            return False
        else:
            self.membershipMap[memberId] = {"tier": tier, "monthlyFee": monthlyFee, "access_time": None, "type": None, "total_time": 0}
            return True

    def scan(self, memberId, timestamp):
        if (memberId not in self.membershipMap):
            return "invalid_request"
        if (self.membershipMap[memberId]["access_time"] is None): 
            self.membershipMap[memberId]["access_time"] = timestamp
            self.membershipMap[memberId]["type"] = "check_in"
            return "registered"
        lastAccess = self.membershipMap[memberId]["type"]
        if lastAccess == "check_in":
            checkinTime = self.membershipMap[memberId]["access_time"]
            sessionTime = timestamp - checkinTime
            self.membershipMap[memberId]["total_time"] = self.membershipMap[memberId]["total_time"] + sessionTime
            self.membershipMap[memberId]["type"] = "check_out"
            self.membershipMap[memberId]["timestamp"] = timestamp
        else: 
            self.membershipMap[memberId]["type"] = "check_in"
            self.membershipMap[memberId]["timestamp"] = timestamp

        return "registered"
    
    def getTotalTime(self, memberId):
        if (memberId not in self.membershipMap):
            return -1
        else:
            return self.membershipMap[memberId]["total_time"]

# Tests for addMember
gym = GymAccessSystem()

print(gym.addMember("alice", "gold", 100))   # True
print(gym.addMember("alice", "gold", 100))   # False
print(gym.addMember("bob", "silver", 50))    # True
print(gym.addMember("bob", "silver", 50))    # False

# Tests for scan
print("\n--- scan tests ---")

# Scan a member that doesn't exist
print(gym.scan("charlie", 100))              # "invalid_request"

# First scan for alice (entry)
print(gym.scan("alice", 100))               # "registered"
print(gym.membershipMap["alice"])           # {..., "type": "check_in", "access_time": 100, "total_time": 0}

# Second scan for alice (exit)
print(gym.scan("alice", 200))              # "registered"
print(gym.membershipMap["alice"])          # {..., "type": "check_out", "total_time": 100}

# Tests for getTotalTime
print("\n--- getTotalTime tests ---")

gym2 = GymAccessSystem()
gym2.addMember("alice", "gold", 100)

# After first check-in, total time should be 0 (no completed visits)
gym2.scan("alice", 100)
print(gym2.getTotalTime("alice"))          # 0

# After check-out, total time should be the difference
gym2.scan("alice", 200)
print(gym2.getTotalTime("alice"))          # 100

# After next check-in, total time should still be 100 (visit not completed yet)
gym2.scan("alice", 300)
print(gym2.getTotalTime("alice"))          # 100
