import constants as c
import pybullet as p
import pybullet_data
from robot import ROBOT
import time
from world import WORLD

class SIMULATION:
    def __init__(self, directOrGUI):

        self.directOrGUI = directOrGUI

        # Creates physics object and connects to GUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)

        else:
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
            self.robot.Think()
            self.robot.Act(i)
            
            if self.directOrGUI == 'GUI':
                time.sleep(c.simSpeed)
    
    def Get_Fitness(self):

        self.robot.Get_Fitness()
