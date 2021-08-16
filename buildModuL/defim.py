from random import randint
def calculating(a,b):
    c=int(input("Enter a number: "))
    sum=a*b*c
    print("The sum is: " + str(sum))

def dogs_age(a):
    print("Real dog's age: " + str(a*7))
    return a*7

def Menu():
    choice=(input("Menu:\n----\n1.Printing 1-100\n2.random 2 cubes\n"))
    if choice=="1":
        for i in range(1,101):
            print (i)
    elif choice=="2":
        print("cube 1: " + str(randint(1,6)))
        print("cube 2: " + str(randint(1,6)))
    else:
        print("\nEnter 1-2 only!")