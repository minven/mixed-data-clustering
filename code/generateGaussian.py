# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:44:18 2016

@author: Mindaugas
"""
import matplotlib.pyplot as plt
import numpy as np
def generateGaussian():
    means = [[0, 0],[5,4.5],[5,-2],[-2,-5],[1,-4],[-5.5,-1.5],[-5,2],[-2,4.5],[2,-3.5],[7,-3.5]]
    covs = [[[0.1, 0], [0, 0.1]],[[0.2, 0], [0, 0.2]],[[0.1, 0], [0, 0.1]],[[0.1, 0], [0, 0.1]],[[0.2, 0], [0, 0.1]],[[1, 0], [0, 0.5]],[[0.5, 0], [0, 1]],[[0.5, 0], [0, 1]],[[0.5, 0], [0, 1]],[[1, 0], [0, 0.5]]]  # diagonal covariance    
    xx = []
    yy = []
    for i in range(5):
        x, y = np.random.multivariate_normal(means[i], covs[i], 20).T
        xx.append(list(x))
        yy.append(list(y))
  
    plt.plot(xx, yy, '.')
    plt.axis('equal')
    plt.show()
    outfile1 = open('../datasets/gaussian_example.csv', 'w')
    outfile1.write("a1,a2\n")
    for i in range(5):
        for j in range(20):
            outfile1.write(str(xx[i][j]))
            outfile1.write(",")
            outfile1.write(str(yy[i][j]))
            outfile1.write("\n")
    outfile1.close()