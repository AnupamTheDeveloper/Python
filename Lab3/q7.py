'''
Write a program to compute sin x for given x. The user should supply x and a positive integer
n. We compute the sine of x using the series and the computation should use all terms in the
series up through the term involving xn
sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........
'''
import math

def factorial(num):
    """Compute factorial of a given number."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sin_series(x, n):
    """Compute sin(x) using the series expansion up to the nth term."""
    sin_x = 0.0
    for i in range(n):
        term = ((-1)**i) * (x**(2 * i + 1)) / factorial(2 * i + 1)
        sin_x += term
    return sin_x

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))

result = sin_series(x, n)
print(f"The computed value of sin({x}) using {n} terms is: {result}")
