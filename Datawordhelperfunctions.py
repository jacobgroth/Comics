import numpy as np
import matplotlib.pyplot as plt

class dataword:

    channelnames = ["LE1", "TE1", "LE2", "TE2", "LE3", "TE3", "LE4", "TE4"]

    def __init__(self,line):
            datawords=line.split()
            self.datawordsdict = {
                'evtid': 0,
                'triggerCount': datawords[0],
                self.channelnames[0]: datawords[1],
                self.channelnames[1]: datawords[2],
                self.channelnames[2]: datawords[3],
                self.channelnames[3]: datawords[4],
                self.channelnames[4]: datawords[5],
                self.channelnames[5]: datawords[6],
                self.channelnames[6]: datawords[7],
                self.channelnames[7]:datawords[8],
                'triggerCountGPS': datawords[9],
                'GPSTime': datawords[10],
                'date': datawords[11],
                'GPSOk': datawords[12],
                'NumGPSSat': datawords[13],
                'dataOk':datawords[14],
                'offset': datawords[15]
            }

    def __str__(self):
        return "dataword: %s" % self.datawords


class timehelperfunc(dataword):


    def __init__(self,line):
        dataword.__init__(self,line)

    def returntimeresolution(self):
        return 1.25

    def hextobin(self,value):
        return bin(int(value, 16))[2:]

    def hextodec(self,value):
        return int(value, 16)

    def gettimeinns(self,value):
        return int(self.hextobin(value)[-5:],2)*self.returntimeresolution()

    def isnewevent(self):
        return len(self.hextobin(self.datawordsdict["LE1"]))==8

    def isvalidedge(self,ch):
        return self.hextobin(self.datawordsdict[ch])[-6:-5]

    def getalledges(self):
        return [self.isvalidedge(x) for x in self.channelnames]

    def gettime(self,ch):
        return self.gettimeinns(self.datawordsdict[ch])

    def getalltimes(self):
        return [self.gettime(x) for x in self.channelnames]


class event:

    def __init__(self,size):
        self.size = size






