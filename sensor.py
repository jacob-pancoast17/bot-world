import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName

        # Create sensor storage (make n = number of steps in simulation)
        self.values = numpy.zeros(c.simSteps)
    
    def Get_Value(self, stepNum):
        self.values[stepNum] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        path = './data/' + self.linkName + '_sensor_data'
        numpy.save(path, self.values)