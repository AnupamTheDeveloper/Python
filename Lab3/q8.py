'''
Write a program to compute cosine of x. The user should supply x and a positive integer n.
We compute the cosine of x using the series and the computation should use all terms in the
series up through the term involving xn
cos x = 1 - x2/2! + x4/4! - x6/6! ....
'''
import math

def factorial(num):
    """Compute factorial of a given number."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def cos_series(x, n):
    """Compute cos(x) using the series expansion up to the nth term."""
    cos_x = 0.0
    for i in range(n):
        term = ((-1)**i) * (x**(2 * i)) / factorial(2 * i)
        cos_x += term
    return cos_x

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))

result = cos_series(x, n)
print(f"The computed value of cos({x}) using {n} terms is: {result}")
