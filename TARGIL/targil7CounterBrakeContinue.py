###While loops

#While = if + for

'''num=int(input("Enter a number: "))
while(num!=7):
    print(num*100)
    #the above is an endless loop from one stroke, therefore it needs something more:
    num=int(input("Enter a number: "))
    #the above loop will end only when the number is 7
'''
counter=10
while(counter>0):
    print("ainshtein" + str(counter))

    #the above is endless since the counter will alwase be more then 0
    #should have done counter=counter-1 (next rounds the counter will be 9,8,7,6,5,4,3,2,1,0)
    counter = counter - 1
    # ainshtein10
    # ainshtein9
    # ainshtein8
    # ainshtein7
    # ainshtein6
    # ainshtein5
    # ainshtein4
    # ainshtein3
    # ainshtein2
    # ainshtein1

###counter with randint else then 12 & until 10 rounds
from random import randint
counter=1
num=randint(1,12)
while (num!=12 and counter<11):
    print("counter:" + str(counter) + "  num:" + str(num) + "\n")
    counter=counter+1
    num=randint(1,12)
    # counter: 1
    # num: 2
    #
    # counter: 2
    # num: 10
    #
    # counter: 3
    # num: 4
    #
    # counter: 4
    # num: 6
    #
    # counter: 5
    # num: 6
    #(counter:6 randint num:12-therefore the counter stop the count before 10)

while True:
    name=input("Enter a name: ")
    if (name=="idan"):
        print("Hello idan")
        break

    else:
        print("Where is idan?")
    number=int(input("Enter a number: "))
    print(number*4)
print("Bye Bye..")

# Enter a name: idan
# Hello idan
# Bye Bye..

# Enter a name: ben
# Where is idan?
# Enter a number: 7
# 28
# Enter a name:
#(continues BY DEFAULT the loop to end & all over again)

while True:
    name=input("Enter a name: ")
    if (name=="idan"):
        print("Hello idan")
        break
    elif (name=="ben"):
        continue
    else:
        print("Where is idan?")
    number=int(input("Enter a number: "))
    print(number*4)
print("Bye Bye..")

# Enter a name: ben
# Enter a name:
#(CONTINUE not by default- is to return to beginning)