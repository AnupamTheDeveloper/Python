#Enter the number from the user and depending on whether the number is even or odd, 
#print out an appropriate message to the user.
num=int(input("enter any number:"))
if(num%2==0):
    print("%s is a even number"%(num))
else:
    print("%s is a odd number:"%(num))