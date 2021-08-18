from time import sleep


def menu():
    while True:
        choice1 = input("Menu:\n----\na. IP System\nb. DNS System\n")
        if choice1 == "a":
            choice2 = input("\nMenu IP System:\n--------------\n1.search for IP address from a list\n2.add IP address "
                             "to a list\n3.Delete IP address from a list\n4.Print all the IPs to the screen\n")
            if choice2 == "1":
                search_ip()

            elif choice2 == "2":
                add_ip()

            elif choice2 == "3":
                delete_ip()

            elif choice2 == "4":
                print_ips()

        elif choice1 == "b":
            choice3 = input("\nMenu DNS System:\n--------------\n1.search for URL from a dictionary\n2.add URL+IP "
                             "address to a dictionary\n3.Delete URl from a dictionary\n4.Update the IP address of "
                             "specific URL\n5.Print all the URL:IP to the screen\n")
            if choice3 == "1":
                search_url()

            elif choice3 == "2":
                add_url_ip()

            elif choice3 == "3":
                delete_url()

            elif choice3 == "4":
                update_ip_dict()

            elif choice3 == "5":
                print_dict()

        else:
            print("Enter a or b only!\n")
            continue
        exit = input("\nDo you want to exit? yes/no ")
        if (exit == "yes"):
            print("Bye, Bye...")
            break
        else:
            print("Welcome back!\n")


def search_ip():
    filename = "C:/Users/ASUS/PycharmProjects/hello2.txt"
    file = open(filename, "r")
    new_list = []
    new_list = file.read().splitlines()
    print(type(new_list))
    print(new_list)
    file.close()
    ip = input("Enter ip to serch: \n")
    sleep(1)
    print("...")
    sleep(1)
    print("......")
    sleep(1)
    print(".........")
    sleep(1)
    print("...............")
    sleep(1)
    filename = "C:/Users/ASUS/PycharmProjects/hello2.txt"
    file = open(filename, "r")
    for i in new_list:
        if i == ip:
            print("The ip is on the list!!!\n")
            break
        else:
            print("The ip isn't on the list!\n")




def add_ip():
    filename = "C:/Users/ASUS/PycharmProjects/hello2.txt"
    file = open(filename, "r")
    p = input("\nEnter IP: \n")
    print(file.read())
    file.close()
    filename = "C:/Users/ASUS/PycharmProjects/hello2.txt"
    file = open(filename, "a+")
    file.write("\n{0}".format(p))
    file.close()




def delete_ip():
    filename = "C:/Users/ASUS/PycharmProjects/hello2.txt"
    file = open(filename, "r")
    lines = file.readlines()
    content = input("Enter IP to delete: ")
    print(file.read())
    file.close()
    filename = "C:/Users/ASUS/PycharmProjects/hello2.txt"
    file = open(filename, "w")
    for line in lines:
        if line.strip("\n") != content:
            file.write(line)
    file.close()




def print_ips():
    filename = open("C:/Users/ASUS/PycharmProjects/hello2.txt", "r")
    while filename:
        line = filename.readline()
        print(line)
        if line == "":
            break
    filename.close()




def search_url():
    dns_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "12.12.12.12"}
    u = input("\nEnter a URL to search from dictionary: ")
    if u in dns_dict:
        print(u + " is already in the dict!\n")
    else:
        print(u + " isn't inside the dict!\n")




def add_url_ip():
    dns_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "12.12.12.12"}
    dns_dict.update({input("Enter a URL to add: "): input("Enter IP to add: ")})
    print("\nThe new dns_dict:\n------------------\n" + str(dns_dict))




def delete_url():
    dns_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "12.12.12.12"}
    url = input("Enter a URL to delete from dns_dict: ")
    if url in dns_dict:
        dns_dict.pop(url)
        print(dns_dict)
    else:
        print(url + " isn't inside the dict!\n")




def update_ip_dict():
    dns_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "12.12.12.12"}
    key = input("\nEnter a specific URL to update the IP address: ")
    value = input("Enter a apecific address to update the URL: ")
    dns_dict[key] = value
    print(dns_dict[key])




def print_dict():
    dns_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "12.12.12.12"}
    print("\nThe new dns_dict:\n------------------\n" + str(dns_dict))


