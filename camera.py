from os import altsep
from numpy import cos, sin
import numpy
from display import Display
from vectors import Matrix4x4, Vector2, Vector3, Vector4, vector3_to_vector2, vector3_to_vector4, vector4_to_vector3, vector_with_array


class Camera:
    position: Vector3 = Vector3()
    rotation: Vector3 = Vector3()
    display: Display = None
    _fov: float = 60

    projection_matrix: Matrix4x4 = None

    def __init__(self, display, fov = 60) -> None:
        self.display = display
        self.position = Vector3()
        self.rotation = Vector3()
        self._fov = fov
        self.projection_matrix = self.get_matrix()

    """
    The original C++-code I constructed this from is from this website: https://www.gamedev.net/forums/topic/59091-projection-matrix-amp-3d-to-2d-conversion/
    """

    def get_matrix(self) -> Matrix4x4:
        result = numpy.array([
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ])
        aspect = self.display.columns / self.display.lines
        fov = self._fov
        nearZ = 1.0
        farZ = -1.0
        w = aspect * ( cos(fov/2)/sin(fov/2) )
        h = 1.0 * ( cos(fov/2)/sin(fov/2) )
        q = farZ / ( farZ - nearZ )
        result[0][0] = w
        result[1][1] = h
        result[2][2] = q
        result[2][3] = 1.0
        result[3][2] = -q  *nearZ
        return result

    def world_to_screen(self, vector3: Vector3) -> Vector2:
        # print(vector3.coords)
        # print(self.projection_matrix)
        v4 = vector_with_array(numpy.dot(self.projection_matrix, vector3_to_vector4(vector3).coords))
        # print(v4.coords)
        return vector_with_array(vector3_to_vector2(vector4_to_vector3(v4)).coords + Vector2(self.display.columns / 2, self.display.lines / 2).coords).round()

    def screen_to_world(self, vector2) -> Vector3:
        pass

if __name__ == "__main__":
    cam = Camera(Display(100, 15), 120)
    print(cam.world_to_screen(Vector3(0, 100, 100)))