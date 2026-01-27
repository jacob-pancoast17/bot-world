import pyrosim.pyrosim as pyrosim

# Tell pyrosim the name of the file info about the world is stored in
# This link will contain a box
pyrosim.Start_SDF("box.sdf")

# Stores a box with these specifications to box.sdf
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])

pyrosim.End()