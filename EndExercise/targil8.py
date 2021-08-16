'''
Write a Python program to convert height (in feet and inches) to
centimeters.
'''
def Menu():
    while "True":

        num=input("Enter a number to convert height to centimeters: ")
        choice=input("Enter from Menu:\n---------------\n1.feet\n2.inches\n ")
        feet=(int(num))/(float(30.48))
        inches=(int(num))/(float(2.54))
        if (choice=="1"):
            print("This feet-integer in centimeters is: " + str(feet))
        elif (choice=="2"):
            print("This inche-integer in centimeters is: " + str(inches))
        else:
            print("Enter only feet or inches!")
            continue

        exit=input("\nDo you want to exit? yes/no\n")
        if (exit=="yes"):
            break
        else:
            print("Welcome back!\n")
    print("\nAlwase a pleasure, Bye Bye...")

Menu()