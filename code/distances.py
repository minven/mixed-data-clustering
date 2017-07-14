# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:06:47 2016

@author: Mindaugas
"""
import numpy as np
from math import sqrt

def hamdist(str1, str2):
    '''
    Hammington distance
    '''
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                    diffs += 1
    return diffs

def Eucdist(X2,X1):
    '''
    Euclidean distance
    '''
    return sqrt(sum(np.subtract(X1,X2)**2))