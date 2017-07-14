# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:23:47 2016

@author: Mindaugas
"""

import numpy as np
from scipy.stats import mode

def newCenters(dataset,CatAtr,NumAtr,cluster_indices,clust_numb):
    clusters = {j: [] for j in range(clust_numb)}
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    for i,clust_ind in enumerate(cluster_indices):
        clusters[clust_ind].append(i)
    new_centroid = {i: [] for i in range(len(clusters))}
    subsetCat = dataset[CatAtr].values
    subsetNum = dataset[NumAtr].values
    
    if Ar and Ac:
        for key,cluster in clusters.items():
            new_centroid[key] = list(np.concatenate((mode(subsetCat[cluster],axis = 0)[0][0],subsetNum[cluster].mean(axis = 0))))
        return [new_centroid,clusters]
    elif not Ar:
        for key,cluster in clusters.items():
            if cluster:
                new_centroid[key] = list(mode(subsetCat[cluster],axis = 0)[0][0])
            else:
                print("cluster {} is empty" . format(key))
        return [new_centroid,clusters]
    elif not Ac:
        for key,cluster in clusters.items():
            new_centroid[key] = list(subsetNum[cluster].mean(axis = 0))
        return [new_centroid,clusters]  