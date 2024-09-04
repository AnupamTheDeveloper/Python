#allow for exam if student has 75% attendence and medical issue
name=input("Enter your name:")
medical_issue=input("If you have any madical issue press Y if not press N:")
class_held=int(input("Enter total no. of class held:"))
attend_class=int(input("Enter number of class attend by the student:"))
percentage=int(attend_class/class_held*100)
print("%s attendence is %d percent"%(name,percentage))
if(percentage>=75):
    print("You are allow for exam")
elif((percentage<75)and(medical_issue=='Y')):
    print("You are allow for exam")
else:
    print("You are not allow for exam")