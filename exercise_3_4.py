'''
Created on Feb 14, 2018

@author: fangyunzhao
'''

import random

def repTrails(numberBlock, LeftRight, numberTask):
    trailList = []
    for x in range(1, numberBlock + 1):
        blockList = []
        for y in range(numberTask/2):
            if y < 2:
                for l in LeftRight:
                    a = ''.join([str(x), ',','Mask',',',l])
                    blockList.append(a)
                    #print a
            else:
                for l in LeftRight:
                    a = ''.join([str(x), ',','NonMask',',',l])
                    blockList.append(a)
                    #print a
        ran = random.sample(blockList, len(blockList))
        for l in ran:
            trailList.append(l)
    for n in trailList:
        print n


repTrails(5, ['right', 'left'], 6)
