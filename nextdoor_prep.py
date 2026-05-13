# ============================================================
# Problem: Compare Version Numbers
#
# Given two version strings version1 and version2, each consisting
# of one or more numeric revisions separated by dots '.', compare them.
#
# Return:
#    1 if version1 > version2
#   -1 if version1 < version2
#    0 if version1 == version2
#
# Notes:
#   - Revisions are compared numerically (not lexicographically)
#   - Leading zeros are ignored: "1.01" == "1.001" == "1.1"
#   - Missing revisions are treated as 0: "1.0" == "1.0.0"
#   - Version strings support any number of segments
#
# Examples:
#   version1 = "1.0.1", version2 = "1"       => 1
#   version1 = "7.5.2.4", version2 = "7.5.3" => -1
#   version1 = "1.01", version2 = "1.001"    => 0
#   version1 = "1.0", version2 = "1.0.0"     => 0
# ============================================================

def compareVersions(version1, version2):
    splitVersion1 = version1.split(".")
    splitVersion2 = version2.split(".")

    while (True):
        if (len(splitVersion1) == 0 and len(splitVersion2) == 0):
            return 0
        elif (len(splitVersion1) == 0):
            version2 = splitVersion2.pop(0)
            if version2 == "0":
                continue
            else: 
                return -1
        
        elif (len(splitVersion2) == 0):
            version1 = splitVersion1.pop(0)
            if version1 == "0":
                continue
            else: 
                return 1
     
        else: 
            currentVersion1 = int(splitVersion1[0])
            currentVersion2 = int(splitVersion2[0])
            if currentVersion1 > currentVersion2:
                return 1
            elif currentVersion1 < currentVersion2:
                return -1
            splitVersion1.pop(0)
            splitVersion2.pop(0)

print(compareVersions("1.0.1", "1" ))
print(compareVersions("7.5.2.4", "7.5.3" ))
print(compareVersions("1.01", "1.001" ))
print(compareVersions("1.0", "1.0.0" ))