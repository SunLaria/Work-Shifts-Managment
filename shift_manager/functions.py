import datetime

def weeks_for_year(year):
    last_week = datetime.date(year, 12, 28)
    return last_week.isocalendar().week
