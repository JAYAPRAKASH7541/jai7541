#import datetime
#import pytz

'''s=datetime.date.today()
print(s.day)'''
'''bday=datetime.date(2020,7,2)
tday=datetime.date.today()
print((bday-tday).days)'''
'''s=datetime.datetime(2016,3,4,12,13,49,tzinfo=pytz.UTC)
#print(s)
dt_now=datetime.datetime.now(tz=pytz.UTC)
#print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
#print(dt_utcnow)
dt_mtn = dt_utcnow().astimezone(pytz.timezone('Indian/Maldives'))
print(dt_mtn)'''

#for tz in pytz.all_timezones:
#    print(tz)'''
#import json
x = '''{
  "name": "John",
  "age": 30,
  "married": true,
  "divorced": false,
  "children": ("Ann","Billy"),
  "pets": null,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}'''
'''data=json.loads(x)
print(type(data))
print(data)'''

with open('stxt.txt','r') as f:
    f_con=f.read()
    print(f_con)



























