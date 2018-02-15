'''
Created on Feb 8, 2018

@author: fangyunzhao
'''

import numpy as np

def repetition(letters, numberBeforeSwitch, numRepetition):
    for i in range(numRepetition):
        for l in letters:
            for i in range(numberBeforeSwitch):
               print l

            
repetition(['A', 'B'], 2, 2)

repetition(['A', 'B'], 1, 1)

repetition(['A', 'B'], 2, 1)      
    

