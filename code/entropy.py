# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:01:32 2016

@author: Mindaugas
"""
from itertools import groupby

iterable = [1,2,33,1,1,12]
print([list(g) for k, g in groupby(iterable)])



def TotalEntropy(data_set):
    '''
    Total Entropy from:
    A Framework for Clustering Mixed Attribute Type Datasets p.5
    '''
    
    cat_subset  = data_set[['cat1','cat2']]
    for col in cat_subset:
        print(list(cat_subset[col]))
        print(ShannonEntropy(list(cat_subset[col])))
        
        
def ShannonEntropy(labels):
    n_labels = len(labels)
    if n_labels <= 1:
        return 0
    probs = [labels.count(x)/n_labels for x in set(labels)]
    return entropy(probs,base = 2)        