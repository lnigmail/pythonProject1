'''
Write a Python program to sum of two given integers. However, if the sum
is between 15 to 20 it will return 20.
'''
from random import randint

num1=randint(1,20)
num2=randint(1,20)
sum=num1+num2
if (sum<=20 and sum>=15):
    print("Due to sum>=15 or sum<=20 : sum=20")
else:
    print("\nThe sum of the randintegers: " + "\n------------\nnum1: " + str(num1) + "\nnum2: " + str(num2))

print("\nAlwase a pleasure, Bye Bye...")