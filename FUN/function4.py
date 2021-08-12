def add_ip(list,ip1,ip2,ip3):
    list=[]
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list

ip_list=[]
ip_n1=input("Enter first ip: ")
ip_n2=input("Enter 2nd ip: ")
ip_n3=input("Enter 3rd ip: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
# ip_list=ip_list+add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)

# Enter first ip: 1.1.1.1
# Enter 2nd ip: 2.2.2.2
# Enter 3rd ip: 3.3.3.3
# ['1.1.1.1', '2.2.2.2', '3.3.3.3']

ip_list=[]
ip_n1=input("Enter first ip: ")
ip_n2=input("Enter 2nd ip: ")
ip_n3=input("Enter 3rd ip: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
ip_list=ip_list+add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)

# Enter first ip: 1.1.1.1
# Enter 2nd ip: 2.2.2.2
# Enter 3rd ip: 3.3.3.3
# [this previous line is run over]
# ['1.1.1.1', '2.2.2.2', '3.3.3.3', '1.1.1.1', '2.2.2.2', '3.3.3.3']
