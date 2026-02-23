import constants as c
import math
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.BackLeg_amplitude
        self.frequency = c.BackLeg_frequency
        self.offset = c.BackLeg_phaseOffset

        if self.jointName == b'Torso_FrontLeg':
            self.frequency = self.frequency / 2

        # Create vector of angles
        self.motorValues = self.amplitude * numpy.sin(
            self.frequency * (
                numpy.linspace(
                    0, 2*math.pi, num = c.simSteps)
                    ) + self.offset
            )

    def Set_Value(self, robot, stepNum):
        # Create motor
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[stepNum],
            maxForce = c.maxForce
            )

    def Save_Values(self):
        path = './data/' + self.jointName + '_motor_data'
        numpy.save(path, self.motorValues)