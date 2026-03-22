import numpy
import os
from pyrosim import pyrosim
import time

class SOLUTION:

    def __init__(self, ID):

        self.myID = ID

        # Create a 3x2 matrix of random weights scaled 
        # to be over the range [-1, 1]
        self.weights = 2 * numpy.random.rand(3, 2) - 1

    def Create_World(self):
        # Tell pyrosim the name of the file info about the world is stored in
        pyrosim.Start_SDF("world.sdf")

        # Stores a box with these specifications to . format    
        pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[1, 1, 1])

        pyrosim.End()

    def Generate_Body(self):
        # File to store desc of robot's body
        pyrosim.Start_URDF("body.urdf")

        # Stores a box with these specifications to . format
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        # Creates a joint of format parent_child
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5, 0, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5, 0, 1])

        pyrosim.End()

    def Generate_Brain(self):
        # File to store desc of robot's body
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Add neuron
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        # Motor neuron
        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

        # Synapses
        #pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 3, weight = 1.0)
        #pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 3, weight = 1.0)

        # Synapses
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight=self.weights[currentRow][currentColumn])


        pyrosim.End()

    def Mutate(self):

        randomRow = numpy.random.randint(0,3)
        randomColumn = numpy.random.randint(0,2)

        self.weights[randomRow][randomColumn] = 2 * numpy.random.random() - 1
    
    def Set_ID(self, ID):

        self.myID = ID

    def Start_Simulation(self, directOrGUI):

        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        os.system(f"start /B python3 simulate.py {directOrGUI} {self.myID}")

    def Wait_For_Simulation_To_End(self):

        # Wait for the file to be created
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(.01)

        with open(f"fitness{self.myID}.txt", 'r') as file:
            self.fitness = file.read()
        
        os.system(f"del fitness{self.myID}.txt")