"""Task I"""

from math import ceil
from datetime import date

DAYS_NAMES = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
DAYS_NUMS = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
MONTHS_NUMS = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
               'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}


def days_in_year(year: int) -> int:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return 366
    else:
        return 365


def count_days(days_in_year: int, day_of_week: str) -> dict:
    day_of_week = DAYS_NUMS[day_of_week]
    days_quantity = dict()

    for i in range(7):
        days_quantity[(i + day_of_week) % 7] = ceil((days_in_year - i) / 7)

    return days_quantity


def days_for_weekend(year: int, holidays: list[str], day_of_week: str) -> str:
    all_days = days_in_year(year)
    days_dict = count_days(all_days, day_of_week)
    print(holidays)

    for day in holidays:
        print(day)
        day = day.split()
        print(day)
        day_date = date(year, MONTHS_NUMS[day[1]], int(day[0]))
        days_dict[day_date.weekday()] -= 1

    min_day = [key for key, value in days_dict.items() if value == min(days_dict.values())][0]
    max_day = [key for key, value in days_dict.items() if value == max(days_dict.values())][0]

    return f'{DAYS_NAMES[max_day]} {DAYS_NAMES[min_day]}'


def days_for_weekend_with_input():
    num = int(input())
    year = int(input())
    holidays = []
    for i in range(num):
        holidays.append(input())
    day_of_week = input()

    print(days_for_weekend(year, holidays, day_of_week))

days_for_weekend_with_input()


# print(days_for_weekend(2015, ['1 January', '8 January'], 'Thursday'))
# print(days_for_weekend(2013, ['1 January', '8 January', '15 January'], 'Tuesday'))
# print(days_for_weekend(2013, ['6  February', '13  February', '20  February'], 'Tuesday'))
