# from django.test import TestCase

# # Create your tests here.

import datetime

import pytz


print(TIME_ZONE)
# from overtime.models import Multiplier
m1 = 1.5
m2 = 2
m3 = 2.5
m4 = 3

current_day = datetime.datetime.today().weekday()
slu_tz = pytz.timezone("America/St_Lucia")
time_in_st_lucia = datetime.datetime.now(slu_tz).strftime("%H:%M")
# currentTimeInNewYork = time_in_st_lucia.strftime("%H:%M")


def get_weekday(current_day):
    if current_day != 5 or current_day != 6:
        return True
    return False


def get_weekend(current_day):
    if current_day == 5 or current_day == 6:
        return True
    return False


# def is_before_mid_night(current_time_hour)

# print(get_weekday(current_day))
# print(get_weekend(current_day))

midnight = datetime.datetime.strptime("0:00", "%H:%M").time()
current_time_hour = datetime.datetime.now().time().strftime("%H:%M")
print(time_in_st_lucia)

# def get_current_day_time():
#     current_day = datetime.today().weekday()+3
#     current_time_hour = datetime.now().time().strftime("%H:%M")
#     midnight = datetime.strptime("0:00", "%H:%M").time()
#     midnight_str = str(midnight)
#     print(current_day, "#", current_time_hour, "#", type(midnight_str))
#     if current_day != 0 or current_day != 6 and current_time_hour < midnight:
#         print('weekday before midnight')
#         if current_day != 0 or current_day != 6 and current_time_hour > midnight_str:
#             print('weekday after midnight')

# else:
#     print('Weekend before might now')


# get_current_day_time()
