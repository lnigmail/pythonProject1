'''
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''

def calculating2(x,y):
    print("x= " + str(x) + "\ny= " + str(y))
    print("\nThe return result of (x+y)*(x+y): " + str((x+y)*(x+y)))

x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
calculating2(x,y)