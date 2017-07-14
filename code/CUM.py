# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:19:07 2016

@author: Mindaugas
"""

import CUN
import CUC
def CUM(data_set,clusters,CatAtr,NumAtr):
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ac + Ar
    if Ar and Ac:
        return((Ar/A)*CUN.CUN(data_set,clusters,NumAtr) + 
        (Ac/A) * CUC.CUC(data_set,clusters,CatAtr))
    elif not Ar:
        return(CUC.CUC(data_set,clusters,CatAtr))
    elif not Ac:
        return(CUN.CUN(data_set,clusters,NumAtr))