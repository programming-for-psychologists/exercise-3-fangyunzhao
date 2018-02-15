'''
Created on Feb 14, 2018

@author: fangyunzhao
'''

import random

def repTrails(numberBlock, LeftRight, numberTask):
    trailList = []
    for x in range(1, numberBlock + 1):
        for y in range(3):
            if y < 2:
                for l in LeftRight:
                    a = ''.join([str(x), ',','Mask',',',l])
                    trailList.append(a)
                    #print a
            else:
                for l in LeftRight:
                    a = ''.join([str(x), ',','NonMask',',',l])
                    trailList.append(a)
                    #print a
    ran = random.sample(trailList, len(trailList))

    for l in ran:
        print l

repTrails(5, ['right', 'left'], 6)


