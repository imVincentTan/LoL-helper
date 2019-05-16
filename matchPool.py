# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:57:51 2019

@author: Vincent
"""

# continue here
import requests

import userInput
import apiKey

key = apiKey.key
region = userInput.region
queue = 'RANKED_SOLO_5x5'
tier = 'DIAMOND'
division = 'I'

players = requests.get('https://'+region+'.api.riotgames.com/lol/league/v4/entries/'+queue+'/'+tier+'/'+division+'?api_key='+key).json()
numPlayers = len(players)

#pick a player
#pick most recent match.
#if most recent match is accounted for, pick next match
#add matchId to (dict)matches

for playerInfo in players[:10]:
    #gets the summonerId
    print(playerInfo)
    summonerId = playerInfo['summonerId']
    summonerInfo = requests.get('https://'+region+'.api.riotgames.com/lol/summoner/v4/summoners/'+summonerId+'?api_key='+key).json()
    accountId = summonerInfo['accountId']