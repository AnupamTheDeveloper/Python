#take student marks and give them grade
marks=int(input("Enter the marks:"))
if(marks<25):
    print("You have %d marks and your grade is: F"%(marks))
elif((marks>=25) and (marks<=45)):
    print("You have %d marks and your grade is: E"%(marks))
elif((marks>45) and (marks<=50)):
    print("You have %d marks and your grade is: D"%(marks))
elif((marks>50)and (marks<=60)):
    print("You have %d marks and your grade is: C"%(marks))
elif((marks>60)and (marks<=80)):
    print("You have %d marks and your grade is: B"%(marks))
else:
    print("You have %d marks and your grade is: A"%(marks))