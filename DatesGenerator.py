import datetime

from pyluach import dates, hebrewcal
from hebrew_numbers import int_to_gematria

import configuration


class DatesGenerator(object):
    def __init__(self, num_of_years):
        self.num_of_years = num_of_years

    def __call__(self, *args, **kwargs):
        desired_dates = self.generate_dates(*args, **kwargs)
        return desired_dates

    def generate_dates(self, date):
        # first_heb_date = dates.HebrewDate.from_pydate(datetime.datetime.strptime(date, configuration.DATE_FORMAT_CODE))
        first_heb_date = dates.HebrewDate.from_pydate(date)
        print(f"Generate {self.num_of_years} next dates corresponding the Hebrew date: {self.format(first_heb_date)}")
        desired_dates = [dates.HebrewDate(first_heb_date.year + i, first_heb_date.month, first_heb_date.day).to_greg()
                         for i in range(self.num_of_years)]
        return desired_dates

    def format(self, date):
        date = date.dict()
        date['month'] = hebrewcal.Month(date['year'], date['month']).name
        year_name = (int_to_gematria(int(str(date['year'])[0])) + int_to_gematria(int(str(date['year'])[1:])))
        return f"{int_to_gematria(date['day'])} {date['month']} {year_name[::-1]}"
