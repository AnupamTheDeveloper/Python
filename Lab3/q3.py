'''
Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which
calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
'''

import cmath

def _solve_quadratic_eqn(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero for a quadratic equation.")

    discriminant = b**2 - 4*a*c

    sol1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    sol2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return sol1, sol2

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
solutions = _solve_quadratic_eqn(a,b,c)
print(f"Solutions: {solutions[0]}, {solutions[1]}")
