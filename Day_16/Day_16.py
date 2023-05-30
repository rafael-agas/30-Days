from datetime import *


# Date Time
# Current time

now = datetime.now()
print(now)
d = now.strftime("%m/%d/%Y, %H:%M:%S")
print(d)
today = "30 May, 2023"
date_today = datetime.strptime(today, "%d %B, %Y")
print(date_today)
# Difference between two times
today2 = date(year=2023, month=5, day=30)
new_year = date(year=2024, month=1, day=1)
old_date = date(year=1970, month=1, day=1)
time_left = new_year - today2
time_since = today2 - old_date
print(time_left)
print(time_since)