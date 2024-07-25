def primeSeries(n):
    if (n==1) or (n==0): return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num = int(input("enter any number: "))
print("prime number from 1 to {}".format(num))
for i in range(1,num+1):
    if(primeSeries(i)):        print(i,end=" ")
