class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def __getLength__(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def __dotProduct__(self, other):
        return self.__x * other.get_x() + self.__y * other.get_y()

    def __str__(self):
        return f"Vector is: x = {self.__x}, y = {self.__y}"

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)
    
    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.__dotProduct__(other)
        else:
            return Vector(self.__x * other, self.__y * other)
    
    def __truediv__(self, skalar):
        if skalar != 0:
            return Vector(self.__x / skalar, self.__y / skalar)
        else:
            raise ValueError("Kan ikke dividere med 0")
    
  

v1 = Vector(4, 2)
v2 = Vector(3, 2)

# Addition, subtraktion, multiplikation og division
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 2
v6 = v1 / 2

#Dot produkt
v7 = v1 * v2
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
print(v7)

