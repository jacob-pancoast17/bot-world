import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
from world import WORLD

class SIMULATION:
    def __init__(self):
        # Creates physics object and connects to GUI
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # When enabled, this disables pybullet sidebars
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setGravity(0, 0, c.gravity, self.physicsClient)

        self.robot = ROBOT()
        self.world = WORLD()
    
    def __del__(self):
        p.disconnect()

    def Run(self):
        # Step simulator physics n times
        for i in range(0, c.simSteps):
            p.stepSimulation()

            # # Create touch sensors 
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            # # Create motor
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = self.robot.robotId,
            #     jointName = b'Torso_BackLeg',
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = BackLeg_angles[i],
            #     maxForce = c.maxForce
            #     )
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = self.robot.robotId,
            #     jointName = b'Torso_FrontLeg',
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = FrontLeg_angles[i],
            #     maxForce = c.maxForce
            #     )
            
            time.sleep(.01)
