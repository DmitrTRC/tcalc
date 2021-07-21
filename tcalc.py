"""Calculates tax rates available period

This script  alows automaticaly calculate available resident periods
You have to suply file named triplog.csv , with next structure: Step in date , Step  out date
Date format  : day.month.fullYear 
"""
import csv
from datetime import datetime
from typing import List, Tuple


# TODO: Realize file reasding from CSV File format . May be add .xls format reading.


def dates_from_csv(
    file_name: str = "triplog.csv", delimiter=":"
) -> List[Tuple[datetime, datetime]]:
    with open(file_name, "r") as csv_file:
        date_reader = csv.reader(csv_file, delimiter=delimiter)
        for index, row in enumerate(date_reader):
            print(index)
            print(row)


def get_trip_days():
    pass


if __name__ == "__main__":
    dates_from_csv()

    # trip1 = datetime.strptime(date_out, "%d.%m.%Y")
