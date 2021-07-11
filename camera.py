from os import altsep

import numpy
from numpy import cos, sin

from display import Display
from vectors import (Matrix4x4, Vector2, Vector3, Vector4, static,
                     vector2_to_vector3, vector3_to_vector2,
                     vector3_to_vector4, vector4_to_vector3, vector_with_array)


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
        self.projection_matrix = self.get_projection_matrix()

    """
    The original C++-code I constructed this from is from this website: https://www.gamedev.net/forums/topic/59091-projection-matrix-amp-3d-to-2d-conversion/
    """

    def get_projection_matrix(self) -> Matrix4x4:
        result = numpy.array([
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0]
        ])
        aspect = self.display.columns / self.display.lines
        fov = numpy.deg2rad(self._fov)
        nearZ = 0.1
        farZ = -500.0
        w = aspect * ( cos(fov/2)/sin(fov/2) )
        h = 1.0 * ( cos(fov/2)/sin(fov/2) )
        q = farZ / ( farZ - nearZ )
        result[0][0] = w
        result[1][1] = h
        result[2][2] = q
        result[2][3] = 1.0
        result[3][2] = -q  *nearZ
        return result

    """
    Converted from C++-code from https://www.3dgep.com/understanding-the-view-matrix/
    """

    # def get_view_matrix(self, target_point: Vector3):
    #     zaxis = vector_with_array(self.position.coords - target_point.coords).normalize()
    #     xaxis = static.v3_up.cross(zaxis).normalize()
    #     yaxis = zaxis.cross(xaxis)
    #     result = numpy.array([
    #         [xaxis[0], yaxis[0], zaxis[0], 0.0],
    #         [xaxis[1], yaxis[1], zaxis[1], 0.0],
    #         [xaxis[2], yaxis[2], zaxis[2], 0.0],
    #         [-numpy.dot(xaxis.coords, self.position.coords),
    #         -numpy.dot(yaxis.coords, self.position.coords),
    #         -numpy.dot(zaxis.coords, self.position.coords), 1.0]
    #     ])
    #     return result

    def get_view_matrix(self):
        pitch = numpy.deg2rad(self.rotation[0])
        yaw = numpy.deg2rad(self.rotation[1])
        cosPitch = cos(pitch)
        sinPitch = sin(pitch)
        cosYaw = cos(yaw)
        sinYaw = sin(yaw)

        xaxis = Vector3(cosYaw, 0, -sinYaw)
        yaxis = Vector3(sinYaw * sinPitch, cosPitch, cosYaw * sinPitch)
        zaxis = Vector3(sinYaw * cosPitch, -sinPitch, cosPitch * cosYaw)

        result = numpy.array([
            [xaxis[0], yaxis[0], zaxis[0], 0.0],
            [xaxis[1], yaxis[1], zaxis[1], 0.0],
            [xaxis[2], yaxis[2], zaxis[2], 0.0],
            [-numpy.dot(xaxis.coords, self.position.coords),
            -numpy.dot(yaxis.coords, self.position.coords),
            -numpy.dot(zaxis.coords, self.position.coords), 1.0]
        ])
        return result;


    """
    Programmed by tutorial from https://wiki.flightgear.org/Howto:Project_3D_to_2D_coordinates_on_desktop_canvas
    """

    def world_to_screen(self, vector3: Vector3) -> Vector2:
        # print(vector3.coords)
        # print(self.projection_matrix)
        v4_view_normalized = numpy.dot(self.get_view_matrix(), vector3_to_vector4(vector3).coords)
        v4 = vector_with_array(numpy.dot(self.projection_matrix, v4_view_normalized))
        v3_view_norm1 = Vector3((v4[0] + 1) * 0.5, (v4[1] + 1) * 0.5, (v4[2] + 1) * 0.5)
        v2_view = Vector2(v3_view_norm1[0] * self.display.columns, v3_view_norm1[1] * self.display.lines)
        # print(v4.coords)
        # return vector_with_array(vector3_to_vector2(vector4_to_vector3(v4)).coords + Vector2(self.display.columns / 2, self.display.lines / 2).coords).round()
        return v2_view.round()

    def screen_to_world(self, vector2) -> Vector3:
        pass

if __name__ == "__main__":
    cam = Camera(Display(100, 15, "-"), 60)
    cam.display.set_pixel(cam.world_to_screen(Vector3(0.0001, 0.0, 0)), "X")
    cam.display.render()
