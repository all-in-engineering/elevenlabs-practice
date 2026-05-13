# ============================================================
# Problem: Simplified Splendor (Single Player)
#
# Build a simplified one-player version of the board game Splendor,
# implemented in three progressive parts. No test cases are provided —
# you must write your own.
#
# Token colors: Yellow, Green, Blue, Red, White
#
# ---------------------------------------------------------------
# Part 1: can_purchase(player, card)
#
#   Determine if a player can afford a card based on their tokens.
#
#   - player: dict mapping color -> token count
#     e.g. {"R": 2, "B": 3, "W": 1, "G": 0, "Y": 0}
#
#   - card cost: dict mapping color -> required amount
#     e.g. {"R": 1, "B": 2, "W": 3}  (represents "1R, 2B, 3W")
#
#   - Return True if the player has enough tokens for every color,
#     False otherwise.
#
#   Write test cases for:
#     - player has exactly enough tokens
#     - player has more than enough
#     - player is short on one color
#     - card costs nothing (empty cost)
#     - player has no tokens
#
# ---------------------------------------------------------------


def can_purchase(player, card):
    card_types_owned = player.get("card_type_count", {})
    for tokenType in card:
        if tokenType == "type":
            continue
        cardType = card.get("type")
        tokenCost = card.get(tokenType)
        discount = card_types_owned.get(cardType, 0)

        if cardType != tokenType:
            discount = 0

        if tokenCost-discount > player.get(tokenType, 0):
            return False
    return True

testPlayerHand = {"R": 2, "B": 3, "W": 1}
testCardCost = {"R": 2, "B": 3, "W": 1, "type": "G"}

print("testing equal tokens")
print(can_purchase(testPlayerHand, testCardCost))

print("testing more than enough tokens")

testPlayerHand = {"R": 3, "B": 4, "W": 2}
testCardCost = {"R": 2, "B": 3, "W": 1, "type": "G"}
print(can_purchase(testPlayerHand, testCardCost))

print("lacking one token")
testPlayerHand = {"R": 2, "B": 2, "W": 1}
testCardCost = {"R": 2, "B": 3, "W": 1, "type": "B"}
print(can_purchase(testPlayerHand, testCardCost))

print("test free card")
testPlayerHand = {"R": 2, "B": 2, "W": 1}
testCardCost = {}
print(can_purchase(testPlayerHand, testCardCost))

print("test no tokens")
testPlayerHand = {}
testCardCost = {"R": 2, "B": 2, "W": 1, "type": "G"}
print(can_purchase(testPlayerHand, testCardCost))

# Part 2: purchase(player, card)
#
#   If the player can afford the card, deduct the token cost and
#   add the card to the player's collection.
#
#   - Deduct tokens spent from the player's token counts.
#   - Track purchased cards on the player (e.g. player["cards"]).
#   - Return True if purchase succeeded, False if not affordable.
#
#   Write test cases for:
#     - successful purchase reduces tokens correctly
#     - failed purchase leaves tokens unchanged
#     - player can purchase multiple cards in sequence
#     - purchasing a card adds it to player's card collection
#
# ---------------------------------------------------------------

def purchase(player, card):
    if (can_purchase(player, card)):
        for tokenType in card:
            if tokenType == "type":
                continue
            tokenCost = card.get(tokenType)
            playerDiscount = player.get("card_type_count", {}).get(tokenType, 0)
            actualCost = tokenCost - playerDiscount
            player[tokenType] = player.get(tokenType) - actualCost

        cardsOwned = player.get("cards", [])
        cardsOwned.append(card)
        player["cards"] = cardsOwned

        card_type = card.get("type")

        card_types_owned = player.get("card_type_count", {}).get(card_type, 0)
        if player.get("card_type_count") is None:
            player["card_type_count"] = {}
        player["card_type_count"][card_type] = card_types_owned + 1

        return True
    else:
        return False
    
    
testPlayerHand = {"R": 2, "B": 3, "W": 1}
testCardCost = {"R": 2, "B": 3, "W": 1, "type": "G"}

print("testing successful purchase")
print(purchase(testPlayerHand, testCardCost))
print("playerhand: " + str(testPlayerHand.get("cards")))
print("playertokens: " + str(testPlayerHand))


print("lacking one token")
testPlayerHand = {"R": 2, "B": 2, "W": 1}
testCardCost = {"R": 2, "B": 3, "W": 1, "type": "G"}
print(purchase(testPlayerHand, testCardCost))
print("playerhand: " + str(testPlayerHand.get("cards")))
print("playertokens: " + str(testPlayerHand))



print("test multiple purchases")
testPlayerHand = {"R": 4, "B": 6, "W": 1}
testCardCost = {"R": 2, "B": 3, "W": 1, "type": "W"}
purchase(testPlayerHand, testCardCost)
purchase(testPlayerHand, testCardCost)
print("playerhand: " + str(testPlayerHand.get("cards")))
print("playertokens: " + str(testPlayerHand))



# Part 3: Cards as coupons
#
#   Each card has a color. Owned cards act as permanent discounts:
#   each card of a color reduces the token cost of that color by 1
#   (minimum 0).
#
#   Example:
#     player has 2 Green cards
#     card cost: {"R": 1, "G": 4, "W": 3}
#     effective cost: {"R": 1, "G": 2, "W": 3}  (4G - 2 cards = 2G)
#
#   Update can_purchase and purchase to apply card discounts before
#   checking/spending tokens.
#
#   Write test cases for:
#     - discount reduces cost exactly to 0 for one color
#     - discount would go negative — clamp to 0, not negative
#     - card discount makes an otherwise unaffordable card affordable
#     - multiple colors discounted at once
#     - no cards owned (discount has no effect)
# ============================================================
