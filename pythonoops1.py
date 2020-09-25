#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import math
 
class Cuboid: 
 
    def __init__(self, length, breadth, height):
        self.l = length
        self.b = breadth
        self.h = height

    def total_surface_area(self):
    	return 2*((self.l * self.b) + (self.b * self.h) + (self.h * self.l))

    def lateral_surface_area(self):
    	return 2*self.h*(self.l + self.b)

    def volume(self):
    	return self.l * self.b * self.h

    def diagonal_legth(self):
    	return math.sqrt(self.l*self.l + self.b*self.b + self.h*self.h)


if __name__ == '__main__':
 	cuboid1 = Cuboid(2,3,4)
 	tsa1 = cuboid1.total_surface_area()
 	lsa1 = cuboid1.lateral_surface_area()
 	v1 = cuboid1.volume()
 	dl1 = cuboid1.diagonal_legth()

 	print(tsa1, lsa1, v1, dl1)
