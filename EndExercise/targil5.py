'''
Write a Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
'''
'''from random import randint

num1=randint(1,3)
num2=randint(1,3)
num3=randint(1,3)
print("\nRandintegers: " + "\n------------\nnum1: " + str(num1) + "\nnum2: " + str(
    num2) + "\nnum3: " + str(num3))
sum=num1+num2+num3
print("\nThe sum of the three given numbers: " + str(sum) + "\n")
if (num1==num2 or num2==num3 or num1==num3):
    print("Due to equal numbers:\n---------------------\n" +
           "Return three times of their sum: " + str(sum*3))'''


def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
