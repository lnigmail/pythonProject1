'''
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2'''

from itertools import count
## initializing string
string="thequickbrownfoxjumpsoverthelazydog"
## initializing a dictionary
duplicates = {}
for char in string:
    ## checking whether the char is already present in dictionary or not
   if char in duplicates:
      ## increasing count if present
      duplicates[char] += 1
   else:
      ## initializing count to 1 if not present
      duplicates[char] = 1
for key, value in duplicates.items():
   if value > 1:
      print(key, end = " ")
      print(value)

print()
'''
t 2
h 2
e 3
u 2
r 2
o 4
'''