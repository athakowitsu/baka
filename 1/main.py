import datetime as df
def get_weekday(date):
    d = df.datetime.strptime(date,'%d-%m-%Y')
    return(d.strftime('%A'))
 
print(get_weekday("13-10-2021"))