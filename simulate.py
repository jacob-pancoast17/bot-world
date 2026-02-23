import constants as c
import math
import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

BackLeg_amplitude = c.BackLeg_amplitude
BackLeg_frequency = c.BackLeg_frequency
BackLeg_phaseOffset = c.BackLeg_phaseOffset

FrontLeg_amplitude = c.FrontLeg_amplitude
FrontLeg_frequency = c.FrontLeg_frequency
FrontLeg_phaseOffset = c.FrontLeg_phaseOffset

# Creates physics object and connects to GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# When enabled, this disables pybullet sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, c.gravity, physicsClient)
# Creates a floor (needs pybullet_data imported)
planeId = p.loadURDF("plane.urdf")

# Create robot
robotId = p.loadURDF("body.urdf")

# Load our link
p.loadSDF("world.sdf")

# Sensor preparation
pyrosim.Prepare_To_Simulate(robotId)

# Create sensor storage (make n = number of steps in simulation)
backLegSensorValues = numpy.zeros(c.simSteps)
frontLegSensorValues = numpy.zeros(c.simSteps)

# Create vector of angles
BackLeg_angles = BackLeg_amplitude * numpy.sin(BackLeg_frequency * (numpy.linspace(0, 2*math.pi, num=c.simSteps)) + BackLeg_phaseOffset)
FrontLeg_angles = FrontLeg_amplitude * numpy.sin(FrontLeg_frequency * (numpy.linspace(0, 2*math.pi, num=c.simSteps)) + FrontLeg_phaseOffset)
#numpy.save('./data/back_leg_motor_data', BackLeg_angles)
#numpy.save('./data/front_leg_motor_data', FrontLeg_angles)
#exit()

# Step simulator physics n times
for i in range(0, c.simSteps):
    p.stepSimulation()

    # Create touch sensor  s 
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Create motor
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = BackLeg_angles[i],
        maxForce = c.maxForce
        )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = FrontLeg_angles[i],
        maxForce = c.maxForce
        )

    time.sleep(.01)

numpy.save('./data/back_leg_sensor_data', backLegSensorValues)
numpy.save('./data/front_leg_sensor_data', frontLegSensorValues)

p.disconnect()