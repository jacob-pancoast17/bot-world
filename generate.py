import pyrosim.pyrosim as pyrosim

# Tell pyrosim the name of the file info about the world is stored in
# This link will contain a box
pyrosim.Start_SDF("box.sdf")

length = 1
width = 2
height = 3

x = 0
z = 0
y = 1.5

# Stores a box with these specifications to box.sdf
pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])

pyrosim.End()