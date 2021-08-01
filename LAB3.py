'''Create variables: string of your name, another string of your mail.
Creater variable of your age (integer)
Print all of them to the screen

then print your name from the end to the begining and print it only with your age*3
Then check if your name is stored inside this full string:
"idan ben dudu yuval shimon yael gal adam shahar yana"'''

a="Leny"
b="lni8wallacoil@gmail.com"
c=47

print("Youre name is:= " + (a) + "\nYour mail is: " + (b) + "\nYour age is: " + str(c))

print("\nYoure name is: " + str(a[::-1]) + "\nYour age is: " + str(c*3))

print("\nLeny" in "idan ben dudu yuval shimon yael gal adam shahar yana")