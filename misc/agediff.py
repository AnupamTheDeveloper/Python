#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import datetime

name=input("Enter your name:")
age=int(input("enter yout age:"))
hundred=int((100-age)+datetime.now().year)

print("Hi %s your age in %s and you will be 100 years old in %s."%(name,age,hundred))
