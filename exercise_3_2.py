'''
Created on Feb 14, 2018

@author: fangyunzhao
'''

def repTrails(numberBlock, LeftRight, numberTask):
    for x in range(1, numberBlock + 1):
        for y in range(3):
            if y < 2:
                for l in LeftRight:
                    print (x, "Mask", l)
            else:
                for l in LeftRight:
                    print (x, "nonMask", l)


repTrails(5, ['right', 'left'], 6)