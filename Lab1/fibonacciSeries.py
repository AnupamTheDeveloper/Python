def fibonacci(n):
    if n<=0:
       return "please give possitive integer"
    fibonacci_series=[0,1]
    while len(fibonacci_series)<n:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series[:n]
try:
    term = int(input("Enter the number of terms in the Fibonacci series: "))
    series = fibonacci(term)
    print(f"The first {term} terms of the Fibonacci series are: {series}")
except ValueError:
    print("Please enter valid input")