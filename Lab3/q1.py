'''
Write a function called check-season, it takes a month parameter and returns the season:
Autumn, Winter, Spring or Summer.
'''
def checkSeason(month):
    month=month.lower()
    if month in ['december','january','fecruary']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'
    
user_month=input("Enter the month:")
print(checkSeason(user_month))