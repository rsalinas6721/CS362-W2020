import Dominion
import random
import testUtility_ACTION
from collections import defaultdict


cardNames = [
    "Woodcutter", "Smithy", "Laboratory", "Village", "Festival",
    "Market", "Chancellor", "Workshop", "Moneylender", "Chapel",
    "Cellar", "Remodel", "Adventurer", "Feast", "Mine",
    "Library", "Gardens", "Moat", "Council Room", "Witch",
    "Bureaucrat", "Militia", "Spy", "Thief", "Throne Room"
    ]


'''
TESTING THE PROPER USAGE OF "USE" FUNCTION
'''
def test_ACTION_use():
    player = testUtility_ACTION.players[0]
    player.hand.pop()
    player.hand.insert(0,testUtility_ACTION.supply["Woodcutter"].pop())
    numHandBefore = 0
    for c in player.hand:
        numHandBefore += 1
    c = Dominion.getcard("Woodcutter",testUtility_ACTION.supply,player.hand,"your hand")
    c.use(player, testUtility_ACTION.trash)
    numHandAfter = 0
    for c in player.hand:
        numHandAfter += 1
    assert(numHandAfter == (numHandBefore - 1))


'''
TESTING THE PROPER USAGE OF "AUGMENT" FUNCTION
'''
def test_ACTION_augment():
    player = testUtility_ACTION.players[1]
    player.hand.pop()
    player.hand.insert(0,testUtility_ACTION.supply["Woodcutter"].pop())
    numHandBefore = 0
    c = Dominion.getcard("Woodcutter", testUtility_ACTION.supply, player.hand,"your hand")
    player.actions = 1
    player.buys = 1
    player.purse = 5
    player.coins = 2
    c.augment(player)
    assert(player.actions == 1)
    assert(player.buys == 2)
    assert(player.purse == 7)
    assert(player.coins == 2)
