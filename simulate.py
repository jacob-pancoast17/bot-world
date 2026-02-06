import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

# Creates physics object and connects to GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# When enabled, this disables pybullet sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, -9.8, physicsClient)
# Creates a floor (needs pybullet_data imported)
planeId = p.loadURDF("plane.urdf")

# Create robot
robotId = p.loadURDF("body.urdf")

# Load our link
p.loadSDF("world.sdf")

# Sensor preparation
pyrosim.Prepare_To_Simulate(robotId)

# Create sensor storage (make n = number of steps in simulation)
backLegSensorValues = numpy.zeros(10000)

# Step simulator physics n times
for i in range(0, 10000):
    p.stepSimulation()

    # Create touch sensor   
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    time.sleep(.01)

print(backLegSensorValues)
p.disconnect()