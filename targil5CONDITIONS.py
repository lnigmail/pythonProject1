#CONDITION 1 VARIABLE
a=input("Enter a name: ")
if (a=="idan"):
    print("it is good")
else:
    print("it isn't good!")

#2 VARIABLES name age
name=input("Enter a name: ")
if (name=="Ainshtein"):
    print("Hello Ainshtein\n")
else:
    print("Where is Ainshtein?\n")
age=int(input("Enter your age: "))
if (age==47):
    print("You've made it this far - respect!")
else:
    print("if only we could turn time back!")

#CONDITION if INSIDE CONDITION if
name=input("Enter a name: ")
if (name=="Ainshtein"):
    print("Hello Ainshtein\n")
    age = int(input("Enter your age: "))
    if (age == 47):
        print( "You've made it this far - respect!" )
    else:
        print( "if only we could turn time back!" )
else:
    print("Where is Ainshtein?\n")

#DOUBLE-CHECK CONDITION or and
name=input("Enter your name: \n")
age=int(input("Enter your age: \n"))
if((name=="ainshtein" or name=="Ainshtein") and (age<=47)):
    print("You're welcome to join the club!")
else:
    print("It was a nice chat")

#CONDITION >= equal&small
number=int(input("Enter a number: \n"))
if (number<=6):
    print(number*2)
else:
    print(number-1)

#CONDITION pass AS A CONDITIONED CONDITION (UNLESS if not CONDITIONED-IT RAISE FALSE)
if 4 or 5 < 7:
    print("good")
else:
    print("bad")
    if not 9:
        pass
    else:
        raise Exception("bad")

#REVERSING A FALSE CONDITION !=
if (5+3) > 10 and 'man' in 'mana' or 100 != 3 and 90 <=91:
    print("fa")
elif True is False:
    pass
else:
    print("else")

# http://www.tutorialspoint.com/python/python_basic_operators.htm