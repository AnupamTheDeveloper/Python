'''
Write a Python program that prompts the user to enter a base number and an exponent,
and then calculates the power of the base to the exponent. The program should not use the
exponentiation operator (**) or the math.pow() function.
'''
def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    for _ in range(exponent):
        result *= base
    
    return result
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)

print(f"{base} to the power of {exponent} is {result}")
