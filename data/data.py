"""дедлайн (результат лени)"""
import fnmatch
from datetime import date


def check_data(data):
    if fnmatch.fnmatch(data, '??.??.????') and \
            (''.join(data.split('.'))).isnumeric():
        day, month, year = [int(i) for i in data.split('.')]
        if ((month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32) or
                (month in [4, 6, 9, 11] and 0 < day < 31) or
                (month == 2 and 0 < day < 29)):
            return date(year, month, day)

        else:
            return "Wrong"
    else:
        return "Wrong"