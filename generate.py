import math
import pyrosim.pyrosim as pyrosim

def Create_World():
    # Tell pyrosim the name of the file info about the world is stored in
    pyrosim.Start_SDF("world.sdf")

    # Stores a box with these specifications to . format    
    pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[1, 1, 1])

    pyrosim.End()

def Generate_Body():
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

def Generate_Brain():
    # File to store desc of robot's body
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # Add neuron
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()