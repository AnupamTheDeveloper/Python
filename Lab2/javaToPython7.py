'''
Write a Python program for following grading system.
Note: Percentage>=90% : Grade A
Percentage>=80% : Grade B
Percentage>=70% : Grade C
Percentage>=60% : Grade D
Percentage>=40% : Grade E
'''

def determine_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 40:
        return 'E'
    else:
        return 'F'  

try:
    percentage = float(input("Enter the percentage: "))
    
    if percentage < 0 or percentage > 100:
        print("Percentage should be between 0 and 100.")
    else:
        grade = determine_grade(percentage)
        print(f"The grade for {percentage}% is: {grade}")
except ValueError:
    print("Please enter a valid number for the percentage.")
