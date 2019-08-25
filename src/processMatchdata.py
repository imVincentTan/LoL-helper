# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:07:54 2019

@author: Vincent
"""

#takes riot match seed data and processes it.

import championById

import json

#key: championAName_championBName
#value: # times championA won against championB
aVsBWins = {}
totalMatches = 0

for counter in range(1,11):
    with open('matchdata/matches' + str(counter) + '.json') as tempinput:
        tempdata = json.load(tempinput)
    
    for match in tempdata['matches']:
        winTeamChampions = []
        loseTeamChampions = []
        
        #get winning team ID
        if match['teams'][0]['win'] == 'Win':
            winTeamID = match['teams'][0]['teamId']
        else:
            winTeamID = match['teams'][1]['teamId']
        
        #store champion names into aTeamChampions and bTeamChampions
        for participantCounter in match['participants']:
            if participantCounter['teamId'] == winTeamID:
                winTeamChampions.append(championById.champions[participantCounter['championId']])
            else:
                loseTeamChampions.append(championById.champions[participantCounter['championId']])
        
        for winChamp in winTeamChampions:
            for loseChamp in loseTeamChampions:
                if winChamp + '_' + loseChamp in aVsBWins:
                    aVsBWins[winChamp + '_' + loseChamp] += 1
                else:
                    aVsBWins[winChamp + '_' + loseChamp] = 1
                    
        #increment totalMatches
        totalMatches += 1

def champInfo(myChamp):
    wins = 0
    losses = 0
    timesPicked = 0
    
    for opponentChampKey in championById.champions:
        if myChamp + '_' + championById.champions[opponentChampKey] in aVsBWins:
            temp = aVsBWins[myChamp + '_' + championById.champions[opponentChampKey]]
            wins += temp
            timesPicked += temp
        if championById.champions[opponentChampKey] + '_' + myChamp in aVsBWins:
            temp = aVsBWins[championById.champions[opponentChampKey] + '_' + myChamp]
            losses += temp
            timesPicked += temp
        
    if wins + losses > 0:
        winRate = wins/(wins+losses)
    else:
        winRate = 0
            
    timesPicked /= 5
    
    return {'pick rate': timesPicked/totalMatches,
            'win rate': winRate}

def aVsBWinRate(aChamp, bChamp):
    if aChamp + '_' + bChamp in aVsBWins:
        wins = aVsBWins[aChamp + '_' + bChamp]
    else:
        wins = 0
    
    if bChamp + '_' + aChamp in aVsBWins:
        losses = aVsBWins[bChamp + '_' + aChamp]
    else:
        losses = 0
    
    if wins + losses > 0:
        return wins/(wins+losses)
    else:
        #this matchup has never happened. 0.5 is fair
        return 0.5




#testing
#print(champInfo('Ahri'))
#print(aVsBWinRate('Ahri','Zed'))
