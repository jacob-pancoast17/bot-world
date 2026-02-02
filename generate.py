import math
import pyrosim.pyrosim as pyrosim

# Tell pyrosim the name of the file info about the world is stored in
# This link will contain a box
pyrosim.Start_SDF("world.sdf")

length = 1
width = 1
height = 1

x = 0
z = 0
y = .5

#Stores a box with these specifications to . format
pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
#pyrosim.Send_Cube(name="Box2", pos=[1, 0, 1.5], size=[length, width, height])

pyrosim.End()