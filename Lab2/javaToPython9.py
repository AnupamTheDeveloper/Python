# Write a Python program to find second highest element of an array
def find_second_highest_sorted(array):
    if len(array) < 2:
        return None  
    unique_sorted_array = sorted(set(array), reverse=True)
    
    if len(unique_sorted_array) < 2:
        return None  
    
    return unique_sorted_array[1]
input_array = input("Enter elements of the array separated by spaces: ")
try:
    array = list(map(int, input_array.split()))
    second_highest = find_second_highest_sorted(array)
    
    if second_highest is not None:
        print(f"The second highest element in the array is: {second_highest}")
    else:
        print("Not enough unique elements to determine the second highest.")
except ValueError:
    print("Please enter valid integers.")
