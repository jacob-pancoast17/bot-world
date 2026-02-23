import constants as c
import math
import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
from robot import ROBOT
from simulation import SIMULATION
import time
from world import WORLD

simulation = SIMULATION()
simulation.Run()
# BackLeg_amplitude = c.BackLeg_amplitude
# BackLeg_frequency = c.BackLeg_frequency
# BackLeg_phaseOffset = c.BackLeg_phaseOffset

# FrontLeg_amplitude = c.FrontLeg_amplitude
# FrontLeg_frequency = c.FrontLeg_frequency
# FrontLeg_phaseOffset = c.FrontLeg_phaseOffset




# # Create vector of angles
# BackLeg_angles = BackLeg_amplitude * numpy.sin(BackLeg_frequency * (numpy.linspace(0, 2*math.pi, num=c.simSteps)) + BackLeg_phaseOffset)
# FrontLeg_angles = FrontLeg_amplitude * numpy.sin(FrontLeg_frequency * (numpy.linspace(0, 2*math.pi, num=c.simSteps)) + FrontLeg_phaseOffset)
# #numpy.save('./data/back_leg_motor_data', BackLeg_angles)
# #numpy.save('./data/front_leg_motor_data', FrontLeg_angles)
# #exit()




# numpy.save('./data/back_leg_sensor_data', backLegSensorValues)
# numpy.save('./data/front_leg_sensor_data', frontLegSensorValues)

