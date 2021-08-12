from time import sleep
def Menu():
    while "True":
        choice=input("Menu:\n----\n1.Dogs details\n2.Friends list\n3.N AZZERET\n")
        if (choice=="1"):
            Dogs()

        elif (choice=="2"):
            Friends()

        elif (choice=="3"):
            Azzeret()

        else:
            print( "Enter 1-3 only!\n" )
            continue

        exit=input("\nDo you want to exit? yes/no\n")
        if (exit=="yes"):
            break
        else:
            print("Welcome back!\n")
    print( "\nAlwase a pleasure, Bye Bye...\n" )


def Dogs():
    name=input(("Enter the Dog's name: "))
    age=int(input(("Enter the Dog's age: ")))
    print("\nDog's name: " + name + "\nDog's age: " + str(age*7) + "\n")

def Friends():
    list_friends=[]
    for i in range(5):
        list_friends.append(input("Enter a friend's name: "))
    name=input("Enter a new name: ")
    if (name in list_friends):
         print(name + " is already in the list!\n")
    else:
        print(name + " isn't inside the list!\n")

def Azzeret():
    num=int(input("Enter a number: "))
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    print(str(num) + " Azzeret is: " + str(sum) + "\n")



Menu()

'''
Menu:
----
1.Dogs details
2.Friends list
3.N AZZERET
1
Enter the Dog's name: nature
Enter the Dog's age: 7

Dog's name: nature
Dog's age: 49


Do you want to exit? yes/no
no
Welcome back!

Menu:
----
1.Dogs details
2.Friends list
3.N AZZERET
2
Enter a friend's name: et
Enter a friend's name: phone
Enter a friend's name: home
Enter a friend's name: right
Enter a friend's name: now
Enter a new name: et
et is already in the list!


Do you want to exit? yes/no
no
Welcome back!

Menu:
----
1.Dogs details
2.Friends list
3.N AZZERET
3
Enter a number: 7
7 Azzeret is: 5040


Do you want to exit? yes/no
n
Welcome back!

Menu:
----
1.Dogs details
2.Friends list
3.N AZZERET
5
Enter 1-3 only!

Menu:
----
1.Dogs details
2.Friends list
3.N AZZERET
3
Enter a number: 1
1 Azzeret is: 1


Do you want to exit? yes/no
yes

Alwase a pleasure, Bye Bye...
'''