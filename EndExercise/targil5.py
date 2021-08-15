'''
Write a Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
'''
from random import randint

num1=randint(1,3)
num2=randint(1,3)
num3=randint(1,3)
print("Randintegers: " + "\n------------\nnum1: " + str(num1) + "\nnum2: " + str(
    num2) + "\nnum3: " + str(num3))
if (num1==num2 or num2==num3 or num1==num3):
    sum=num1+num2+num3
    print("\nDue to equal numbers:\n---------------------\n" 
          "The sum of the three given numbers: " + str(sum) + "\n" +
          "Return three times of their sum: " + str(sum*3))