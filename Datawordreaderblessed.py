
import numpy as np
import matplotlib.pyplot as plt
from Datawordhelperfunctions import *

filename="/Users/rgjg/Desktop/6865.2016.0411.0"

with open(filename) as f:

    for line in f:

    TOT1=[]
    TOT2=[]
    TOT3=[]
    TOT4=[]

    for line in f:

        dw=datawordblessed(line)

        if (dw.getChannelnr()==1):  TOT1.append(float(dw.TOT))
        if (dw.getChannelnr()==2):  TOT2.append(float(dw.TOT))
        if (dw.getChannelnr()==3):  TOT3.append(float(dw.TOT))
        if (dw.getChannelnr()==4):  TOT4.append(float(dw.TOT))


        TOT1 = np.array(TOT1)
        TOT2 = np.array(TOT2)
        TOT3 = np.array(TOT3)
        TOT4 = np.array(TOT4)

        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax0, ax1, ax2, ax3 = axes.flat

        num_bins = 20
        ax0.hist(TOT1, num_bins,(0, 50), normed=1, facecolor='blue', alpha=0.5)
        ax1.hist(TOT2, num_bins,(0, 50), normed=1, facecolor='green', alpha=0.5)
        ax2.hist(TOT3, num_bins,(0, 50), normed=1, facecolor='red', alpha=0.5)
        ax3.hist(TOT4, num_bins,(0, 50), normed=1, facecolor='yellow', alpha=0.5)


        ax0.set_title('TOT of ch1')
        ax0.set_xlabel('ns')
        ax1.set_title('TOT of ch2')
        ax2.set_title('TOT of ch3')
        ax3.set_title('TOT of ch4')

        plt.tight_layout()
        plt.show()

