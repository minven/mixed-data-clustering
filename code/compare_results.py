# -*- coding: utf-8 -*-
"""
Created on Sun May  8 15:15:54 2016

@author: Mindaugas
"""
import pandas as pd
def compare_results():
    labels = pd.read_csv("../output/contraceptive/labels.csv",header = None)
    results = pd.read_csv("../output/contraceptive/result.csv",header = None).transpose()
    labels[0][labels[0] == 1] = 'a'
    labels[0][labels[0] == 2] = 'b'
    labels[0][labels[0] == 3] = 'c'
    a11 = sum(labels[0] == results[0])
    disagree = sum(labels[0] != results[0])
    z = 0
    for i in range(len(labels)):
        if (labels[0][i] == results[0][i]) and (labels[0][i] == "a") and (results[0][i] == "a"):
            z += 1
    print(z)
    z = 0
    for i in range(len(labels)):
        if (labels[0][i] == results[0][i]) and (labels[0][i] == "b") and (results[0][i] == "b"):
            z += 1
    print(z)
    z = 0
    for i in range(len(labels)):
        if (labels[0][i] == "a") and (results[0][i] == "b"):
            z += 1
    print(z)
    z = 0
    for i in range(len(labels)):
        if (labels[0][i] == "b") and (results[0][i] == "a"):
            z += 1
    print(z)

    #a11 = sum(labels[0] == results[0])
    #disagree = sum(labels[0] != results[0])
    
    #print(disagree)    

compare_results()