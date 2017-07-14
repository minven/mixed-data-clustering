# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:16:46 2016

@author: Mindaugas
"""


def EquivalenceClasses(dataset,CatAtr):
    """                                                                                       
    EquivalenceClasses                                              
                                                                                  
    Parameters                                                                                
    ----------                                                                                
    data_set - pandas dataframe
    CatAtr - list of categorical attributes
                                                                                               
    Returns                                                                                   
    -------                                                                                                                                       
    """
    subsetCat = dataset[CatAtr].values.tolist()
    if type(subsetCat[0]) == int:
        unique_values = set([a for a in subsetCat])
        rez = {}    
        for unique_value in unique_values:
            indices = [i for i,value in enumerate(subsetCat) if value == unique_value]   
            rez[unique_value] = indices
        return rez
    else:
        unique_values = set([a[0] for a in subsetCat])
        rez = {}    
        for unique_value in unique_values:
            indices = [i for i,value in enumerate(subsetCat) if value[0] == unique_value]   
            rez[unique_value] = indices
        return rez
        
def CUC(data_set,clusters,CatAtr):
    """                                                                                       
    Categorical utility function for categorical data                                                  
                                                                                  
    Parameters                                                                                
    ----------                                                                                
    data_set - pandas dataframe
    clusters - dictionary keys - clusters, values - lists with data_set indexes
    CatAtr - list of categorical attributes
                                                                                               
    Returns                                                                                   
    -------                                                                                   
    Q - numerical value based on p.6 eq. 20                                                    
    """
    U = data_set.shape[0]
    Q = 0
    for attribute in CatAtr:
        IND = EquivalenceClasses(data_set,attribute)
        for key_x,ind in IND.items():
            X = len(ind)
            for key_c, value in clusters.items():
                X_Ci = sum(map(lambda x: x in value, ind))
                Ci = len(value)
                try:
                    Q += (Ci/U)*((X_Ci**2)/(Ci**2)-(X**2)/(U**2))
                except ZeroDivisionError:
                    print("CUC calculation error Ci = 0")
    return Q/len(clusters)