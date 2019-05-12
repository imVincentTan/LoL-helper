# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:13:50 2019

@author: Vincent
"""

import requests

import apiKey
import userInput

#user input
summonerName = userInput.summonerName
region = userInput.region

#riot API key
key = apiKey.key

#default player information (Rito Vincent)
response = requests.get('https://'+region+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+summonerName+'?api_key='+key)
data = response.json()
    
#fetches information from riot API and puts it in data    
def fetchAccountData():
    response = requests.get('https://'+region+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+summonerName+'?api_key='+key)
    data = response.json()

#returns accountId of player
def getAccountId():
    return data["accountId"]