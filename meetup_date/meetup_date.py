from datetime import date, timedelta
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(
    year: int, month: int, nth: int = 4, weekday: [int | Weekday] = 3
):
    """
    Function which returns day of the month if available for Python Meetup
    :param year:
    :param month:
    :param nth:
    :param weekday:
    :return:
    """
    if isinstance(weekday, Weekday):
        _weekday = weekday.value
    else:
        _weekday = weekday

    days_in_week = 7
    if month < 1 or month > 12:
        raise ValueError("Month should be between 1-12!")

    if _weekday < 0 or _weekday > 6:
        raise ValueError("Weekday should be between 0-6!")

    if nth < 0:
        # get last weekday
        somewhere_next_month = date(
            year=year, month=month, day=28
        ) + timedelta(days=4)
        last_day_of_month = somewhere_next_month - timedelta(
            days=somewhere_next_month.day
        )
        last_day_of_month_weekday = last_day_of_month.weekday()
        if last_day_of_month_weekday != _weekday:
            if last_day_of_month_weekday > _weekday:
                delta = last_day_of_month_weekday - _weekday
            else:
                delta = (last_day_of_month_weekday + days_in_week) - _weekday
            last_weekday = last_day_of_month - timedelta(days=delta)
        else:
            last_weekday = last_day_of_month
        last_weekday = last_weekday - timedelta(
            days=((nth * -1) - 1) * days_in_week
        )
        if last_weekday.month != month:
            raise ValueError("Out of month's scope!")

        return last_weekday

    first_day_of_month = date(year=year, month=month, day=1)
    first_day_of_month_weekday = first_day_of_month.weekday()
    if first_day_of_month_weekday != _weekday:
        if first_day_of_month_weekday < _weekday:
            delta = days_in_week - first_day_of_month_weekday
        else:
            delta = days_in_week - (first_day_of_month_weekday - _weekday)
        first_weekday = first_day_of_month + timedelta(days=delta)
    else:
        first_weekday = first_day_of_month

    if nth:
        first_weekday = first_weekday + timedelta(
            days=(nth - 1) * days_in_week
        )

    if first_weekday.month != month:
        raise ValueError("Out of month's scope!")

    return first_weekday


print("\n[B] Bonus1")  # @todo debug
print(
    f"\n[i] meetup_date(year=2023, month=8): {meetup_date(year=2023, month=8)}"
)  # @todo debug


print(
    "\n[i] SD Python:", meetup_date(2015, 8, nth=4, weekday=3)
)  # @todo debug
# SD Python: 2015-08-27
print(
    "\n[i] PyLadies on 4th Wed:", meetup_date(2018, 7, nth=4, weekday=2)
)  # @todo debug
# PyLadies on 4th Wed: 2018-07-25
print(
    "\n[i] SDJS on 1st Tues:", meetup_date(2012, 2, nth=1, weekday=1)
)  # @todo debug
# SDJS on 1st Tues: 2012-02-07

print("\n[B] Bonus2")  # @todo debug
print(
    "\n[i]SDHN on last Friday:", meetup_date(2010, 6, nth=-1, weekday=4)
)  # @todo debug
# SDHN on last Friday: 2010-06-25
print(
    "\n[i]-1 != 4 (sometimes):", meetup_date(2020, 1, nth=-1, weekday=4)
)  # @todo debug
# -1 != 4 (sometimes): 2020-01-31

print("\n[B] Bonus3")  # @todo debug
print(
    "\n[i] SDJS", meetup_date(2012, 2, nth=1, weekday=Weekday.TUESDAY)
)  # @todo debug
# SDJS 2012-02-07
print(
    "\n[i] PyLadies", meetup_date(2018, 7, nth=2, weekday=Weekday.WEDNESDAY)
)  # @todo debug
# PyLadies 2018-07-11
print(
    "\n[i] SDHN", meetup_date(2010, 6, nth=-1, weekday=Weekday.FRIDAY)
)  # @todo debug
# SDHN 2010-06-25
