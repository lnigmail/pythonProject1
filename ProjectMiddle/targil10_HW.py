# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.

# Expected output: {'N': 1, 'e': 1, 't': 2, '4': 1, 'U': 1}

import json
stringA = '{"N" : 1, "e" : 1, "t" : 2, "4" : 1, "U" : 1}'
#Given string dictionary
print("Given string: \n",stringA)
#Using Json.loads()
res = json.loads(stringA)
#Result
print("The converted dictionary: \n",res)

#  {"N" : 1, "e" : 1, "t" : 2, "4" : 1, "U" : 1}
# The converted dictionary:
#  {'N': 1, 'e': 1, 't': 2, '4': 1, 'U': 1}

