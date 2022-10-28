from datetime import datetime, timedelta
from datetime import date
from pytz import timezone
import pytz
import holidays

now = datetime.now()
today_date = date.today()
united_states_holidays = holidays.UnitedStates()

west_coast = timezone('US/Pacific')
wc_time = datetime.now(west_coast)
central_time = timezone('US/Central')
c_time = datetime.now(central_time)
time = now.strftime("%H:%M:%S")

print("The Current Eastern Standard Time Is:", time)
print("The Current Central Standard Time Is:", c_time.strftime("%H:%M:%S"))
print("The Current Pacific Standard Time Is:", wc_time.strftime("%H:%M:%S"))

print("The current year is:", today_date.year)
print("The current month is:", today_date.month)
print("The current day of the week is:", today_date.day)

for ptr in holidays.UnitedStates(years = 2022).items():
    print(ptr)
