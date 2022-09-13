# days in month
from leef import is_leef


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if is_leef(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print(days_in_month(year, month))
