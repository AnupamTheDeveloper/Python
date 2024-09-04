#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    if x1==x2:
        raise ValueError("The slope is undefined")
    slope = (y2-y1)/(x2-x1)
    return slope

p1=int(input("Enter value of x1:"))
p2=int(input("Enter value of y1:"))
p3=int(input("Enter value of x2:"))
p4=int(input("Enter value of y2:"))
try:
    print(calculate_slope(p1,p2,p3,p4))
except ValueError as e:
    print(e)