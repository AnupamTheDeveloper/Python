#To solve the quadratic equation.

import cmath
def solve_quadratic(a, b, c):
    discri = b**2 - 4*a*c
    sol1 = (-b + cmath.sqrt(discri)) / (2 * a)
    sol2 = (-b - cmath.sqrt(discri)) / (2 * a)
    return sol1, sol2

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

solution1, solution2 = solve_quadratic(a, b, c)

print(f"The solutions are {solution1} and {solution2}")
