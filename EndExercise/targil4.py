'''
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import datetime, timedelta

dt = datetime.now()

print("Date and Time= " + str(dt))

future_dt = dt + timedelta(days=9)
print("Future Date and Time  = " + str(future_dt))