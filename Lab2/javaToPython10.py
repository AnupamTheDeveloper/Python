# Write a Python program to count the prime numbers in an array.
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(array):
    """Count the number of prime numbers in the array."""
    return sum(1 for num in array if is_prime(num))
input_array = input("Enter elements of the array separated by spaces: ")
try:
    array = list(map(int, input_array.split()))
    prime_count = count_primes(array)
    
    print(f"The number of prime numbers in the array is: {prime_count}")
except ValueError:
    print("Please enter valid integers.")
