# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:33:11 2016

@author: Mindaugas
"""
import numpy as np
import distances as ds

def dunnIndex(data_set,CatAtr,NumAtr,clusters):
    clusters_numb = len(clusters)
    subsetCat = data_set[CatAtr].as_matrix()
    subsetNum = data_set[NumAtr].as_matrix()
    U = data_set.shape[0]
    D = np.zeros(shape = (U,U))
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ar+Ac
        
    if Ar and Ac:
        for i in range(U):
            for j in range(U):
                D[i][j] =  (Ar/A)*ds.Eucdist(subsetNum[i],subsetNum[j]) + (Ac/A)*ds.hamdist(subsetCat[i],subsetCat[j])
    elif not Ar:
        for i in range(U):
            for j in range(U):
                D[i][j] = ds.hamdist(subsetCat[i],subsetCat[j])
    elif not Ac:
        for i in range(U):
            for j in range(U):
                D[i][j] =  ds.Eucdist(subsetNum[i],subsetNum[j])
    
  
    
    nc = len(clusters)
    interClust = np.zeros(shape = (nc,nc))
    intraClust = np.zeros(shape = (1,nc))
    
    interClust = np.empty((nc,nc,))
    interClust[:] = np.NAN   
    
    for i in range(nc):
        c1 = clusters[i]
        for j in range(nc):
            if j == i:
                D_sub = D[c1,:]
                D_sub = D_sub[:,c1]
                intraClust[0][i] = np.max(np.max(D_sub,axis = 0))
            if j > i:
                c2 = clusters[j]
                D_sub_j = D[c1,:]
                D_sub_j = D_sub_j[:,c2]
                interClust[i][j] = np.min(np.min(D_sub_j,axis = 0))
    return np.nanmin(interClust)/np.max(intraClust)