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
            print("Congrats...\n")
            sleep(2)
            print("You're won in a minion\n")
            sleep(2)
            print("You win the house: \n")
            sleep(1)
        else:
            prize_money=prize_money+100
            print("U\n")
            sleep(1)
            print("r\n")
            sleep(1)
            print("1\n")
            sleep(1)
            print("in a hundred...\n")
            sleep(1)
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

'''
Welcome to the CUBE THRILL...

Each turn cost 3 NIS (;

Enter the amount of money you wish to burn...
10
Your change: 1 NIS

You have 3 turns...


Rolling the dice for round number 1
----------------------------------

   (: 
        (: 
              (: 

cube1: 6
cube2: 5

Calculating the damage...


                  (: 
          (: 
   (: 

Your prize money is: 0 NIS




Rolling the dice for round number 2
----------------------------------

   (: 
        (: 
              (: 

cube1: 6
cube2: 6

Congrats...

You're won in a minion

You win the house: 

Calculating the damage...


                  (: 
          (: 
   (: 

Your prize money is: 1000 NIS




Rolling the dice for round number 3
----------------------------------

   (: 
        (: 
              (: 

cube1: 5
cube2: 1

Calculating the damage...


                  (: 
          (: 
   (: 

Your prize money is: 1000 NIS'''