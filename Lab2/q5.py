#Compute a)sin of 60 degree b)cos of pi c)sin(0.8660254037844386) d)tan of 90 degree
import math

sin_60_degrees = math.sin(math.radians(60))
cos_pi = math.cos(math.pi)
sin_value = math.sin(0.8660254037844386)
try:
    tan_90_degrees = math.tan(math.radians(90))
except ValueError as e:
    tan_90_degrees = str(e)

print(f"Sin of 60={sin_60_degrees},cos of pi={cos_pi},sin(0.8660254037844386)={sin_value},tan of 90 degree{tan_90_degrees}")
