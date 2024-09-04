'''
Declare a function named print_list. It takes a list as a parameter and it prints out each
element of the list.
'''
def print_list(lst):
   print("[", end="")
   for i, element in enumerate(lst):
        if i != 0:
            print(", ", end="")
        print(f"{element}", end="")
   print("]")

user_input = input("Enter a list of elements separated by commas: ")
user_list = user_input.split(',')
user_list = [element.strip() for element in user_list]

print_list(user_list)
