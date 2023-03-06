# if-statement
def numberOfDays(year: int, month: int) -> int:
    if month != 2:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        else:
            return 30
    else:
        isLeapYear = (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0)
        if isLeapYear:
            return 29
    return 28

# list
def numberOfDays(year: int, month: int) -> int:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 2:
        return days[month-1]
    isLeapYear = (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0)
    if isLeapYear:
        return 29
    return 28

year = 1900
month = 2
print(f"Output: {numberOfDays(year, month)}")