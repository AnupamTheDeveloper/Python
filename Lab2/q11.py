#Write a program in Python to find the sum of digits of a number.
def sum_of_digit(a):
    sum=0
    temp=a
    while(temp>0):
        rem=temp%10
        sum+=rem
        temp//=10
    return sum

num=int(input("enter any number: "))
result = sum_of_digit(num)
print(f"Sum of digit of {num}: {result}")