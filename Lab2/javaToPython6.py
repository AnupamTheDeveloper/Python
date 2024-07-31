#Write a Python program to search an element in an array
def search_element(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index
    return -1  

input_array = input("Enter elements of the array separated by spaces: ")
array = list(map(int, input_array.split()))
target = int(input("Enter the element to search for: "))

index = search_element(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
