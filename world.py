import pybullet as p

class WORLD:
    def __init__(self):
        # Creates a floor (needs pybullet_data imported)
        self.planeId = p.loadURDF("plane.urdf")

        # Load our link
        p.loadSDF("world.sdf")

