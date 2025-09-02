"""
Lecture05b.py
====================================
This introduces the concepts of a Python class.

From:
    https://runestone.academy/ns/books/published/fopp/Classes/ObjectsasArgumentsandParameters.html

| Seth McNeill
| 2025 September 02
"""

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. 
    
    Attributes
    ----------
    initX
      Initial x coordinate for point
    initY
      Initial y coordinate for point

    """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        """
        Returns the X coordinate
        """
        return self.x

    def getY(self):
        """
        Returns the Y coordinate
        """
        return self.y

    def distanceFromOrigin(self):
        """
        Calculates the distance from the origin to the point
        """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(self, point2):
        """
        Calculates the distance from *this* point to point2
        """
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(4,3)
q = Point(0,0)
print(p.distance(q))
