import pybullet as p
import pybullet_data
import time

# Creates physics object and connects to GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# When enabled, this disables pybullet sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, -9.8, physicsClient)
# Creates a floor (needs pybullet_data imported)
planeId = p.loadURDF("plane.urdf")

# Load our link
p.loadSDF("boxes.sdf")

# Step simulator physics 1000 times
for i in range(0, 1000):
    p.stepSimulation()
    time.sleep(.1)
    print(i)

p.disconnect()