
import numpy as np
import matplotlib.pyplot as plt
from Datawordhelperfunctions import *


filename="/Users/rgjg/Desktop/6865.2016.0411.0"

f=open(filename)
lines=f.readlines()

events = []
ievt = []

times = []

for i in xrange(1000):

    if i+1 >= len(lines): break

    dw = timehelperfunc(lines[i])

    times.append(dw.getalltimes())

    if timehelperfunc(lines[i]).isnewevent():
        print "------------- event nr %s ------------" % i

    if timehelperfunc(lines[i+1]).isnewevent():
        events.append(event(len(ievt)))

        listsum = np.zeros(len(times[0]))

        for j in times:
            listsum += j
        listsum = listsum.tolist()

        print times
        print "HEP" , listsum
        ievt = []
        times = []



#    print dw.getalltimes(), lines[i]


print len(events)
