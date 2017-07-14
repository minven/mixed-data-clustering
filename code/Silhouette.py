# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:07:00 2016

@author: Mindaugas
"""
from sklearn import metrics
import numpy as np

def calculateSilhouetteNum(data_set,clusters,NumAtr):
    d = data_set[NumAtr]
    a = [0]*data_set.shape[0]
    for key,clusters in clusters.items():
        for c in clusters:
            a[c] = key
    return(metrics.silhouette_score(d.as_matrix(), np.array(a), metric='euclidean'))
    
    
def calculateSilhouetteCat(data_set,clusters,CatAtr):
    d = data_set[CatAtr]
    a = [0]*data_set.shape[0]
    for key,clusters in clusters.items():
        for c in clusters:
            a[c] = key
    return(metrics.silhouette_score(d.as_matrix(), np.array(a), metric='hamming'))
    
    
def calculateSilhouetteMix(data_set,clusters,NumAtr,CatAtr):
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ac + Ar
    if Ar and Ac:
        return((Ar/A)*calculateSilhouetteNum(data_set,clusters,NumAtr) + (Ac/A) *calculateSilhouetteCat(data_set,clusters,CatAtr))
    elif not Ar:
        return(calculateSilhouetteCat(data_set,clusters,CatAtr))
    elif not Ac:
        return(calculateSilhouetteNum(data_set,clusters,NumAtr))