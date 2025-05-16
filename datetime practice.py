#datetime practice

import datetime


today = datetime.date.today()
print(today)

time = datetime.time(16, 8)
print(time)

now = datetime.datetime.now()
#print(now)

now1 = now.strftime("%d%m%y")
print(now1)

