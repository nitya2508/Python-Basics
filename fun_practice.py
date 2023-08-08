month_days = [0, 31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """Returns true for leap year, False for non leap year""" #doc string

    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)

def get_month_days(year, month):
    """returns number of days in that month in that year"""
    if not 1<= month <= 12:
        return "Invalid month"
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]


print(is_leap(2020))
print(get_month_days(2022,2))
 