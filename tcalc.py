"""Calculates tax rates available period

This script  alows automaticaly calculate available resident periods
You have to suply file named triplog.csv , with next structure: Step in date , Step  out date
Date format  : day.month.fullYear 
"""
from datetime import datetime 

# TODO: Realize file reasding from CSV File format . May be add .xls format reading.

if __name__ == '__main__':
    date_in = '28.11.2020'
    date_out ='09.05.2021'

    date_in2 = '17.06.2021'
    date_out2 = '07.07.2021'

    trip1 =  datetime.strptime(date_out, "%d.%m.%Y") - datetime.strptime(date_in, "%d.%m.%Y")
    trip2 =  datetime.strptime(date_out2, "%d.%m.%Y") - datetime.strptime(date_in2, "%d.%m.%Y")

    total = trip1 + trip2
    
    print (total.days)
    