import constants as c
import numpy
import os
from pyrosim import pyrosim
import time

class SOLUTION:

    def __init__(self, ID):

        self.myID = ID

        # Create a 3x2 matrix of random weights scaled 
        # to be over the range [-1, 1]
        self.weights = 2 * numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) - 1

        # Create a 1x4 matrix of random leg lengths 0.5-1.5
        self.upper_leg_lengths = numpy.random.rand(1, c.numLegs) + 0.5

        # Create a 1x4 matrix of random leg lengths 0.5-1.5
        self.lower_leg_lengths = numpy.random.rand(1, c.numLegs) + 0.5

    def Create_World(self):

        # Tell pyrosim the name of the file info about the world is stored in
        pyrosim.Start_SDF(f"world{self.myID}.sdf")

        # Wait for the file to be created
        while not os.path.exists(f"world{self.myID}.sdf"):
            time.sleep(.01)

        # Stores a box with these specifications to . format    
        pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[1, 1, 1])

        pyrosim.End()

    def Generate_Body(self):
        # File to store desc of robot's body
        pyrosim.Start_URDF(f"body{self.myID}.urdf")

        # Wait for the file to be created
        while not os.path.exists(f"body{self.myID}.urdf"):
            time.sleep(.01)

        # Take measurements
        BackLeg_Length = self.upper_leg_lengths[0][0]
        FrontLeg_Length = self.upper_leg_lengths[0][1]
        LeftLeg_Length = self.upper_leg_lengths[0][2]
        RightLeg_Length = self.upper_leg_lengths[0][3]

        # Stores a box with these specifications to . format
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -(BackLeg_Length / 2), 0], size=[0.2, BackLeg_Length, 0.2])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, (FrontLeg_Length / 2), 0], size=[0.2, FrontLeg_Length, 0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-(LeftLeg_Length / 2), 0, 0], size=[LeftLeg_Length, 0.2, 0.2])
        pyrosim.Send_Cube(name="RightLeg", pos=[(RightLeg_Length / 2), 0, 0], size=[RightLeg_Length, 0.2, 0.2])
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        

        # Creates a joint of format parent_child
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -BackLeg_Length, 0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, FrontLeg_Length, 0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-LeftLeg_Length, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[RightLeg_Length, 0, 0], jointAxis = "0 1 0")

        pyrosim.End()

    def Generate_Brain(self):
        # File to store desc of robot's body
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Wait for the file to be created
        while not os.path.exists(f"brain{self.myID}.nndf"):
            time.sleep(.01)

        # Add neuron
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")


        # Motor neuron
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 5, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 6, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 7, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name = 8, jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 9, jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 10, jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 11, jointName = "RightLeg_RightLowerLeg")



        # Synapses
        #pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 3, weight = 1.0)
        #pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 3, weight = 1.0)

        # Synapses
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])


        pyrosim.End()

    def Mutate(self):

        randomRow = numpy.random.randint(0,c.numSensorNeurons)
        randomColumn = numpy.random.randint(0,c.numMotorNeurons)

        self.weights[randomRow][randomColumn] = 2 * numpy.random.random() - 1
    
    def Set_ID(self, ID):

        self.myID = ID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        
        while not os.path.exists(f"brain{self.myID}.nndf"):
            time.sleep(0.05)

        os.system(f"start /B python3 simulate.py {directOrGUI} {self.myID}")

    def Wait_For_Simulation_To_End(self):

        # Wait for the file to be created
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(.01)

        with open(f"fitness{self.myID}.txt", 'r') as file:
            self.fitness = file.read()
        
        os.system(f"del fitness{self.myID}.txt")