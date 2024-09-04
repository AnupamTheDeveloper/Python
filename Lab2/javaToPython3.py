#Write a Python Program to check if a number is Positive or Negative.
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

try:
    number = float(input("Enter a number: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Please enter a valid number.")
