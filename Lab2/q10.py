#Write a program in Python to check if a number is Krishnamurthy number.
import math
def Krishnamurthy_number(a):
    sum_of_fact=0
    temp=a

    while(temp>0):
        reminder=temp%10
        sum_of_fact+=math.factorial(reminder)
        temp//=10
    return sum_of_fact==a

num=int(input("Enter any number: "))
if Krishnamurthy_number(num):
    print(f"{num} is a Krishnamurthy number")
else:
    print(f"{num} is not a Krishnamurthy number")