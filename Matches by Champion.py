import requests
from numpy import zeros

import apiKey
import championById
import summonerInfo
import userInput
#response = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Icarus142?api_key=RGAPI-65b1396f-57f0-4faa-be9d-b3cc1ecff0d2')
#print((response.content.decode("utf-8")).replace(',','\n'))

playerid = summonerInfo.getAccountId()
key = apiKey.key
region = userInput.region

response = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + playerid + '?api_key=' + key)
data = response.json()

#init something? 
matchesplayed = zeros([600],dtype=int)

#for each 
for i in data["matches"]:
    x = i["champion"]
    matchesplayed[x] = matchesplayed[x] + 1

for i in championById.champions:
    if matchesplayed[i] > 0:
        print(championById.champions[i] + ': ' + str(matchesplayed[i]))