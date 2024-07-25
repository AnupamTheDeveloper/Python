def isPerfect(x):
    if x<1:
        return False
    sum_of_divisors=0
    for i in range(1,x):
        if x%i==0:
            sum_of_divisors += i
        if(sum_of_divisors==x):
            return True 

def isArmstrong(n):
    digits = str(n)
    num_digits = len(digits)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    return sum_of_powers == n
a = int(input("Enter the number: "))
print("Case-1")
if(isPerfect(a)):
    print(f"{a} is a perfect number")
else:
    print(f"{a} is not a perfect number")
print("case-2")
if(isArmstrong(a)):
    print(f"{a} is a Armstrong number")
else:
    print(f"{a} is not a Armstrong number")