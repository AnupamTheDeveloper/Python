#Write a Python program to calculate the sum of natural numbers up to a certain range.
def sum_of_natural_numbers_loop(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

try:
    number = int(input("Enter the range (a positive integer): "))
    if number < 1:
        print("Please enter a positive integer.")
    else:
        sum_loop = sum_of_natural_numbers_loop(number)
        print(f"The sum of natural numbers up to {number} using loop is: {sum_loop}")
except ValueError:
    print("Please enter a valid integer.")
