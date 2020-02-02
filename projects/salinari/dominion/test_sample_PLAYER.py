import Dominion
import random
import testUtility_PLAYER
from collections import defaultdict


cardNames = [
    "Woodcutter", "Smithy", "Laboratory", "Village", "Festival",
    "Market", "Chancellor", "Workshop", "Moneylender", "Chapel",
    "Cellar", "Remodel", "Adventurer", "Feast", "Mine",
    "Library", "Gardens", "Moat", "Council Room", "Witch",
    "Bureaucrat", "Militia", "Spy", "Thief", "Throne Room"
    ]


'''
TESTING THE PROPER USAGE OF "ACTION_BALANCE" FUNCTION
'''
def test_PLAYER_actionBalance():
    player = testUtility_PLAYER.players[2]
    player.hand.pop()
    player.hand.insert(0,testUtility_PLAYER.supply["Woodcutter"].pop())
    numHandBefore = 0
    c = Dominion.getcard("Woodcutter", testUtility_PLAYER.supply,player.hand,"your hand")
    num = player.action_balance()
    assert(num == -7.0)


'''
TESTING THE PROPER USAGE OF "CALCPOINTS" FUNCTION
'''
def test_PLAYER_calcPoints():
    player = testUtility_PLAYER.players[3]
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())

    player.deck.pop()
    player.deck.pop()
    player.deck.pop()
    player.deck.pop()
    player.deck.pop()
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())

    num = player.calcpoints()
    assert(num == 5)


'''
TESTING THE PROPER USAGE OF "DRAW" FUNCTION
'''
def test_PLAYER_draw():
    player = testUtility_PLAYER.players[4]
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.draw()
    numCards = 0
    for c in player.hand:
        numCards += 1
    assert(numCards == 1)


'''
TESTING THE PROPER USAGE OF "CARDSUMMARY" FUNCTION
'''
def test_PLAYER_cardSummary():
    player = testUtility_PLAYER.players[5]
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.pop()
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Silver"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.hand.insert(0,testUtility_PLAYER.supply["Estate"].pop())

    player.deck.pop()
    player.deck.pop()
    player.deck.pop()
    player.deck.pop()
    player.deck.pop()
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())
    player.deck.insert(0,testUtility_PLAYER.supply["Estate"].pop())

    cardsum = {}
    cardsum[player.name]=player.cardsummary()
    for sec in cardsum:
        name = sec
    car = player.cardsummary()
    cardNameOne = car.get("Estate")
    cardNameTwo = car.get("Silver")
    vicPoints = car.get("VICTORY POINTS")
    assert(name == "Vick")
    assert(cardNameOne == 7)
    assert(cardNameTwo == 3)
    assert(vicPoints == 7)
