import datetime
import pytz

d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2023, 9, 16)
till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

print(dt + tdelta)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_mtn = datetime.datetime.now()
print(dt_mtn)

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
