# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:47:03 2019

@author: Vincent
"""

#takes a while to load, but code is O(n) 
#Need to figure out how to handle efficiently calling the API to reduce runtime.
#complexity breakdown: (getWinRate)
#

import requests

import apiKey
import championById
import summonerInfo
import userInput

playerId = summonerInfo.getAccountId()
key = apiKey.key
region = userInput.region

def getWinrate():
    response = requests.get('https://'+region+'.api.riotgames.com/lol/match/v4/matchlists/by-account/' + playerId + '?api_key=' + key)
    matchList = response.json()
    
    championInfo = []
    #key:value = championId:index value in championInfo
    #note will be obsolete after sorting championInfo
    championsPlayed = {}
    championsPlayedInd = 0
    
    #for each match played
    for ind, matchCount in enumerate(matchList["matches"]):
        #this is to make sure we don't exceed the api call rate limit. 
        if ind >= 50:
            break
        #The information for the specific match the player played
        response = requests.get('https://'+region+'.api.riotgames.com/lol/match/v4/matches/' + str(matchCount['gameId']) + '?api_key=' + key)
        matchInfo = response.json()
        #Finding the participantId
        for participantCount in matchInfo["participantIdentities"]:
            if participantCount['player']['currentAccountId'] == playerId:
                participantId = participantCount['participantId']
        #determining whether the player won or lost.
        playerWon = False
        for participantCount in matchInfo['participants']:
            if participantCount['participantId'] == participantId:
                if participantCount['stats']['win']:
                    playerWon = True
                    break
                break
                        
        #if the champion has already been played, increment the statistic in match info.
        if (matchCount["champion"] in championsPlayed):
            championInfo[championsPlayed[matchCount['champion']]]['games'] += 1
            if playerWon:
                championInfo[championsPlayed[matchCount['champion']]]['wins'] += 1
            else:
                championInfo[championsPlayed[matchCount['champion']]]['losses'] += 1
        
        #if the champion has not been played, add the champion to championsPlayed and append new information to matchInfo
        else:
            #if the player won
            if playerWon:
                temp = {'champion' : championById.champions[matchCount['champion']],
                    'games' : 1,
                    'wins' : 1,
                    'losses' : 0,
                    'winrate' : 1}
            #if the player lost
            else:
                temp = {'champion' : championById.champions[matchCount['champion']],
                    'games' : 1,
                    'wins' : 0,
                    'losses' : 1,
                    'winrate' : 0}
            championInfo.append(temp)
            championsPlayed[matchCount['champion']] = championsPlayedInd
            championsPlayedInd += 1
    
    #calculate winrates
    for champion in championInfo:
        champion['winrate'] = champion['wins']/champion['games']
    return championInfo

def sortChampionName(championInfo):
    championInfo.sort(key = lambda x: x['champion'])

def sortNumGames(championInfo):
    championInfo.sort(key = lambda x: x['games'], reverse = True)

def sortWins(championInfo):
    championInfo.sort(key = lambda x: x['wins'], reverse = True)

def sortWinrate(championInfo):
    championInfo.sort(key = lambda x: x['winrate'], reverse = True)
#testing

printval = getWinrate()
sortChampionName(printval)
print(printval)
sortNumGames(printval)
print(printval)
sortWins(printval)
print(printval)
sortWinrate(printval)
print(printval)