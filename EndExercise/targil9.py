'''
 Write a Python program to convert a byte string to a list of integers
'''
filename="C:/Users/ASUS/PycharmProjects/hello.txt"
file=open(filename, "r")
new_list=[]
new_list=file.read().splitlines()
print(type(new_list))
print(new_list)
file.close()
# <class 'list'>
# ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
