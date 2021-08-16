'''
 Write a Python program to convert a byte string to a list of integers
'''

String = "Net4U is the best"
print("Original string:")
print(String)
nums = []
print("\nConvert bytes of the said string to a list of integers:")
for chr in String:
   nums.append(ord(chr))
print(nums)

