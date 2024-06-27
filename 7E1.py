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
        if self.cross(other) == Vector(0, 0, 0):
            raise ValueError("Parallel vectors")
        c = self.cross(other)
        return Vector(c.x/c.length(),c.y/c.length(),c.z/c.length())
v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
x = Vector(1, 0, 0)
y = Vector(0, 1, 0)
z = Vector(0, 0, 1)
print (v.find_axis(w))
print (w.find_axis(z))
print (x.find_axis(y))
print (x.find_axis(z))
print (v.find_axis(v))
