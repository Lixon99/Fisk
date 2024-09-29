import math

class Vector:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def __getLength__(self):
        return (self.__x ** 2 + self.__y ** 2) ** 0.5

    def length(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def __dotProduct__(self, other):
        return self.__x * other.get_x() + self.__y * other.get_y()

    def __str__(self):
        return f"Vector is: x = {self.__x}, y = {self.__y}"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.__x + other.__x, self.__y + other.__y)
        else:
            raise TypeError(f"Cannot add Vector with {type(other)}")
    
    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.__dotProduct__(other)
        else:
            return Vector(self.__x * other, self.__y * other)
    
    def __truediv__(self, skalar):
        if skalar == 0:
            raise ValueError("Kan ikke dividere med 0")
        return Vector(self.__x / skalar, self.__y / skalar)            
        
    def distance_to(self, other):
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - self.__y) ** 2)
    
    def normalize(self):
        length = self.__getLength__()
        if length != 0:
            return Vector(self.__x / length, self.__y / length)
        else:
            return Vector(0, 0)  # Hvis længden er 0, returner en nulvektor
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
  
"""
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

"""