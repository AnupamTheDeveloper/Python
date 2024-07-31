#Write a Python program to calculate Sum & Average of an integer array.
def calculate_sum_and_average(numbers):
    if len(numbers) == 0:
        return 0, 0  

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return total_sum, average

input_numbers = input("Enter integers separated by spaces: ")

try:
    numbers = list(map(int, input_numbers.split()))
    total_sum, average = calculate_sum_and_average(numbers)
    print(f"The sum of the array is: {total_sum}")
    print(f"The average of the array is: {average:.2f}")
except ValueError:
    print("Please enter valid integers.")
