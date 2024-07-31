#Print the series upto N terms: 1,2,6,24,120,720 …
import math

def factorial_series(n):
    series = []
    for i in range(1, n + 1):
        series.append(math.factorial(i))
    return series
N = int(input("Enter the number of terms to print: "))
series = factorial_series(N)
print("The first", N, "terms of the factorial series are:", series)
