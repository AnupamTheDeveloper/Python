#program to check if the number is divisible by both 7 and 5 or not
num=int(input("Enter the number:"))
if((num%5==0) and (num%7==0)):
    print("The number is divisible by both 5 and 7")
elif((num%5==0) and (num%7 !=0)):
    print("The number is only divided by 5")
elif((num%5!=0)and (num %7==0)):
    print("The number is only divided by 7")
else:
    print("The number is not divisible by both 5 and 7")