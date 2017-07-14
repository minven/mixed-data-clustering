# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:24:25 2016

@author: Mindaugas
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

def plotClusters(data_set,clusters,clust_numb,prototypes,title,number,status):
    if status == "save":
        
        pp = PdfPages('../output/{}_{}_clusters.pdf'.format(title,number))
        plt.figure()
        plt.clf()    
        data_list = data_set.as_matrix()
        colors = iter(plt.cm.rainbow(np.linspace(0, 1, clust_numb)))
        for key,cluster in clusters.items():
            #plt.scatter()
            plt.scatter(x = data_list[cluster][:,0],y = data_list[cluster][:,1],color = next(colors))
            plt.plot(prototypes[key][0],prototypes[key][1],'sg',markersize=8)
        pp.savefig()
        pp.close()
        
    else:
        plt.figure()
        plt.clf()    
        data_list = data_set.as_matrix()
        colors = iter(plt.cm.rainbow(np.linspace(0, 1, clust_numb)))
        for key,cluster in clusters.items():
            #plt.scatter()
            plt.scatter(x = data_list[cluster][:,0],y = data_list[cluster][:,1],color = next(colors))
            plt.plot(prototypes[key][0],prototypes[key][1],'sg',markersize=8)  
        plt.show()