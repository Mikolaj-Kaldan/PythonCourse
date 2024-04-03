import datetime
def print_working_days(date1, date2):
    curr_date = date1
    while curr_date < date2:
        if curr_date.weekday() < 5:
            print(curr_date.date())
        curr_date += datetime.timedelta(days=1)
input = input()
date1, date2 = input.split()
print_working_days(datetime.datetime.fromisoformat(date1),datetime.datetime.fromisoformat(date2))
