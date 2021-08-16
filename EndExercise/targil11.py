'''
Write a Python function that takes a positive integer and returns the sum
of the cube of all the positive integers smaller than the specified number.
'''

def positive(num):
 num = num-1
 total = 0
 while num > 0:
   total = total + (num * num * num)
   num = num-1
 return total
print("Cube sum of smaller than specified: ",positive(3))


