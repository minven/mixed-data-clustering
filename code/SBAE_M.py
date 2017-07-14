# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:14:21 2016

@author: Mindaugas
"""
import SBAE_N
import SBAE_C
def SBAE_M(data_set,cluster,clusters,CatAtr,NumAtr,sigma):
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ac + Ar
    C_k = list(clusters.keys())
    SUM_SBAE_N = 0
    SUM_SBAE_C = 0
    
    if Ar and Ac:
        KTH_SBAE_N = SBAE_N.SBAE_N(data_set,cluster,clusters,NumAtr,sigma)
        
        KTH_SBAE_C = SBAE_C.SBAE_C(data_set,cluster,clusters,CatAtr)
        
        for k in C_k:
            SUM_SBAE_N += SBAE_N.SBAE_N(data_set,k,clusters,NumAtr,sigma)
            SUM_SBAE_C += SBAE_C.SBAE_C(data_set,k,clusters,CatAtr)
        return (Ar/A) * (KTH_SBAE_N/SUM_SBAE_N) + (Ar/A) * (KTH_SBAE_C/SUM_SBAE_C)  
    elif not Ar:
        KTH_SBAE_C = SBAE_C.SBAE_C(data_set,cluster,clusters,CatAtr)
        for k in C_k:
            SUM_SBAE_C += SBAE_C.SBAE_C(data_set,k,clusters,CatAtr)
        return (Ac/A) * (KTH_SBAE_C/SUM_SBAE_C)  
    elif not Ac:
        KTH_SBAE_N = SBAE_N.SBAE_N(data_set,cluster,clusters,NumAtr,sigma)
        for k in C_k:
            
            SUM_SBAE_N += SBAE_N.SBAE_N(data_set,k,clusters,NumAtr,sigma)
        return (Ar/A) * (KTH_SBAE_N/SUM_SBAE_N)