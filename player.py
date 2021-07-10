from vectors import Vector2, Vector3, vector2_to_vector3
from world import World
from camera import Camera

class Player:
    _world: World = None
    _camera: Camera = None
    _position: Vector3 = Vector3()

    def __init__(self, camera, world, start_pos = Vector3()) -> None:
        self._camera = camera
        self._world = world
        self._position = start_pos
        self._camera.position = start_pos

    def walk(self, relative_amount: Vector2):
        self._position += vector2_to_vector3(relative_amount)
        self._camera.position += vector2_to_vector3(relative_amount)