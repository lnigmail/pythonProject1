while (True):
    choice=input("Menu:\n----\n1.Insert number to ** it by 3\n2.Insert 4 IPs to print\n3.Insert 4 entries for a "
                 "DNS_Dictionary\n4.Check if a string is Palindromic\n")
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
            print("This is Palindromic!")
        else:
            print("This isn't Palindromic!")
    else:
        print("Insert 1-4 only!...\n")

    exit=input("Do you want to exit? y/n\n")
    if (exit=="y" or exit=="yes"):
        break
    else:
        print("Welcome back:\n")


print("\nIt was Enlightening, bye bye...\n")

