"""Calculates tax rates available period

This script  alows automaticaly calculate available resident periods
You have to suply file named triplog.csv , with next structure: Step in date , Step  out date
Date format  : day.month.fullYear 
"""
from datetime import datetime 

if __name__ == '__main__':
    date_in = '28.11.20'
    date_out ='09.05.21'

    date_in2 = '17.06.21'
    date_out2 = '07.07.21'

    trip1 =  datetime.strptime(date_out, "%d.%m.%y") - datetime.strptime(date_in, "%d.%m.%y")
    trip2 =  datetime.strptime(date_out2, "%d.%m.%y") - datetime.strptime(date_in2, "%d.%m.%y")

    total = trip1 + trip2
    
    print (total.days)
    