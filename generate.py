import pyrosim.pyrosim as pyrosim

# Tell pyrosim the name of the file info about the world is stored in
# This link will contain a box
pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
z = 0
y = .5

# Stores a box with these specifications to box.sdf
pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[x, z, y], size=[length, width, height])

pyrosim.End()