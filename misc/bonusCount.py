#add 5% bonous if service year more than 5 year
from datetime import datetime
salary=int(input("Enter the salary:"))
bonous=int(salary*0.05)
start_date=input("Enter the date when your job start(YYYY-MM-DD):")
user_date=datetime.strptime(start_date,"%Y-%m-%d")
current_date=datetime.now()
time_diff=current_date-user_date
division_result=time_diff.days
if(division_result>=1825):
    total_salary=int(salary+bonous)
    print(f"Your salary is:{total_salary}")
else:
    total_salary=salary
    print(f"Your salary is:{total_salary}")