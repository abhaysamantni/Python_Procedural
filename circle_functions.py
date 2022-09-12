# The circle module has functions that perform
# calculations related to circles.
import math

# The area function accepts a circle's radius as an
# argument and returns the area and circumference of the circle.
def calculate_area(radius, scaling_factor):
    """Return the area of the circle."""
    #return math.pi * radius**2
    #scaling_factor=1.23
    return scaling_factor*math.pi * radius**2
    
def calculate_circumference(radius):
    return math.pi * 2.0 * radius
    
    



