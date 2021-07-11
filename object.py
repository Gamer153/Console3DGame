from vectors import Vector2, Vector3, static
from display import Display
from camera import Camera
import random
from numpy import linalg

class Object:
    position = Vector3()
    size = Vector3()
    block = "█"
    id = 0

    def __init__(self, position: Vector3, size: Vector3 = static.v3_one, block = "█") -> None:
        self.position = position
        self.position[0] = position[0]
        self.position[1] = position[1]
        self.position[2] = position[2]
        self.size[0] = size[0]
        self.size[1] = size[1]
        self.size[2] = size[2]
        self.id = random.randint(153, 2000000000)
        self.block = block

    def render(self, cam: Camera):
        if linalg.norm(cam.position.coords) <= linalg.norm(self.position.coords):
            pos = cam.world_to_screen(self.position)
            cam.display.set_pixel(pos, self.block)
            with open("pos.txt", "a") as f:
                f.write("obj id " + str(self.id) + " with pos " + str(self.position) + " told to render at " + str(pos) + "\n")
