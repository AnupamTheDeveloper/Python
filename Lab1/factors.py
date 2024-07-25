def printFactor(n):
    print("factors of {}".format(n))
    for i in range(1,n+1):
        if n%i ==0:
            print(i)

num = int(input("Enter any number: "))
printFactor(num)