import math
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


# Generate a tower
for i in range(0, 5):
    for j in range(0, 5):
        iteration = 0
        while iteration < 10:
            pyrosim.Send_Cube(name="Box",
                            pos=[i, j, 0.5 + iteration],
                                size=[1 * math.pow(0.9, iteration),
                                        1 * math.pow(0.9, iteration),
                                        1 * math.pow(0.9, iteration)])
            iteration += 1
#Stores a box with these specifications to . format
#pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
#pyrosim.Send_Cube(name="Box2", pos=[1, 0, 1.5], size=[length, width, height])

pyrosim.End()