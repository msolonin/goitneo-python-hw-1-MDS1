# -*- coding: utf-8 -*-
"""
Method for parsing users bitrhdays
"""

import calendar
from datetime import datetime


def get_birthdays_per_week(users):
    days_in_week = 7
    result = {}
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        else:
            birthday_this_year = birthday_this_year.replace(year=today.year)
        delta_days = (birthday_this_year - today).days
        if delta_days < days_in_week:
            weekday = birthday_this_year.weekday()
            day_name = calendar.day_name[weekday]
            if weekday in [5, 6]:
                day_name = calendar.day_name[0]
            if day_name in result:
                result[day_name] = result[day_name] + ', ' + name
            else:
                result[day_name] = name
    # Get names of week days from numbers
    week_days = [calendar.day_name[_] for _ in range(days_in_week)]
    # Print structured data from monday to friday
    for weekday in week_days:
        if weekday in result:
            print("{}: {}".format(weekday, result[weekday]))
