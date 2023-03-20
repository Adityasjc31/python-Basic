# Write a python program to find the roots of a quadratic equation.
import math


print("Equation format : ax²+bx+c")
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

D = (b*b) - 4*a*c

r1 = (-b+math.sqrt(D))/2
r2 = (-b-math.sqrt(D))/2

print("Two roots are ",r1,",",r2)