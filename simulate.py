import math
import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

amplitude = math.pi/4
frequency = 1
phaseOffset = 0 

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
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# Create vector of angles
angles = amplitude * numpy.sin(frequency * (numpy.linspace(0, 2*math.pi, num=1000)) + phaseOffset)
#numpy.save('./data/sin', angles)

# Step simulator physics n times
for i in range(0, 1000):
    p.stepSimulation()

    # Create touch sensor  s 
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Create motor
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = angles[i],
        maxForce = 20
        )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = angles[i],
        maxForce = 20
        )

    time.sleep(.01)

numpy.save('./data/back_leg_sensor_data', backLegSensorValues)
numpy.save('./data/front_leg_sensor_data', frontLegSensorValues)

p.disconnect()