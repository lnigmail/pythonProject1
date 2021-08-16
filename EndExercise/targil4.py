'''
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
'''from datetime import datetime, timedelta

dt = datetime.now()

print("Date and Time= " + str(dt))

future_dt = dt + timedelta(days=9)
print("Expected output :  = " + str(future_dt))'''

from datetime import date
f_date = date(2021, 8, 1)
print(f_date)
l_date = date(2021, 8, 10)
print(l_date)
delta=l_date-f_date
print("Expected output : " + str(delta.days) + " days")