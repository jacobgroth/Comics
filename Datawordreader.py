
import numpy as np
import matplotlib.pyplot as plt
from Datawordhelperfunctions import *

filename="/Users/rgjg/Desktop/6865.2016.0411.0"

f=open(filename)
lines=f.readlines()

events = []
ievt = []

for i in xrange(1000):

    if i+1 >= len(lines): break

    dw = timehelperfunc(lines[i])

    ievt.append(i)

    if timehelperfunc(lines[i]).isnewevent():
        print "------------- event nr %s ------------" % i

    if timehelperfunc(lines[i+1]).isnewevent():
        events.append(event(len(ievt)))
        ievt = []


    print dw.getalltimes()


print len(events)
