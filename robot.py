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
        # for each motor neuron, 
        for neuron in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuron):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuron).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuron)
                self.motors[jointName].Set_Value(self, desiredAngle)
                jointName.decode("utf-8")
    
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        
        self.stateOfLinkZero = p.getLinkState(self.robotId,0)
        
        self.positionOfLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
        
        # Write to file
        with open("fitness.txt", 'w') as file:
            file.write(str(self.xCoordinateOfLinkZero))