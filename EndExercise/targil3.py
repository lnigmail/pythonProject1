'''
Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn
Sample value of n is 5
Expected Result : 615
'''
#
# print("Now we will accept an integer and compute the value...\n")
# for i in range (1):
#     n=input("Enter an integer: ")
#     print("\nPrinting: " + str(i+1))
#     print("\nThe value of n+nn+nnn is: " + str(int(n) + int(n+n) + int(n+n+n)))
#
# print("\nAlwase a pleasure...Bye Bye...")

n=int(input("Enter a number: "))
print(n + (n*10+n) + (n*100+n*10+n))





