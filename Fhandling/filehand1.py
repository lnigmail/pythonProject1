# filename = "C:/Users/ASUS/PycharmProjects/hello.txt"
# file = open(filename, "r")
# print(file.read())
# file.close()
##hello idan

# filename="C:/Users/ASUS/PycharmProjects/hello.txt"
# file=open(filename,"w")
# file.write("192.168.1.1\n192.168.1.2\n")
# file.close()
# filename = "C:/Users/ASUS/PycharmProjects/hello.txt"
# file = open(filename, "r")
# print(file.read())
# file.close()
##192.168.1.1
##192.168.1.2


# filename="C:/Users/ASUS/PycharmProjects/hello.txt"
# file=open(filename,"r+")
# print(file.read())
# file.write("192.168.1.1\n192.168.1.2\n")
# print(file.read())
# file.close()
##192.168.1.1
##192.168.1.2
#
filename="C:/Users/ASUS/PycharmProjects/hello.txt"
file=open(filename,"a+")
print(file.read())
file.write("192.168.1.3\n192.168.1.4\n")
print(file.read())
file.close()

filename = "C:/Users/ASUS/PycharmProjects/hello.txt"
file = open(filename, "r")
print(file.read())
file.close()
## 192.168.1.1
## 192.168.1.2
## 192.168.1.3
## 192.168.1.4
