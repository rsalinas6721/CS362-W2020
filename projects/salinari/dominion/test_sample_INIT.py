import Dominion
import random
import testUtility_INIT
from collections import defaultdict


cardNames = [
    "Woodcutter", "Smithy", "Laboratory", "Village", "Festival",
    "Market", "Chancellor", "Workshop", "Moneylender", "Chapel",
    "Cellar", "Remodel", "Adventurer", "Feast", "Mine",
    "Library", "Gardens", "Moat", "Council Room", "Witch",
    "Bureaucrat", "Militia", "Spy", "Thief", "Throne Room"
    ]

'''
TESTING THE RIGHT AMOUNT OF PLAYERS
'''
def test_players():
    assert len(testUtility_INIT.player_names) == 3

'''
TESTING THE CONTENTS OF THE BOX
'''
def test_box():
    assert len(testUtility_INIT.box) == 25
    boxValidation = 0
    for name in cardNames:
        if testUtility_INIT.box[name]:
            boxValidation += 1
    assert(boxValidation == 25)

'''
TESTING THE CONTENTS OF THE SUPPLY
'''
def test_supply():
    assert len(testUtility_INIT.supply) == 17
    assert(len(testUtility_INIT.supply["Copper"])) == 39
    assert(len(testUtility_INIT.supply["Silver"])) == 40
    assert(len(testUtility_INIT.supply["Gold"])) == 30
    assert(len(testUtility_INIT.supply["Estate"])) == 12
    assert(len(testUtility_INIT.supply["Duchy"])) == 12
    assert(len(testUtility_INIT.supply["Province"])) == 12
    assert(len(testUtility_INIT.supply["Curse"])) == 20

    for names in cardNames:
        if testUtility_INIT.supply[names]:
            if names == "Gardens":
                assert(len(testUtility_INIT.supply[names])) == 12
            else:
                assert(len(testUtility_INIT.supply[names])) == 10

'''
TESTING THE PROPER DISTRIBUTION OF COINS
'''
def test_coins():
    for player in testUtility_INIT.players:
        copper = 0
        for c in player.hand:
            if((c.name) == 'Copper'):
                copper += 1
        for d in player.deck:
            if((d.name) == 'Copper'):
                copper += 1
        assert(copper == 7), player.name + " did not receive the Copper. "

    for player in testUtility_INIT.players:
        silver = 0
        for c in player.hand:
            if((c.name) == 'Silver'):
                silver += 1
        for d in player.deck:
            if((d.name) == 'Silver'):
                silver += 1
        assert(silver == 0), player.name + " did received Silver. "

    for player in testUtility_INIT.players:
        gold = 0
        for c in player.hand:
            if((c.name) == 'Gold'):
                gold += 1
        for d in player.deck:
            if((d.name) == 'Gold'):
                gold += 1
        assert(gold == 0), player.name + " did received Gold. "
