import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "Vector(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __ne__(self, other):
        return not self == other
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    def find_axis(self, other):
        if v.cross(w) == Vector(0, 0, 0):
            raise ValueError("Parallel vectors")
        return v.cross(w)*(1/length(v.cross(w)))
v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
print (v.find_axis(w))
