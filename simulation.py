import constants as c
import pybullet as p
import pybullet_data
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

            self.robot.Sense(i)
            self.robot.Act(i)
            
            time.sleep(c.simSpeed)
