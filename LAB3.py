'''Create variables: string of your name, another string of your mail.
Create variable of your age (integer)
Print all of them to the screen

then print your name from the end to the begining and print it only with your age*3
Then check if your name is stored inside this full string:
"idan ben dudu yuval shimon yael gal adam shahar yana"'''

a="Ainshtein"
b="Ainshtein@gmail.com"
c=47

print("Your name is: " + (a) + "\nYour mail is: " + (b) + "\nYour age is: " + str(c))

print("\nYour name is: " + str(a[::-1]) + "\nYour age is: " + str(c*3))

print("\nAinshtein" in "idan ben dudu yuval shimon yael gal adam shahar yana")

'''
Your name is:= Leny
Your mail is: lni8wallacoil@gmail.com
your age is: 47

Your name is: yneL
Your age is: 141
False
'''