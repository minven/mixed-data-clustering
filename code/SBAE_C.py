# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:05:44 2016

@author: Mindaugas
"""
import itertools
import distances as ds

def BE_C(data_set,cluster1,cluster2,clusters,CatAtr):
    '''
    Two clusters validation index for categorical attrib
    p. 5, eq. 16
    '''
    subset1 = data_set[CatAtr].values[clusters[cluster1]]
    subset2 = data_set[CatAtr].values[clusters[cluster2]]
    N1 = subset1.shape[0]
    N2 = subset2.shape[0]
    s = 0
    for i in range(N1):
        for j in range(N2):
            s += ds.hamdist(subset1[i],subset2[j])
    return s/(N1*N2)

def SBAE_C(data_set,cluster1,clusters,CatAtr):
    rez = 0 
    C_k = list(clusters.keys())
    C_k.remove(cluster1)
    permutations = list(itertools.combinations(C_k,2))  
    for permutation in permutations:
        rez += BE_C(data_set,permutation[0],permutation[1],clusters,CatAtr)
    return rez