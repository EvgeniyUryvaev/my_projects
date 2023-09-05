
"""Создаем классы фигур прямоугольника, квадрата и круга"""
import math
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2 # Возводим в квадрат

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return self.r ** 2 * math.pi # Вычисляем площадь круга по формуле S=п*r**2 . math.pi(число Пи)

