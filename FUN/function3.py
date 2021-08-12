# def calculating():
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter a number: "))
#     sum=(num1*num2)
#     print("Your new number is: " + str(sum))
#     return sum
#
# a=calculating()+29
# print("wow: " + str(a))

def calculating2(x,y):
    print("Your first number: " + str(x) + "\nYour second number: " + str(y))
    sum=(x*y)
    print("\nYour new number is: " + str(sum))
    return sum

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
idan=calculating2(a,b)+29
print("wow: " + str(idan))