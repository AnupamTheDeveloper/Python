#Write a python program to find area and perimeter of a circle.
import math
r=float(input("Enter the radiyus of the circle: "))
area=math.pi*r**2
perimeter=2*math.pi*r
print(f"The perimeter of the circle is: {perimeter:.2f}")
print(f"The area of the circle is: {area:.2f}")