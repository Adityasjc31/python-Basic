#  Write a python program to find the volume of cylinder and cone.

import math

radius = float(input("Enter radius of cylinder : "))
height = float(input("Enter height of cylinder : "))

vol = math.pi * radius*radius * height

print("Volume of cylinder : ",vol)

radius = float(input("Enter radius of cone : "))
height = float(input("Enter height of cone : "))

vol = math.pi * radius*radius * height * (1/3)

print("Volume of cone : ",vol)