import constants as c
import numpy

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName

        # Create sensor storage (make n = number of steps in simulation)
        self.values = numpy.zeros(c.simSteps)
        print(self.values)