#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""circle.py: The circle module, which defines the Circle class"""
from math import pi
 
class Circle:
 
    def __init__(self, _radius = 1.0):
        self.set_radius(_radius)   # Call setter
 
    def set_radius(self, _radius):
        if _radius < 0:
            raise ValueError('Radius shall be non-negative')
        self._radius = _radius
 
    def get_radius(self):
        return self._radius
 
    def get_area(self):
        return self.get_radius() * self.get_radius() * pi  # Call getter
 
    def __repr__(self):
        return 'Circle(radius={})'.format(self.get_radius())  # Call getter
 
if __name__ == '__main__':
    c1 = Circle(1.2)        # Constructor and Initializer
    print(c1)               # Invoke __repr__(). Output: Circle(radius=1.200000)
    print(vars(c1))         # Output: {'_radius': 1.2}
    print(c1.get_area())    # Output: 4.52389342117
    print(c1.get_radius())  # Run Getter. Output: 1.2
    c1.set_radius(3.4)      # Test Setter
    print(c1)               # Output: Circle(radius=3.400000)
    c1._radius = 5.6        # Access instance variable directly (NOT recommended but permitted)
    print(c1)               # Output: Circle(radius=5.600000)
 
    c2 = Circle()  # Default radius
    print(c2)      # Output: Circle(radius=1.000000)
 
    #c3 = Circle(-5.6)  # ValueError: Radius shall be non-negative