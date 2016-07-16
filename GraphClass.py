import numpy as np
import matplotlib.pyplot as plt


class graphbaseclass:

    def __init__(self):
        return True

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

    def plotGraph(self,num_bins,xbinlow,xbinhigh):

        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax0, ax1, ax2, ax3 = axes.flat

        ax0.hist(self.TOT1, num_bins, (xbinlow, xbinhigh), facecolor='blue', alpha=0.5)
        ax1.hist(self.TOT2, num_bins, (xbinlow, xbinhigh), facecolor='green', alpha=0.5)
        ax2.hist(self.TOT3, num_bins, (xbinlow, xbinhigh), facecolor='red', alpha=0.5)
        ax3.hist(self.TOT4, num_bins, (xbinlow, xbinhigh), facecolor='yellow', alpha=0.5)

        ax0.set_title('TOT of ch1')
        ax0.set_xlabel('ns')
        ax1.set_title('TOT of ch2')
        ax2.set_title('TOT of ch3')
        ax3.set_title('TOT of ch4')

        plt.tight_layout()

        self.canvas = plt


class plotCoin(graphbaseclass):


    def __init__(self,events):

        for evt in events:
            nrcoin = 0
            for ich in evt.getTOTs():
                if ich:  nrcoin += 1
            self.coin.append(nrcoin)

        self.coin = np.array(self.coin)

    def plotGraph(self,num_bins,xbinlow,xbinhigh):

        n, bins, patches = plt.hist(self.coin, num_bins, (xbinlow, xbinhigh), facecolor='green', alpha=0.5)
        # add a 'best fit' line

        plt.xlabel('Antal')
        plt.title(r'Histogram af coincidences')

        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)

        self.canvas = plt


class plotTimeDiff(graphbaseclass):


    def __init__(self,events):

        self.timeDiff = []

        for i in xrange(len(events)):
            if i + 1 >= len(events): break
            self.timeDiff.append( (events[i+1].gettrigtimes()[0] - events[i].gettrigtimes()[0])/1e9 )

        self.timeDiff = np.array(self.timeDiff)

    def plotGraph(self,num_bins,xbinlow,xbinhigh):

        n, bins, patches = plt.hist(self.timeDiff, num_bins, (xbinlow, np.amax(self.timeDiff)/200), facecolor='green', alpha=0.5)

        plt.xlabel('Tid/sek')
        plt.title(r'Histogram af tids difference')
        plt.subplots_adjust(left=0.15)

        self.canvas = plt
