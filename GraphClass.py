import numpy as np
import matplotlib.pyplot as plt


class graphbaseclass:

    def __init__(self):
        return trut

class plotTOTs(graphbaseclass):


    def __init__(self,events):

        self.TOT1 = []
        self.TOT2 = []
        self.TOT3 = []
        self.TOT4 = []

        for evt in events:
            if evt.getTOTs()[0] != 0: self.TOT1.append(float(evt.getTOTs()[0]))
            if evt.getTOTs()[1] != 0: self.TOT2.append(float(evt.getTOTs()[1]))
            if evt.getTOTs()[2] != 0: self.TOT3.append(float(evt.getTOTs()[2]))
            if evt.getTOTs()[3] != 0: self.TOT4.append(float(evt.getTOTs()[3]))

        self.TOT1 = np.array(self.TOT1)
        self.TOT2 = np.array(self.TOT2)
        self.TOT3 = np.array(self.TOT3)
        self.TOT4 = np.array(self.TOT4)

        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax0, ax1, ax2, ax3 = axes.flat

        num_bins = 20
        ax0.hist(self.TOT1, num_bins, (0, 50), normed=1, facecolor='blue', alpha=0.5)
        ax1.hist(self.TOT2, num_bins, (0, 50), normed=1, facecolor='green', alpha=0.5)
        ax2.hist(self.TOT3, num_bins, (0, 50), normed=1, facecolor='red', alpha=0.5)
        ax3.hist(self.TOT4, num_bins, (0, 50), normed=1, facecolor='yellow', alpha=0.5)

        ax0.set_title('TOT of ch1')
        ax0.set_xlabel('ns')
        ax1.set_title('TOT of ch2')
        ax2.set_title('TOT of ch3')
        ax3.set_title('TOT of ch4')

        plt.tight_layout()
        plt.show()
