'''


fruits=["apple", "banana", "cherry"]
for x in fruits:
    print (x)
    for x in "banana":
        print(x)
fruits=["app", "ban", "chair"]
for x in fruits:
    print(x)
    if x == "ban":
        break
for x in range (10):
    print(x)
for x in range (5, 10):
    print(x)
fruits=["apple", "banana"]
for x in fruits:
    print(x)
    if x == "banana":
        continue
for x in range (2, 30, 3):
    print(x)'''
# apple
# b
# a
# n
# a
# n
# a
# banana
# b
# a
# n
# a
# n
# a
# cherry
# b
# a
# n
# a
# n
# a
# app
# ban
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 5
# 6
# 7
# 8
# 9
# apple
# banana
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29

'''
#The count begins in range 0 - therefore it ends at 10
for x in range (11):
    print(x)
    print("wow")
    0
    wow
    1
    wow
    2
    wow
    3
    wow
    4
    wow
    5
    wow
    6
    wow
    7
    wow
    8
    wow
    9
    wow
    10
    wow'''
'''
#Determing the conunt from 1 insted from 0
for x in range (1, 11):
    print(x)
    print("wow")'''
    # 1
    # wow
    # 2
    # wow
    # 3
    # wow
    # 4
    # wow
    # 5
    # wow
    # 6
    # wow
    # 7
    # wow
    # 8
    # wow
    # 9
    # wow
    # 10
    # wow
#printing every [,] in range of length(3) of list_idan
'''list_idan=["banana", "apple", "mango"]
for x in range(len(list_idan)):
    print(list_idan[x])'''
    # banana
    # apple
    # mango

#jumps of 2 (אי זוגי)
"""for x in range (1,11,2):
    print (x)
    print ("wow\n")"""
    # 1
    # wow
    #
    # 3
    # wow
    #
    # 5
    # wow
    #
    # 7
    # wow
    #
    # 9
    # wow

#To input 4 names of students and print them
from time import sleep
print("Now we will get all the details about your class: \n------------------------------------------------\n")
for i in range( 4 ):
    name=input("Enter a name: ")
    age=int(input("Enter Age: "))
    phone=input("Enter a Phone number: ")
    print("Printing student number: " + str(i+1) + " Details...\n")
    sleep(3)
    print("Full name: " + name + "\nAge:" + str(age) + "\nPhone: " + phone + "\n-----------------\n")
print("\nBye Bye...")
# Now we will get all the details about your class:
# ------------------------------------------------
#
# Enter a name: ainshtein
# Enter Age: 100
# Enter a Phone number: 10010099100
# Printing student number 1 Details...
#
# Full name: ainshtein
# Age:100
# Phone: 10010099100
# -----------------
# Enter a name: yehudit
# Enter Age: 47
# Enter a Phone number: 1001009910
# Printing student number 2 Details...
#
# Full name: yehudit
# Age:47
# Phone: 1001009910
# -----------------
# Enter a name: yehuda
# Enter Age: 77
# Enter a Phone number: 7707707777
# Printing student number 3 Details...
#
# Full name: yehuda
# Age:77
# Phone: 7707707777
# -----------------
# Enter a name: zion
# Enter Age: 7000
# Enter a Phone number: 7007007777
# Printing student number 4 Details...
#
# Full name: zion
# Age:7000
# Phone: 7007007777
# -----------------
#
# Bye Bye...