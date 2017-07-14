'''
-need to have numerical attribute names NumAtr, and categorical CatAtr
-need to have first columns categorical and others numerical due to  
 Kprototypes function SN,SD calculation
'''
import pandas as pd
import numpy as np
import random
import csv
import math
import kPrototypes as kp
import SBAE_C
import SBAE_N
import CUM
import SBAE_M
import generateGaussian
import plotClusters
import plotCum
import multidimensionalScaling
import Silhouette
import dunnIndex
import chooseInitialCentroids
import DaviesBouldin
import matplotlib.pyplot as plt
from scipy.stats import mode


def Step2(distance_matrix):
    ShortestDistances = np.argmin(distance_matrix,axis = 0)
    return(ShortestDistances.tolist())
    


def newCenters(dataset,CatAtr,NumAtr,cluster_indices,clust_numb):
    clusters = {j: [] for j in range(clust_numb)}
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    for i,clust_ind in enumerate(cluster_indices):
        clusters[clust_ind].append(i)
    new_centroid = {i: [] for i in range(len(clusters))}
    subsetCat = dataset[CatAtr].values
    subsetNum = dataset[NumAtr].values
    
    if Ar and Ac:
        for key,cluster in clusters.items():
            new_centroid[key] = list(np.concatenate((mode(subsetCat[cluster]\
            ,axis = 0)[0][0],subsetNum[cluster].mean(axis = 0))))
        return [new_centroid,clusters]
    elif not Ar:
        for key,cluster in clusters.items():
            if cluster:
                new_centroid[key] = list(mode(subsetCat[cluster],axis = 0)[0][0])
            else:
                print("cluster {} is empty" . format(key))
        return [new_centroid,clusters]
    elif not Ac:
        for key,cluster in clusters.items():
            new_centroid[key] = list(subsetNum[cluster].mean(axis = 0))
        return [new_centroid,clusters]      

directory = "../datasets/australian_credit_approval_without_label_orig.csv"
data_set = pd.read_csv(directory)
k_min = 1
k_max = 5
sigma = 2.5



def main(data_set,k_min,k_max,sigma):
    NumAtr = ['a9','a10','a11','a12','a13','a14']
    CatAtr = ['a1','a2','a3','a4','a5','a6','a7','a8']
    #normalization
    data_set[NumAtr] = (data_set[NumAtr] - data_set[NumAtr].mean())\
    /(data_set[NumAtr].std())

    dunn_index = []
    davies = []
    U = data_set.shape[0]
    #Z = random.sample(range(0,U),k_max)
    Z = chooseInitialCentroids.chooseInitialCentroids(data_set,CatAtr,NumAtr,k_max)
   
    prototypes = {i: data_set[j:j+1].values.tolist()[0] for i,j in enumerate(Z)}
    #prototypes = {0: ['a', 'b'], 1: ['t', 'o'], 2: ['y', 'i'], 3: ['b', 'a']}
    outfile = open('../output/output.csv', 'w')
    writer = csv.writer(outfile, delimiter=',', quotechar='"')
    outfile.write("Clustering started \n")
    outfile.write("Initial centers: \n")
    writer.writerows([prototypes.values()])
    clusters_numb = list(range(k_max,k_min,-1))
    
    for clust_numb in clusters_numb:
        print("{} clusters".format(clust_numb))
        outfile.write("{} clusters \n" . format(clust_numb))
        # Generate random initial prototopes
        distance_matrix = np.zeros(shape = (clust_numb,U))
        cluster_indices = [0] * U
        clusters_different = True
        while clusters_different:
            for i in range(clust_numb):
                for u in range(U):
                    distance_matrix[i][u] = kp.Kprototypes(data_set,CatAtr,\
                    NumAtr,prototypes,prototypes[i],u)
            new_indices = Step2(distance_matrix)     
            if cluster_indices == new_indices:
                outfile.write("clustering stopped \n")           
                clusters_different = False
            else:
                outfile.write("indices \n")
                writer.writerows([new_indices])
                cluster_indices = list(new_indices)
                [prototypes,clusters] = newCenters(data_set,CatAtr,NumAtr,\
                cluster_indices,clust_numb)
                if [] in clusters.values():
                    print('Empty cluster')
                outfile.write("prototypes \n")
                writer.writerows([prototypes.values()])
                
        multidimensionalScaling.cmdscale(data_set,CatAtr,NumAtr,clusters,\
        'categorical',clust_numb,"save")
        
        dunn_index.append(dunnIndex.dunnIndex(data_set,CatAtr,NumAtr,clusters))
        davies.append(DaviesBouldin.DaviesBouldin(data_set,CatAtr,NumAtr,\
        clusters,prototypes))
        # identify worst cluster
        if clust_numb > 2:
            SBAE_M_values = []
            for cluster_k in clusters.keys():
                SBAE_M_values.append(SBAE_M.SBAE_M(data_set,cluster_k,clusters,\
                CatAtr,NumAtr,sigma))
           
            outfile.write("SBAE_M values \n")
            writer.writerows([SBAE_M_values])
            worst_clust_numbb = np.argmax(SBAE_M_values)  
            mod_distance_matrix = np.delete(distance_matrix,worst_clust_numbb,\
            axis = 0)
            mod_indices = Step2(mod_distance_matrix)
            [prototypes,clusters] = newCenters(data_set,CatAtr,NumAtr,\
            mod_indices,clust_numb-1)
        else:
            continue


    outfile.close()
    plotCum.plotCum(clusters_numb,dunn_index,"Klasteriu skaičius",\
    "Duno indeksas",'dunn_plot')
    plotCum.plotCum(clusters_numb,davies,"Klasteriu skaičius",\
    "Davies bouldin indeksas",'davies_plot')
    

a = main(data_set,k_min,k_max,sigma)



