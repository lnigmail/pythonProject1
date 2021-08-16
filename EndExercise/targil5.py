'''
Write a Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
'''

def sum_identicle(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_identicle(1, 2, 3))
print(sum_identicle(3, 3, 3))
