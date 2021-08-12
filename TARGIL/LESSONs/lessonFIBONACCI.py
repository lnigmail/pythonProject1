from random import randint
from time import sleep

while("True"):
    choice = input("Menu:\n----\n1.Printing 100 numbers\n2.Check fibonachi\n3.randint numbers untill we get 12 or "
                    "the count is of 10 times\n")
    if (choice=="1"):
        # counter=100
        # while (counter=counter-1):
            print("(:"*100)

    elif (choice == "2"):
        #FIBONACHI LIST CONTAINS PREVIOUS+PREVIOUS=NEXT
        # fibonacci=[1,2,3,5,8,13,21]
        fibonacci=[]
        for i in range(7):
            fibonacci.append(int(input("Enter a number: ")))
        #a starting point
        boolean="True"
        #therefore; for i in range(2,len(6) in order to check from number3:
        for i in range(2,len(fibonacci)):
            print(fibonacci[i])
            print(fibonacci[i-1])
            print(fibonacci[i-2])
            print("\n")
            if fibonacci[i]!=(fibonacci[i-1]+fibonacci[i-2]):
                boolean="False"
                break
        if boolean=="True":
            print("It is fibonacci series")
        else:
            print("It isn't fibonacci series")

        # '''fibonacci=[1,2,3,5,8,13,21]
        # 3
        # 2
        # 1
        #
        # 5
        # 3
        # 2
        #
        # 8
        # 5
        # 3
        #
        # 13
        # 8
        # 5
        #
        # 21
        # 13
        # 8
        #
        # It is fibonacci series'''
        #
        #
        # '''fibonacci=[1,2,3,5,8,13,22]
        # 3
        # 2
        # 1
        #
        # 5
        # 3
        # 2
        #
        # 8
        # 5
        # 3
        #
        # 13
        # 8
        # 5
        #
        # 22
        # 13
        # 8
        #
        # It isn't fibonacci series'''
    elif (choice=="3"):
        counter=10
        for i in range(counter):
            print("\n\"Randint numbers for round" + str(i+1) + "\n---------------------------\n" )
            sleep( 1 )
            print( "   (: " )
            sleep( 1 )
            print( "        (: " )
            sleep( 1 )
            print( "              (: \n" )
            sleep( 3 )
            num=randint(1,12)
            print("The number is: " + str(num) + "\n")
            if (num==12):
                print("Congrats...\n")
                sleep(2)
                print("You're won in a minion\n")
                sleep(2)
                break
    else:
        print( "Enter 1-3 only!...\n")


# "Randint numbers for round1
# ---------------------------
#
#    (:
#         (:
#               (:
#
# The number is: 12
#
# Congrats...
#
# You're won in a minion
#
# Menu:
# ----
# 1.Printing 100 numbers
# 2.Check fibonachi
# 3.randint numbers untill we get 12 or the count is of 10 times
