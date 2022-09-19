# The circle module has functions that perform
# calculations related to circles.
import math

# The area function accepts a circle's radius as an
# argument and returns the area and circumference of the circle.
#def calculateArea(radius):

    #return math.pi * radius**2
#    return math.pi * radius**2

def multiple_functions(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference, diameter
