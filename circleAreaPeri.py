# Write a python program to find the area and circumference of a circle.

import math


radius = float(input("Enter radius of circle : "))
Area = radius*radius*math.pi
circumference = 2*math.pi*radius

print("Area : ",Area)
print("Cirumference : ",circumference)