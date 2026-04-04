import os
import pybullet as p

class WORLD:
    def __init__(self, simID):
        # Creates a floor (needs pybullet_data imported)
        self.planeId = p.loadURDF("plane.urdf")

        # Load our link
        p.loadSDF(f"world{simID}.sdf")

        # Delete world file
        os.system(f"del world{simID}.sdf")

