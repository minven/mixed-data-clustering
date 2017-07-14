# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:51:33 2016

@author: Mindaugas
"""
import numpy as np
import distances as ds



def diameter(subsetNum,subsetCat,cluster_indexes,CatAtr,NumAtr,prototype,clust_numb):
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ar + Ac
    ss = 0
    if Ar and Ac:
        for x in cluster_indexes:
            ss += (Ar/A)*ds.Eucdist(subsetNum[x],prototype[Ac:A]) + (Ac/A)*ds.hamdist(subsetCat[x],prototype[0:Ac])
        return ss/len(cluster_indexes)
            
    elif not Ar:
        for x in cluster_indexes:
            ss += ds.hamdist(subsetCat[x],prototype[0:Ac])
        return ss/len(cluster_indexes)        
    elif not Ac:
        for x in cluster_indexes:
            ss += ds.Eucdist(subsetNum[x],prototype[Ac:A])
        return ss/len(cluster_indexes)        



def DaviesBouldin(data_set,CatAtr,NumAtr,clusters,prototypes):
    clusters_numb = len(clusters)
    subsetCat = data_set[CatAtr].as_matrix()
    subsetNum = data_set[NumAtr].as_matrix()
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ar+Ac
        
    if Ar and Ac:
        s = []
        for i,cluster_i in enumerate(clusters.values()):
            prototype_i = prototypes[i]
            d_i = diameter(subsetNum,subsetCat,cluster_i,CatAtr,NumAtr,prototype_i,clusters_numb)
            t = 0
            for j,cluster_j in enumerate(clusters.values()):
                if i != j:
                    prototype_j = prototypes[j]  
                    d_i = diameter(subsetNum,subsetCat,cluster_i,CatAtr,NumAtr,prototype_i,clusters_numb)
                    d_j = diameter(subsetNum,subsetCat,cluster_j,CatAtr,NumAtr,prototype_j,clusters_numb)
                    d_ij = (Ar/A)*ds.Eucdist(prototype_i[Ac:A],prototype_j[Ac:A]) + (Ac/A)*ds.hamdist(prototype_i[0:Ac],prototype_j[0:Ac])
                    t += (d_i+d_j)/d_ij
            s.append(t/len(clusters))
        return max(s)
        
    elif not Ar:
        s = []
        for i,cluster_i in enumerate(clusters.values()):
            prototype_i = prototypes[i]
            d_i = diameter(subsetNum,subsetCat,cluster_i,CatAtr,NumAtr,prototype_i,clusters_numb)
            t = 0
            for j,cluster_j in enumerate(clusters.values()):
                if i != j:
                    prototype_j = prototypes[j]   
                    d_j = diameter(subsetNum,subsetCat,cluster_j,CatAtr,NumAtr,prototype_j,clusters_numb)
                    d_ij = ds.hamdist(prototype_i[0:Ac],prototype_j[0:Ac])
                    t += (d_i+d_j)/d_ij
            s.append(t/len(clusters))
        return max(s)
    elif not Ac:
        s = []
        for i,cluster_i in enumerate(clusters.values()):
            prototype_i = prototypes[i]
            d_i = diameter(subsetNum,subsetCat,cluster_i,CatAtr,NumAtr,prototype_i,clusters_numb)
            t = 0
            for j,cluster_j in enumerate(clusters.values()):
                if i != j:
                    prototype_j = prototypes[j]  
                    d_j = diameter(subsetNum,subsetCat,cluster_j,CatAtr,NumAtr,prototype_j,clusters_numb)
                    d_ij = (ds.Eucdist(prototype_i[Ac:A],prototype_j[Ac:A]))
                    t += (d_i+d_j)/d_ij
            s.append(t/len(clusters))
        return max(s)
                
   