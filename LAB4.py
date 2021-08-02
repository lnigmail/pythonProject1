'''
create a list with 4 details about you: name, age, mail, phone and print it to the screen
then create another list with 2IPs, then add 3 more IPs, pop the 3rd IP and print how many
IPs do we have and print them.
'''

details_list= ["Ainshtain Ainshtain", 47, "il@gmail.com", "0500000000"]
print("My name is: " + str(details_list[0]) + "\nMy Age is: " + str(details_list[1]) +
"\nMy mail is: " + str(details_list[2]) + "\nMy phone is: " + str(details_list[3]))

IP_list=["1.1.1.1", "2.2.2.2"]
print("\nThis is IPs list: " + str(IP_list))

IP_list.append("3.3.3.3")
IP_list.append("4.4.4.4")
IP_list.append("5.5.5.5")
print("\nThis is 3 more IPs: " + str(IP_list))

IP_list.pop(2)
print("\nThis is IPs list without the 3rd IP: " + str(IP_list))
print("IP list lengh is: " + str(len(IP_list)))


