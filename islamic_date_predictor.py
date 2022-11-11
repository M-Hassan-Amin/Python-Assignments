import datetime as dt
from datetime import datetime as dc

curyear = dt.date(2022,10,9)
print(curyear)
us = input("select your year : ")
cus = dc.strptime(us,'%Y').date()
print(cus.year)
# cusb = cus.strftime('%Y')
# print(type(cusb))
if cus.year > curyear.year:
    dif = cus.year - curyear.year
    remove = dif*10
    day = curyear+dt.timedelta(-remove)
    a = day.month
    print(f"12th Rabiulawal of year {cus.year} is", dt.date(cus.year,day.month,day.day))