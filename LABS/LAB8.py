from random import randint

while(True):

    choice=input("Menu:\n----\n1.Printing 100 numbers\n2.Check fibonacci\n3.randint numbers untill we get 12 or the "
                 "count is of 10 times\n")

    if (choice=="1"):
        for i in range(1,101):
            print(i)

    elif (choice=="2"):
        #fibonacci = [1, 2, 3, 5, 8, 13, 21]
        fibonacci=[]
        for i in range(7):
            fibonacci.append(int(input("Enter a number: ")))
        boolean = "True"
        for i in range(2, len(fibonacci)):
            print(fibonacci[i])
            print(fibonacci[i - 1])
            print(fibonacci[i - 2])
            print("\n")
            if fibonacci[i] != (fibonacci[i-1] + fibonacci[i-2]):
                boolean = "False"
                break
        if boolean == "True":
            print("It is fibonacci series")
        else:
            print("It isn't fibonacci series")

    elif (choice=="3"):
        counter=1
        num=randint(1,12)
        while (num!=12 and counter<11):
            print("counter:" + str(counter) + "  num:" + str(num) + "\n")
            counter=counter+1
            num=randint(1,12)

    else:
        print("Enter 1-3 only!\n")
        continue

    exit=input("\nDo you want to exit? yes/no\n")
    if(exit=="yes"):
        print( "\nAlwase a pleasure, Bye Bye...\n" )
        break
