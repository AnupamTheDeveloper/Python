#Write a python program to find median of a set of numbers.
def find_median(numbers):
    # Sort the list of numbers
    numbers.sort()
    
    n = len(numbers)
    
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        median = (mid1 + mid2) / 2
    
    return median

input_numbers = input("Enter a set of numbers separated by spaces: ")
numbers = list(map(float, input_numbers.split()))
median = find_median(numbers)
print("The median of the given set of numbers is:", median)
