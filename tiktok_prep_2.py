# TikTok Interview Prep 2

# Given a string representing an IPv4 address, determine if it is valid.
# An IPv4 address consists of four octets, each can range from 0 to 255, separated by a ".".
# Implement a function isValidIPv4(address: str) -> bool to validate the IPv4 address.
# Return True if the address is valid, otherwise return False.
# Note that the delimiter between bytes is ".".
#
# Example test cases:
# assert isValidIPv4("255.255.11.135") == True
# assert isValidIPv4("-1.255.11.135") == False
# assert isValidIPv4("256.255.11.135") == False
# assert isValidIPv4("255.255.11.256") == False
# assert isValidIPv4("255.255.11.") == False

def isValidIPv4(address):
    #1. split by periods
    splitAddress = address.split(".")

    #2. make sure there are 4 parts
    if (len(splitAddress) != 4):
        return False
    #3. make sure each are all integers and positive

    for octet in splitAddress:
        try:
            integerOctet = int(octet)
            #4. make sure each one ranges from 1 to 255 inclusive
            if integerOctet >= 0 and integerOctet <= 255:
                continue
            else:
                return False
        except ValueError:
            return False

    return True

assert isValidIPv4("255.255.11.135") == True
assert isValidIPv4("-1.255.11.135") == False
assert isValidIPv4("256.255.11.135") == False
assert isValidIPv4("255.255.11.256") == False
assert isValidIPv4("255.255.11.") == False
print("All tests passed!")

# Given a string consisting only of digits, restore it by returning all possible valid IPv4 addresses.
# Insert dots into the input string to form a valid IPv4 address where each byte is between 0 and 255.
# Segments with leading zeros are invalid.
# Implement a function restoreIpAddresses(s: str) -> List[str] to return the list of possible IP addresses.
#
# Example test cases:
# assert set(restoreIpAddresses("25525511135")) == set([
#     "255.255.11.135",
#     "255.255.111.35"
# ])
# assert restoreIpAddresses("0002555") == []

def restoreIpAddresses(inputString):
    return restoreIpAddressesHelper(inputString, "", "", set())

#1. returns a set of all validIP's with the input's starting position

def restoreIpAddressesHelper(inputString, currentOctet, ipAddressSoFar, validAddressesSeen):

    if (len(ipAddressSoFar)) > 0 and ipAddressSoFar[0] == ".":
        ipAddressSoFar = ipAddressSoFar[1:]

    #1. exit condition, if inputString is "" and currentOctet is also empty, and octetsofar is valid, add to  validOctets and return
    if (inputString == "" and currentOctet == "" and isValidIPv4(ipAddressSoFar)):
        validAddressesSeen.add(ipAddressSoFar)
        return validAddressesSeen
    
    #2. exit condition, if input string is "" and currentOctet is valid, call this function agains with it appended to ipAddressSoFar
    if (inputString == "" and currentOctet != "" and int(currentOctet) >= 0 and int(currentOctet) <= 255 and isValidIPv4(ipAddressSoFar + "." + currentOctet)):
        validAddressesSeen.add(ipAddressSoFar + "." + currentOctet)
        return validAddressesSeen
    
    #3. beginning with 0
    if (len(inputString) > 0 and currentOctet == "" and inputString[0] == "0"):
        validAddressesSeen.update(restoreIpAddressesHelper(inputString[1:], "", ipAddressSoFar + "." + "0", validAddressesSeen))
    
    if (len(inputString) > 0 and currentOctet == "" and inputString != "" and inputString[0] != "0"):
        validAddressesSeen.update(restoreIpAddressesHelper(inputString[1:], inputString[0], ipAddressSoFar, validAddressesSeen))

    #4. currentOctet is valid
    if (currentOctet != "" and int(currentOctet) >= 0 and int(currentOctet) <= 255):
        validCombos = restoreIpAddressesHelper(inputString, "", ipAddressSoFar + "." + currentOctet, validAddressesSeen)
        validAddressesSeen.update(validCombos)

    #5. adding another number is valid from inputString
    if (len(inputString) > 0 and currentOctet != "" and int(currentOctet + inputString[0]) >= 0 and int(currentOctet + inputString[0]) <= 255):
        validCombos = restoreIpAddressesHelper(inputString[1:], currentOctet + inputString[0], ipAddressSoFar, validAddressesSeen)
        validAddressesSeen.update(validCombos)

    if not validAddressesSeen:
        return []
    return validAddressesSeen

assert restoreIpAddresses("0000") == {"0.0.0.0"}
assert restoreIpAddresses("1111") == {"1.1.1.1"}
assert set(restoreIpAddresses("25525511135")) == set([
    "255.255.11.135",
    "255.255.111.35"
])
assert restoreIpAddresses("0002555") == []
print("restoreIpAddresses tests passed!")
