# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:47:03 2019

@author: Vincent
"""

#this guy doesnt run because I ran out of time. Come back to fix it at around line 37

import requests

import apiKey
import championById
import summonerInfo
import userInput

playerid = summonerInfo.getAccountId()
key = apiKey.key
region = userInput.region

response = requests.get('https://'+region+'.api.riotgames.com/lol/match/v4/matchlists/by-account/' + playerid + '?api_key=' + key)
matchList = response.json()


matchInfo = []
#champions played by id
championsPlayed = {}
counter = 0

#for each match played
for a in matchList["matches"]:
    #if the champion has already been played, increment the statistic in match info.
    if (a["champion"] in championsPlayed):
        
    #if the champion has not been played, add the champion to championsPlayed and append new information to matchInfo
    else:
        matchInfo = requests.get('https://'+region+'.api.riotgames.com/lol/match/v4/matches/' + str(a['gameId']) + '?api_key=' + key)
        if 
        temp = {"champion" : championById[a["champion"]],
                "games" : 1,
                "wins" : }
        matchInfo.append()

for i in championById.champions:
    if matchesplayed[i] > 0:
        print(championById.champions[i] + ': ' + str(matchesplayed[i]))