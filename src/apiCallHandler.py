# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:41:58 2019

@author: Vincent
"""

import datetime
import time
import math
import requests

requestTimeList = [[],[]]
requestPerTimeList = [[20,1],[100,120]]

second = datetime.timedelta(seconds=1)
twoMinutes = datetime.timedelta(seconds=2)

def preAPICall():
    #check if we need to delay, and delay if needed
    tempnow = datetime.datetime.now()
    for ind, a in enumerate(requestTimeList):
        if len(a) >= requestPerTimeList[ind][0] and a[0] >= tempnow:
            time.sleep(math.ceil(a[0]-tempnow).total_seconds())
            
    #clean up requestTimeList to not include any times that have past
    for a in requestTimeList:
        for ind, b in enumerate(a):
            if b < tempnow:
                a.pop(ind)

def postAPICall():
    #add endtimes to requestTimeList
    tempnow = datetime.datetime.now()
    for ind, a in enumerate(requestTimeList):
        a.append(tempnow+datetime.timedelta(seconds=requestPerTimeList[ind][1]))



def callAPI(callType):
    callTypes = {'playerInfo'}
    if callType in callTypes:
        preAPICall()
        #call the API and do something useful with it
            
    
    
        postAPICall()
    
    
    

    
    return 0


