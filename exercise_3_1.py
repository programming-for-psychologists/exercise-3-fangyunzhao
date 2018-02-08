'''
Created on Feb 8, 2018

@author: fangyunzhao
'''

import numpy as np

def repetition(letters, numberBeforeSwitch, numRepetition):
    for i in range(numRepetition):
        for l in letters:
            list = np.repeat(l, numberBeforeSwitch)
            print np.repeat(l, numberBeforeSwitch)
            for i in range(len(list)):
               print list[i]

repetition(['A', 'B'], 2, 2)
    

