#--------method 1---------
#take a number from user and reverse it
num = int(input("Enter any number:"))
reverse = (str(num)[::-1])
print("Reverse of the number is: {}".format(reverse))
#--------method 2---------
#using while loop
num1 = int(input("Enter the number:"))
r_num = 0
while num1!=0:
    digit=num1%10
    r_num=r_num*10+digit
    num1//=10
print(f"Reversed number:{r_num}")