#Write a program in Python that prompts the user to input a number and prints its
#multiplication table.
a=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")