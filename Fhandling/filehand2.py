# filename="C:/Users/ASUS/PycharmProjects/hello.txt"
# file=open(filename,"r")
# for line in file:
#     print(line)
# file.close()
# # 192.168.1.1
# #
# # 192.168.1.2
# #
# # 192.168.1.3
# #
# # 192.168.1.4
#
# filename="C:/Users/ASUS/PycharmProjects/hello.txt"
# file=open(filename,"r")
# my_string=file.read()
# file.close()
# print(my_string)
# print(my_string.split(","))
# #['192.168.1.1\n192.168.1.2\n192.168.1.3\n192.168.1.4\n']

filename="C:/Users/ASUS/PycharmProjects/hello.txt"
file=open(filename,"r")
my_string=file.read()
file.close()
my_list=my_string.split(",")
print(type(my_list))
print(my_list)
#<class 'list'>
#['192.168.1.1\n192.168.1.2\n192.168.1.3\n192.168.1.4\n']
