import pybullet as p
import time

# Creates physics object and connects to GUI
physicsClient = p.connect(p.GUI)

# When enabled, this disables pybullet sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# Step simulator physics 1000 times
for i in range(0, 1000):
    p.stepSimulation()
    time.sleep(.1)
    print(i)

p.disconnect()