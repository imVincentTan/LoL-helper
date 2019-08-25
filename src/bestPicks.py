# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:15:47 2019

@author: Vincent
"""

#pick the champion among player champion pool that has the highest cumulative win rate against currently picked enemy team composition

import userInput
import processMatchdata

orderedBestChampion = []

for champ in userInput.championPool:
    if not (champ in userInput.enemyTeam):
        orderedBestChampion.append([champ,0])
        for enemy in userInput.enemyTeam:
            orderedBestChampion[-1][1] += processMatchdata.aVsBWinRate(champ,enemy)
            

orderedBestChampion.sort(key=lambda x: x[1], reverse = True)

print(orderedBestChampion)
    
