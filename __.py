from datetime import datetime

print((datetime.now() - datetime(2001, 1, 17, 13, 9, 27)).total_seconds() / 86400)
from datetime import date, timedelta

start_day = date(2001, 1, 17)
current_period_start = start_day + timedelta(days=((date.today() - start_day).days // 100) * 100)
current_period_end = current_period_start + timedelta(days=99)

print(current_period_start)
print(current_period_end)
