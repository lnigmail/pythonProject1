

def positive(num):
 n = num-1
 total = 0
 while n > 0:
   total = total + (n * n * n)
   n = n-1
 return total
print("Cube sum of smaller than specified: ",positive(3))


