# -*- coding: utf-8 -*-
"""
Created on Sunday Jan 12 14:50:00 2020

@author: salinari
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

'''
# REFACTORED CODE
    This portion of the refactored code utilises the testUtility python script
'''
box = testUtility.GetBoxes(nV)
#Define box

supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]

'''
# REFACTORED CODE
    random.shuffle(boxlist) was commented out
    Game Box is not shuffled and in turn will cause the cards to consistently remain the same throughout miultiple games.
'''
#random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])


#The supply always has these cards
supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
supply["Silver"]=[Dominion.Silver()]*40
supply["Gold"]=[Dominion.Gold()]*30
supply["Estate"]=[Dominion.Estate()]*nV
supply["Duchy"]=[Dominion.Duchy()]*nV


'''
# REFACTORED CODE
    supply["Province"]=[Dominion.Province()]*nV was refactored to supply["Province"]=[Dominion.Province()]*1
    This bug maeks the game only have 1 Province card available.
'''
supply["Province"]=[Dominion.Province()]*1
supply["Curse"]=[Dominion.Curse()]*nC

#initialize the trash
trash = []

#Costruct the Player objects
players = []
for name in player_names:
    if name[0]=="*":
        players.append(Dominion.ComputerPlayer(name[1:]))
    elif name[0]=="^":
        players.append(Dominion.TablePlayer(name[1:]))
    else:
        players.append(Dominion.Player(name))

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
