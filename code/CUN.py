# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:18:02 2016

@author: Mindaugas
"""
import numpy as np
from math import sqrt
def CUN(data_set,clusters,NumAtr):
    """                                                                                       
    Categorical utility function for numerical dataset                                           
                                                                                  
    Parameters                                                                                
    ----------                                                                                
    data_set - pandas dataframe
    clusters - dictionary keys - clusters, values - lists with data_set indexes
    CatAtr - list of categorical attributes
                                                                                               
    Returns                                                                                   
    -------                                                                                   
    rez - numerical value based on p.6 eq. 21                                                    
    """
    U = data_set.shape[0]
    rez = 0
    for attribute in NumAtr:
        subsetNum = data_set[attribute].values.tolist()
        m_l = np.mean(subsetNum)
        #s_l = np.std(subsetNum)

        delta_l = sum(map(lambda x: ((x - m_l)**2), subsetNum))/U
      
        delta_jl_sum = 0        
        for key,cluster in clusters.items():
            m_jl = np.mean([subsetNum[x] for x in cluster])
            s_l = np.std([subsetNum[x] for x in cluster])
            C_j = len(cluster)
            delta_jl = sum(map(lambda x: ((subsetNum[x] - m_jl)**2), cluster))/C_j
            delta_jl_sum += ((C_j/U) * delta_jl)
            #delta_jl_sum += (C_j/U) * delta_jl
        rez += (delta_l - delta_jl_sum)
    return  rez