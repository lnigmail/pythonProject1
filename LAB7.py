#LAB7-Cube Project
from random import randint
from time import sleep
print("Welcome to the CUBE THRILL...\n\nEach turn cost 3 NIS (;\n")
spend=int(input("Enter the amount of money you wish to burn...\n"))
turns=spend//3
print("Your change: " + str(spend%3) + " NIS\n")
print("You have " + str(turns) + " turns...")
prize_money=0
for i in range(turns):
    print("\n\nRolling the dice for round number " + str(i+1) + "\n----------------------------------\n")
    sleep(1)
    print("   (: ")
    sleep(1)
    print("        (: ")
    sleep(1)
    print("              (: \n")
    sleep(3)
    cube1=randint(1,6)
    cube2=randint(1,6)
    print("cube1: " + str(cube1) + "\ncube2: " + str(cube2) + "\n")
    if (cube1==cube2):
        if (cube1==6):
            prize_money=prize_money+1000
            print("Congrats... You're won in a minion, You win the house: ")
        else:
            prize_money=prize_money+100
    elif (cube2==2):
        prize_money=prize_money+40
    elif (cube1==1):
        prize_money=prize_money+20
    print("Calculating the damage...\n\n")
    sleep(1)
    print("                  (: ")
    sleep(1)
    print("          (: ")
    sleep(1)
    print("   (: \n")
    sleep(3)
    print("Your prize money is: " + str(prize_money) + " NIS\n\n")
    sleep(5)

