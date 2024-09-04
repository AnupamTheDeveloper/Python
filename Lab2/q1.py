##To find the sum of square root of any three numbers.
import math
def sum_sqr_root(n1,n2,n3):
    sqr_n1=math.sqrt(n1)
    sqr_n2=math.sqrt(n2)
    sqr_n3=math.sqrt(n3)
    total = sqr_n1+sqr_n2+sqr_n3
    return total

a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=float(input("Enter 3rd number: "))
answer=sum_sqr_root(a,b,c)

print(f"The sum of square root of {a},{b},{c}is: {answer}")