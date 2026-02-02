import math
import pyrosim.pyrosim as pyrosim

def Create_World():
    # Tell pyrosim the name of the file info about the world is stored in
    pyrosim.Start_SDF("world.sdf")

    # Stores a box with these specifications to . format
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])

    pyrosim.End()

def Create_Robot():
    # File to store desc of robot's body
    pyrosim.Start_URDF("body.urdf")

    # Stores a box with these specifications to . format
    pyrosim.Send_Cube(name="Torso", pos=[3, 3, 0.5], size=[1, 1, 1])

    pyrosim.End()

Create_World()
Create_Robot()