# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:48:46 2016

@author: Mindaugas
"""
import distances as ds
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
def cmdscale(data_set,CatAtr,NumAtr,clusters,title,number,status):
    # http://www.nervouscomputer.com/hfs/cmdscale-in-python/
    """                                                                                       
    Classical multidimensional scaling (MDS)                                                  
                                                                                               
    Parameters                                                                                
    ----------                                                                                
    D : (n, n) array                                                                          
        Symmetric distance matrix.                                                            
                                                                                               
    Returns                                                                                   
    -------                                                                                   
    Y : (n, p) array                                                                          
        Configuration matrix. Each column represents a dimension. Only the                    
        p dimensions corresponding to positive eigenvalues of B are returned.                 
        Note that each dimension is only determined up to an overall sign,                    
        corresponding to a reflection.                                                        
                                                                                               
    e : (n,) array                                                                            
        Eigenvalues of B.                                                                     
                                                                                               
    """
    subsetCat = data_set[CatAtr].as_matrix()
    subsetNum = data_set[NumAtr].as_matrix()
    U = data_set.shape[0]
    D = np.zeros(shape = (U,U))

    clust_numb = len(clusters)
    colors = iter(plt.cm.rainbow(np.linspace(0, 1, clust_numb)))
    Ar = len(NumAtr)
    Ac = len(CatAtr)
    A = Ar+Ac
    
    
    if Ar and Ac:
        for i in range(U):
            for j in range(U):
                D[i][j] =  (Ar/A)*ds.Eucdist(subsetNum[i],subsetNum[j]) + (Ac/A)*ds.hamdist(subsetCat[i],subsetCat[j])
    elif not Ar:
        for i in range(U):
            for j in range(U):
                D[i][j] = ds.hamdist(subsetCat[i],subsetCat[j])
    elif not Ac:
        for i in range(U):
            for j in range(U):
                D[i][j] =  ds.Eucdist(subsetNum[i],subsetNum[j])
    


    # Number of points                                                                        
    n = len(D)
    # Centering matrix                                                                        
    H = np.eye(n) - np.ones((n, n))/n
    # YY^T                                                                                    
    B = -H.dot(D**2).dot(H)/2
    # Diagonalize                                                                             
    evals, evecs = np.linalg.eigh(B)
    # Sort by eigenvalue in descending order                                                  
    idx   = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:,idx]
    # Compute the coordinates using positive-eigenvalued components only                      
    w, = np.where(evals > 0)
    L  = np.diag(np.sqrt(evals[w]))
    V  = evecs[:,w]
    Y  = V.dot(L)
    
      
    if status == "save":
        pp = PdfPages('../output/{}_{}_multidimensional_scaling.pdf'.format(title,number))  
        for key,cluster in clusters.items():
            plt.scatter(x = Y[cluster][:,0],y = Y[cluster][:,1],color = next(colors))
            plt.xlabel("x1")
            plt.ylabel("x2")
        pp.savefig()
        pp.close()
    else:
        for key,cluster in clusters.items():
            plt.scatter(x = Y[cluster][:,0],y = Y[cluster][:,1],color = next(colors))
            plt.xlabel("x1")
            plt.ylabel("x2")
        plt.show()
    return Y
        
    
    