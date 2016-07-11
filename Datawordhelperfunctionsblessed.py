import numpy as np
import matplotlib.pyplot as plt

class datawordblessed:


    def __init__(self,line):
            datawords=line.split()
            self.channelnr=datawords[0]
            self.TOT=datawords[4]
            self.LE=datawords[5]
            self.TE=datawords[6]


    def getChannelnr(self):
        return int(self.channelnr[-1:])
