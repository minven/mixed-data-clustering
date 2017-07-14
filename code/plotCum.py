# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:40:58 2016

@author: Mindaugas
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
def plotCum(clusters_numb,cum_values,xlab,ylab,title):
    pp = PdfPages('../output/{}.pdf'.format(title))
    plt.figure()
    plt.clf()
    plt.plot(clusters_numb,cum_values)
    plt.xticks(clusters_numb)  
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    pp.savefig()
    pp.close()