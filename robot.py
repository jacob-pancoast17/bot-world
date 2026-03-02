import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        # Create robot
        self.robotId = p.loadURDF("body.urdf")

        # Create brain
        self.nn = NEURAL_NETWORK("brain.nndf")

        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, stepNum):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(stepNum)
    
    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, stepNum):
        for motor in self.motors:
            self.motors[motor].Set_Value(self, stepNum)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()