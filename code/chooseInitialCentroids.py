# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:11:15 2016

@author: Mindaugas
"""
import numpy as np
import distances as ds

def chooseInitialCentroids(data_set,CatAtr,NumAtr,clust_numb):
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
    
    
    centers = []
    remembered_indexes = [i for i in range(U)]
    step = int(U/clust_numb)
    for i in range(clust_numb):
        sums_axis = []
        sums_axis = list(np.sum(D,axis = 0))        
        max_ind =  sums_axis.index(max(sums_axis))
        max_ind_real = remembered_indexes[max_ind] 
        centers.append(max_ind_real)

        
        
        max_ind_row = list(D[max_ind,:])
        
        
        for j in range(step):
           
            min_ind_inner =  max_ind_row.index(min(max_ind_row))
            D = np.delete(D, (min_ind_inner), axis=0)
            D = np.delete(D, (min_ind_inner), axis=1)
            remembered_indexes.pop(min_ind_inner)
            max_ind_row.pop(min_ind_inner)       
            
  
    return centers
    