def divisibleBy(n):
    if(n%7==0) and (n%5!=0):
        return True
    return False
print("Numbers that divisible by 7 and not multiple of 5 from 1000 to 2000 are")
for i in range(1000,2001):
    if (divisibleBy(i)):
        print(i,end=",")
