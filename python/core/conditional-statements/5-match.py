"""
Match:

match expression:
    case 1:
        statement
    case 2:
        statement
    case 3:
        statement
    case 4:
        statement
    case _:
        statement

"""
# 0-m, 1- t....6-s

import datetime
day = datetime.datetime.now().weekday()

match day:
    case 0:
        print("Mon")
    case 1:
        print("Tue")
    case 2:
        print("Wed")
    case 3:
        print("Thu")
    case 4:
        print("Fri")
    case 5:
        print("Sat")
    case 6:
        print("Sun")
    case _:
        print("Invalid day")
