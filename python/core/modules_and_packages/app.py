import random

# print(random.random())
# print(random.randint(111111, 999999))

musics = [
    "song1",
    "song2",
    "song3",
    "song4",
    "song5",
    "song6"
]
# print(random.choice(musics))
# random.shuffle(musics)
# print(musics)
# print(random.randrange(1, 100, 2))
# print(dir(random))

# import datetime
# datetime.datetime.now()

from datetime import datetime, timedelta

# print(datetime.now())

current_time = datetime.now()

# print(current_time.date())
# print(current_time.day)
# print(current_time.month)
# print(current_time.year)

# print(current_time.time())
# print(current_time.hour)
# print(current_time.minute)
# print(current_time.second)
# print(current_time.microsecond)

# print(current_time.strftime('%d/%m/%Y, %H:%M:%S %p'))
# print(current_time.strftime('%d/%m/%Y, %I:%M:%S %p : - %a %A'))

# https://docs.python.org/3/library/datetime.html



# future time
# print(current_time + timedelta(weeks=1))

# past time
# print(current_time - timedelta(days=1))

import math

# print(dir(math))
# print(math.sqrt(16))
# print(math.sqrt(25))

# 5*4*3*2*1

# print(math.factorial(5))