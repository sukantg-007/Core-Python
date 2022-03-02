import datetime as dt
date=dt.datetime.now()
print(date)
print("Todays date : {:%d/%m/%y}".format(date))
print("Todays Time : {:%H:%M:%S}".format(date))
print("Todays Time : {:%d/%m/%y %H:%M:%S}".format(date))