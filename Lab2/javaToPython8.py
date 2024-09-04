# Write a Python program to print every alternate number of a given array
def print_alternate_numbers(array):
    
    for i in range(0, len(array), 2):
        print(array[i], end=' ')
    print()  

input_array = input("Enter elements of the array separated by spaces: ")

try:
    array = list(map(int, input_array.split()))
    print("Every alternate number in the array is:")
    print_alternate_numbers(array)
except ValueError:
    print("Please enter valid integers.")
