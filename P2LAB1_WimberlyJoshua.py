#Wimberly Joshua
#6/19/2025
#P2LAB1
#Using math expressions
import math
#Get radius user
radius = float(input("Enter the readius: "))

#Caculate circum, diameter, area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#display results
print(f"The diameter of the circle is {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")
