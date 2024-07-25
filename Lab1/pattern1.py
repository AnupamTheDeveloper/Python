# 1
# 2 3 4
# 5 6 7 8 9
def printPattern(n):
    num=1
    if(n>0):
        for i in range(0,n):
            for j in range(0,2*i+1):
                print(num,end=' ')
                num+=1
            print("")
a = int(input("Enter the row number: "))
printPattern(a)