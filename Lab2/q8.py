#Write a function to calculate the power of a number using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent > 1:
        return base * power(base, exponent - 1)
    if exponent < 0:
        return 1 / power(base, -exponent)

base = 5
exponent = 3
result = power(base, exponent)
print(f"{base} to the power of {exponent} is {result}")
