'''
write a code that will show the Menu:
Menu:
1.Insert number and ** it by 3
2.Insert 4 IPs to a list and print it
3.Insert 4 entries to a DNS_Dictionary and print it
4.Check if a string is Palindrome

if the user wont choose 1-4, you will tell him to Insert 1-4 only!
'''

from time import sleep

choice=input("Menu:\n----\n1.Insert number and ** it by 3\n2.Insert 4 IPs to print\n3.Insert 4 entries to a "
             "DNS_Dictionary\n4.Check if a string is Palindrome\n")
if(choice=="1"):
    print("The new number is: " + str((int(input("\nEnter a number: ")))**3))
elif (choice=="2"):
     list_ip=[]
     list_ip.append(input("Enter new IP: "))
     list_ip.append(input("Enter new IP: "))
     list_ip.append(input("Enter new IP: "))
     list_ip.append(input("Enter new IP: "))
     print("\nThe new list:\n--------------------------------------------\n" + str(list_ip))
elif (choice=="3"):
    dns_dict={}
    dns_dict.update({input("Enter a URL: "):input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "):input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "):input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "):input("Enter IP: ")})
    print("\nThe new dns_dict:\n------------------\n" + str(dns_dict))
elif (choice=="4"):
    word=input("Enter a word: ")
    if (word == word[::-1]):
        print("This is polindrom!")
    else:
        print("This isn't polindrom!")
else:
    print("\n\nInsert 1-4 only!...\n")

print("It was Enlightening, bye bye...\n")

'''
Menu:
----
1.Insert number and ** it by 3
2.Insert 4 IPs to print
3.Insert 4 entries to a DNS_Dictionary
4.Check if a string is Palindrome
1

Enter a number: 3
The new number is: 27
It was Enlightening, bye bye...

2
Enter new IP: 1.1.1.1
Enter new IP: 2.2.2.2
Enter new IP: 3.3.3.3
Enter new IP: 4.4.4.4

The new list:
--------------------------------------------
['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']
It was Enlightening, bye bye...

3
Enter a URL: www.google.com
Enter IP: 8.8.8.8
Enter a URL: www.youtube.com
Enter IP: 4.4.4.4
Enter a URL: www.facebook.com
Enter IP: 7.7.7.7
Enter a URL: www.ynet.co.il
Enter IP: 9.9.9.9

The new dns_dict:
--------------
{'www.google.com': '8.8.8.8', 'www.youtube.com': '4.4.4.4', 'www.facebook.com': '7.7.7.7', 'www.ynet.co.il': '9.9.9.9'}
It was Enlightening, bye bye...

4
Enter a word: anna
This is polindrom!
It was Enlightening, bye bye...
4
Enter a word: ainshtein
This isn't polindrom!
It was Enlightening, bye bye...
'''