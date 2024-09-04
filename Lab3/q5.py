'''
Declare a function named reverse_list. It takes an array as a parameter and it returns the
reverse of the array (use loops).
'''
def reverse_list(arr):
    """
    Function to reverse an array using loops.
    
    Parameters:
    arr (list): The list to be reversed.
    
    Returns:
    list: The reversed list.
    """
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Get user input
user_input = input("Enter a list of elements separated by commas: ")

# Convert the user input into a list
user_list = user_input.split(',')

# Remove any extra whitespace from each element
user_list = [element.strip() for element in user_list]

# Reverse the list
reversed_user_list = reverse_list(user_list)

# Print the reversed list
print("Reversed list:", reversed_user_list)
