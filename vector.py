import math

class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)
            
    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)
    
    def __mul__(self, other):
        return Vector(self.__x * other, self.__y * other)
    
    def __truediv__(self, skalar):
        if skalar == 0:
            raise ValueError("Kan ikke dividere med 0")
        return Vector(self.__x / skalar, self.__y / skalar)
    
    def __str__(self):
        return f"Vector is: x = {self.__x}, y = {self.__y}"
    
    def getLength(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def normalize(self):
        length = self.length()
        if length != 0:
            return Vector(self.__x / length, self.__y / length)
        else:
            return Vector(0, 0)  # Return 0 vector hvis length is 0

    def distance(self, other):
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)