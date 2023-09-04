# The circle module has functions that perform
# calculations related to circles.
import math

def calculateCircleParameters(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return area, circumference
