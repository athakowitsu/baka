import datetime
import calendar
def get_weekday(date):
    d = datetime.datetime.strptime(date,'%d-%m-%y')
    return(calendar.day_name[d])
print(get_weekday('13-08-2021'))