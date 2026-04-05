import math

BackLeg_amplitude = math.pi/4
BackLeg_frequency = 5
BackLeg_phaseOffset = -math.pi/2

FrontLeg_amplitude = math.pi/4
FrontLeg_frequency = 5
FrontLeg_phaseOffset = 0

gravity = -9.8

simSteps = 100

maxForce = 20

simSpeed = .02

numberOfGenerations = 5

populationSize = 1

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 0.5

numLegs = 4