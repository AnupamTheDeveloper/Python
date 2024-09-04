#allow for exam if student has 75% attendence
name=input("Enter your name:")
class_held=int(input("Enter total no. of class held:"))
attend_class=int(input("Enter number of class attend by the student:"))
percentage=int(attend_class/class_held*100)
print("%s attendence is %d percent"%(name,percentage))
if(percentage>=75):
    print("You are allow for exam")
else:
    print("You are not allow for exam")