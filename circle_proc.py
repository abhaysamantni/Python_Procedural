# The circle module has functions that perform
# calculations related to circles.
import math

# The area function accepts a circle's radius as an
# argument and returns the area and circumference of the circle.
def area(radius, scalingFactor):

    #return math.pi * radius**2
    return scalingFactor * math.pi * radius**2


