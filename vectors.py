import numpy
import numpy as np

class Vector2:
    coords = numpy.array([0, 0])

    def __init__(self, x = 0, y = 0, do_round = False) -> None:
        if do_round:
            self.coords = numpy.array([round(x), round(y)])
        else:
            self.coords = numpy.array([float(x), float(y)])

    def __gt__(self, other):
        return self.coords.tolist() > other.coords.tolist()
    
    def __ge__(self, other):
        return self.coords.tolist() >= other.coords.tolist()

    def __ne__(self, other):
        return self.coords.tolist() != other.coords.tolist()
    
    def __eq__(self, other):
        return self.coords.tolist() == other.coords.tolist()
        
    def __lt__(self, other):
        return self.coords.tolist() < other.coords.tolist()
    
    def __le__(self, other):
        return self.coords.tolist() <= other.coords.tolist()

    def __getitem__(self, key):
        try:
            return self.coords.tolist()[key]
        except:
            return None

    def __setitem__(self, key, value):
        try:
            lst = self.coords.tolist()
            lst[key] = value
            self.coords = numpy.array(lst)
        except:
            pass

    def __delitem__(self, key):
        try:
            self[key] = 0
        except:
            pass

    def __str__(self) -> str:
        return "[" + str(self.coords[0]) + ", " + str(self.coords[1]) + "]"

    def __add__(self, other):
        self.coords += other.coords
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def round(self):
        for i in range(len(self.coords)):
            self[i] = int(round(self[i]))
        return self

    def normalize(self):
        self.coords = self.coords / numpy.linalg.norm(self.coords)
        return self

class Vector3(Vector2):
    coords = numpy.array([0, 0, 0])

    def __init__(self, x = 0, y = 0, z = 0, do_round = False) -> None:
        if do_round:
            self.coords = numpy.array([round(x), round(y), round(z)])
        else:
            self.coords = numpy.array([float(x), float(y), float(z)])
            
    def __str__(self) -> str:
        return "[" + str(self.coords[0]) + ", " + str(self.coords[1]) + ", " + str(self.coords[2]) + "]"

    def cross(self, other):
        self.coords = numpy.cross(self.coords, other.coords)
        return self

class Vector4(Vector3):
    coords = numpy.array([0, 0, 0, 0])

    def __init__(self, x = 0, y = 0, z = 0, w = 0, do_round = False) -> None:
        if do_round:
            self.coords = numpy.array([round(x), round(y), round(z), round(w)])
        else:
            self.coords = numpy.array([float(x), float(y), float(z), float(w)])

class Matrix4x4(numpy.ndarray):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

def vector2_to_vector3(v2: Vector2) -> Vector3:
    return Vector3(v2[0], v2[1], 0)

def vector3_to_vector2(v2: Vector3, round = False) -> Vector2:
    return Vector2(v2[0], v2[1], round)

def vector3_to_vector4(v2: Vector3, w = 1) -> Vector4:
    return Vector4(v2[0], v2[1], v2[2], w)

def vector4_to_vector3(v2: Vector4) -> Vector3:
    return Vector3(v2[0]/v2[3], v2[1]/v2[3], v2[2]/v2[3])

def vector_with_array(array: numpy.ndarray) -> Vector2:
    if len(array) == len(Vector2.coords):
        v2 = Vector2()
        v2.coords = array
        return v2
    elif len(array) == len(Vector3.coords):
        v3 = Vector3()
        v3.coords = array
        return v3
    elif len(array) == len(Vector4.coords):
        v4 = Vector4()
        v4.coords = array
        return v4
    else:
        raise ValueError("array length does not match")

def euler_to_quaternion(yaw, pitch, roll):
        qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
        qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
        qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

        return [qx, qy, qz, qw]

class static:
    v3_one = Vector3(1, 1, 1)
    v3_forward = Vector3(1, 0, 0)
    v3_backward = Vector3(-1, 0, 0)
    v3_up = Vector3(0, 0, 1)
    v3_down = Vector3(0, 0, -1)
    v3_left = Vector3(0, -1, 0)
    v3_right = Vector3(0, 1, 0)
    v2_one = Vector2(1, 1)
    v2_up = Vector2(1, 0)
    v2_down = Vector2(-1, 0)
    v2_left = Vector2(0, -1)
    v2_right = Vector2(0, 1)
