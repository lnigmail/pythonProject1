
num=input("Enter a number to convert height to 7 centimeters: ")
choice=input("Enter from Menu:\n---------------\n1.feet\n2.inches\n ")
feet=(int(num))/(float(30.48))
inches=(int(num))/(float(2.54))
if (choice=="1"):
    print("This feet-number in 7 centimeters is: " + str(7*feet))
elif (choice=="2"):
    print("This inche-number in 7 centimeters is: " + str(7*inches))
else:
    print("Enter only feet or inches!")

print("\nAlwase a pleasure, Bye Bye...")

# Enter a number to convert height to 7 centimeters: 1
# Enter from Menu:
# ---------------
# 1.feet
# 2.inches
#  1
# This feet-number in 7 centimeters is: 0.22965879265091863
#
# Alwase a pleasure, Bye Bye...

# Enter a number to convert height to 7 centimeters: 1
# Enter from Menu:
# --------
# 1.feet
# 2.inches
#  2
# This inche-number in 7 centimeters is: 2.755905511811023
#
# Alwase a pleasure, Bye Bye...

# Enter a number to convert height to 7 centimeters: 3
# Enter from Menu:
# ---------------
# 1.feet
# 2.inches
#  3
# Enter only feet or inches!
#
# Alwase a pleasure, Bye Bye...
