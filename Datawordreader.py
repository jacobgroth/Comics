
import numpy as np
import matplotlib.pyplot as plt
import glob
import fileinput
from Datawordhelperfunctions import *
from GraphClass import *

path='/Users/rgjg/Dropbox/CosmicsDataFiles/*'
files=glob.glob(path)

events = []
ievt = []

times = []
trigtimes = []


for filename in files:
    f = open(filename)
    lines = f.readlines()

    print ' ****** Der arbejdes paa filen der hedder %s *********' % filename

    #for i in xrange(10000):
    for i in xrange(len(lines)):



        if i+1 >= len(lines): break



        if ( (len(lines) - i ) % 50000 == 0 ): print "Der er %s begivenheder tilbage" % (len(lines) - i )

        dw = timehelperfunc(lines[i])

        times.append(dw.getalltimes())
        trigtimes.append(dw.getactivetrigtimes())

        if timehelperfunc(lines[i+1]).isnewevent():

            listsum = np.zeros(len(times[0]))
            trigsum = np.zeros(len(times[0]))

            for j in times:
                listsum += j

            for k in trigtimes:
                trigsum += k

            events.append( event(listsum.tolist(),trigsum.tolist()) )

            ievt = []
            times = []
            trigtimes = []


print " ---------- plotting ------------ Der er %s begivenheder der skal plottes" % len(events)

TOTgraph = plotTOTs(events)
TOTgraph.plotGraph(20,0,50)
TOTgraph.canvas.show()

#coinGraph = plotCoin(events)
#coinGraph.plotGraph(5,0,5)
#coinGraph.canvas.show()


TFGraph = plotTimeDiff(events)
TFGraph.plotGraph(50,0.0001,20)
TFGraph.canvas.show()