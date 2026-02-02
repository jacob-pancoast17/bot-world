import math
import pyrosim.pyrosim as pyrosim

def Create_World():
    # Tell pyrosim the name of the file info about the world is stored in
    pyrosim.Start_SDF("world.sdf")

    #Stores a box with these specifications to . format
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])

    pyrosim.End()

Create_World()