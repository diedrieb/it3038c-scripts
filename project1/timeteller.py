from datetime import datetime
from pytz import timezone

now = datetime.now()

west_coast = timezone('US/Pacific')
wc_time = datetime.now(west_coast)
central_time = timezone('US/Central')
c_time = datetime.now(central_time)
time = now.strftime("%H:%M:%S")

print("The Current Eastern Standard Time Is:", time)
print("The Current Central Standard Time Is:", c_time.strftime("%H:%M:%S"))
print("The Current Pacific Standard Time Is:", wc_time.strftime("%H:%M:%S"))
