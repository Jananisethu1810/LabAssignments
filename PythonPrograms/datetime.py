'''
import datetime
x=datetime.datetime.now()

print(x)
print(x.strftime('%A'))
print(x.strftime('%d'))
print(x.strftime('%B'))
'''
import datetime
from dateutil import tz

from_ist=tz.gettz('IST')
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('CET')
timenow=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
CurrentCet=datetime.datetime.strptime(str(timenow),'%Y-%m-%d %H:%M:%S').replace(tzinfo=from_ist).astimezone(to_zone)
CurrentCet=datetime.datetime.strptime(str(CurrentCet).split('+')[0], '%Y-%m-%d %H:%M:%S')
Subject0="Service level Warning tickets On "+ CurrentCet.strftime('%dth %B %Y %H:%M:%S')+" (CET)"
print(Subject0);
