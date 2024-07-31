#Define a sum function with two parameters and call the function

def sum_of_two(n1,n2):
    sum=n1+n2
    return sum

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

result=sum_of_two(a,b)
print(f"{a}+{b}={result}")