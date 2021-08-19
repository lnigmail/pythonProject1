from random import randint
from time import sleep
counter=1
print("Welcome to the LOTTERY THRILL...\n\nEach turn cost 3 NIS (;\n")
spend=int(input("how much money do you have?...\n"))
turns=spend//3
print("Your change: " + str(spend%3) + " NIS\n")
print("You have " + str(turns) + " turns...")
prize_money=0
num=randint(1,6)

for i in range(turns):
    print("\n\nRolling the dice for round number " + str(i + 1) + "\n----------------------------------\n")
    sleep(1)
    print("   (: ")
    sleep(1)
    print("        (: ")
    sleep(1)
    print("              (: \n")

    num1 = randint(1, 37)
    num2 = randint(1, 37)
    num3 = randint(1, 37)
    num4 = randint(1, 37)
    num5 = randint(1, 37)
    num6 = randint(1, 37)
    lotostring = num1, num2, num3, num4, num5, num6
    print(lotostring)
    sleep(5)
    duplicates = {}
    for char in lotostring:
        if char in duplicates:
            duplicates[char] = duplicates[char] + 1
        else:
            duplicates[char] = 1
    for key, value in duplicates.items():
        if value == 6:
            print(value)
            prize_money = prize_money + 1000000
            print("You're won in a MiNion\n")
            sleep(2)
            print("You did it...\n")
            sleep(2)
            print("You win the WINNER's number  *,*   ^,^     W-O-W........     \n")

        elif value == 5:
            print(value)
            prize_money = prize_money + 5000
            print("Congrats     *_*     \n")
            sleep(2)
            print("You did it           *,*     \n")
            sleep(2)
            print("...You're second best        ^_*     \n")

        elif value == 4:
            print(value)
            prize_money = prize_money + 100
            print("U\n")
            sleep(1)
            print("r\n")
            sleep(1)
            print("won in a hundred...  ^_^\n")




print("Calculating the damage...\n")
sleep(1)
print("                  (: ")
sleep(1)
print("          (: ")
sleep(1)
print("   (: \n")
sleep(3)
print("Your prize money is: " + str(prize_money) + " NIS\n\n")
#
# Welcome to the LOTTERY THRILL...
#
# Each turn cost 3 NIS (;
#
# how much money do you have?...
# 6
# Your change: 0 NIS
#
# You have 2 turns...
#
#
# Rolling the dice for round number 1
# ----------------------------------
#
#    (:
#         (:
#               (:
#
# (3, 3, 2, 3, 3, 6)
# 4
# U
#
# r
#
# won in a hundred...  ^_^
#
#
#
# Rolling the dice for round number 2
# ----------------------------------
#
#    (:
#         (:
#               (:
#
# (6, 4, 1, 1, 5, 1)
# Calculating the damage...
#
#                   (:
#           (:
#    (:
#
# Your prize money is: 100 NIS