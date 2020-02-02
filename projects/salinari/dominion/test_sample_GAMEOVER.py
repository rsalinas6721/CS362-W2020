import Dominion
import random
import testUtility_GAMEOVER
from collections import defaultdict


cardNames = [
    "Woodcutter", "Smithy", "Laboratory", "Village", "Festival",
    "Market", "Chancellor", "Workshop", "Moneylender", "Chapel",
    "Cellar", "Remodel", "Adventurer", "Feast", "Mine",
    "Library", "Gardens", "Moat", "Council Room", "Witch",
    "Bureaucrat", "Militia", "Spy", "Thief", "Throne Room"
    ]


'''
TESTING THE PROPER USAGE OF "GAMEOVER" FUNCTION
'''
def test_GAMEOVER():
    player = testUtility_GAMEOVER.players[0]
    gameexit = Dominion.gameover(testUtility_GAMEOVER.supply)
    assert(gameexit == False)
    for i in range(0, 12):
        player.deck.insert(0,testUtility_GAMEOVER.supply["Province"].pop())
    gameexit = Dominion.gameover(testUtility_GAMEOVER.supply)
    assert(gameexit == True)
