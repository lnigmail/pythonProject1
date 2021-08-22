from random import randint
from time import sleep

def menu():
    while True:
        choice = input("Menu:\n----\na. Marketing budjet\nb. Lotto game\n")
        if choice == "a":
            marketing_budget()

        elif choice == "b":
            lottery()

        else:
            print("Enter a or b only!\n")
            continue
        exit = input("\nDo you want to exit? yes/no ")
        if (exit == "yes"):
            print("Bye, Bye...")
            break
        else:
            print("Welcome back!\n")



def marketing_budget():
    print("Pricelisting:\n-----------\nFacebook campaign=100 ILS per day\nInstagram campaign 50 ILS per day\n")
    budget=int(input("How much money do you have?: "))
    facebook=int(input("\nEnter how many days would you like the Facebook campaign to run?"))
    instagram=int(input("\nEnter how many days would you like the Instagram campaign to run?"))

    print("\nSummary of the cost:\n-------------------\nFacebook: " + str(facebook) + " days" + "\nInstagram: " + str(
        instagram) + " days")

    summary=(facebook*100)+(instagram*50)
    summary1 = summary * 1.17 - budget
    print("You have to pay: " + str("%.2f" % (summary*1.17)) + " ILS with tax")
    sum1=facebook*100
    sum2=instagram*50
    if summary < budget:
        print( "\nsuccessfull" )
    else:
        print( "\nPlease add: " + str( summary1 * 1.17 ) + " ILS" )



def lottery():
    counter=1
    print("Welcome to the LOTTERY THRILL...\n\nEach turn cost 3 ILS (;\n")
    spend=int(input("how much money do you have?...\n"))
    turns=spend//3
    print("Your change: " + str(spend%3) + " ILS\n")
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
                print("won in a hundred...  ^_^     \n")




    print("Calculating the damage...\n")
    sleep(1)
    print("                  (: ")
    sleep(1)
    print("          (: ")
    sleep(1)
    print("   (: \n")
    sleep(3)
    print("Your prize money is: " + str(prize_money) + " ILS\n\n")



menu()