import pyrosim.pyrosim as pyrosim

# Tell pyrosim the name of the file info about the world is stored in
# This link will contain a box
pyrosim.Start_SDF("boxes.sdf")

iteration = 0

length = 1
width = 1
height = 1

x = 0
z = 0
y = .5


while iteration < 10:
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5 + iteration], size=[length, width, height])
    iteration += 1
# Stores a box with these specifications to . format
#pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
#pyrosim.Send_Cube(name="Box2", pos=[1, 0, 1.5], size=[length, width, height])

pyrosim.End()