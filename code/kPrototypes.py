# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:20:40 2016

@author: Mindaugas
"""
import distances as ds

def Kprototypes(dataset,CatAtr,NumAtr,Z,z,x):
    subsetCat = dataset[CatAtr].as_matrix()
    subsetNum = dataset[NumAtr].as_matrix()
    
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ar+Ac
    SN = 0
    SD = 0
    if Ar and Ac:
        for key,prototype in Z.items():
            SN += ds.Eucdist(subsetNum[x],prototype[Ac:A])
            SD += ds.hamdist(subsetCat[x],prototype[0:Ac])
        return((Ar/(A*SN))*ds.Eucdist(subsetNum[x],z[Ac:A])+(Ac/(A*SD))*ds.hamdist(subsetCat[x],z[0:Ac]))
    elif not Ar:
        for key,prototype in Z.items():
            SD += ds.hamdist(subsetCat[x],prototype[0:Ac])
        return((Ac/(A*SD))*ds.hamdist(subsetCat[x],z[0:Ac]))
    elif not Ac:
        for key,prototype in Z.items():
            SN += ds.Eucdist(subsetNum[x],prototype[0:Ar])
        return((Ar/(A*SN))*ds.Eucdist(subsetNum[x],z[0:Ar])) 