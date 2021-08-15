filename="C:/Users/ASUS/PycharmProjects/hello.txt"
file=open(filename, "r")
new_list=[]
new_list=file.read().splitlines()
print(type(new_list))
print(new_list)
file.close()
##<class 'list'>
##['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']

for i in new_list:
    print(i)
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4

filename="C:/Users/ASUS/PycharmProjects/hello.txt"
file=open(filename, "r")
print(file.read(8))
file.close()
# 192.168.

filename="C:/Users/ASUS/PycharmProjects/hello.txt"
file=open(filename, "r")
print(file.readlines()[2])
file.close()
#192.168.1.3

filename = open("C:/Users/ASUS/PycharmProjects/hello.txt", "r")
while filename:
    line=filename.readline()
    print(line)
    if line=="":
        break
filename.close()
# 192.168.1.1
#
# 192.168.1.2
#
# 192.168.1.3
#
# 192.168.1.4