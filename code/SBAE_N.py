# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:02:23 2016

@author: Mindaugas
"""
import math
import itertools
import numpy as np

def gauss_kernel(sigma,d,x,y):
    return (1/(((2*math.pi)**(d/2))*(sigma**d)))*math.exp(-np.dot((x-y),(x-y))/(2*sigma**2))
    
def BE_N(data_set,cluster1,cluster2,clusters,NumAtr,sigma):
    '''
    Two clusters validation index for numerical attrib
    p. 4, eq. 9
    '''
    subset1 = data_set[NumAtr].values[clusters[cluster1]]
    subset2 = data_set[NumAtr].values[clusters[cluster2]]
    N1 = subset1.shape[0]
    N2 = subset2.shape[0]
    s = 0
    for i in range(N1):
        for j in range(N2):
            s += gauss_kernel(sigma,2,subset1[i],subset2[j])
    return -math.log(s/(N1*N2))

def SBAE_N(data_set,cluster1,clusters,NumAtr,sigma):
    rez = 0 
    C_k = list(clusters.keys())
    C_k.remove(cluster1)
    permutations = list(itertools.combinations(C_k,2))
    for permutation in permutations:
        rez += BE_N(data_set,permutation[0],permutation[1],clusters,NumAtr,sigma)
    return rez