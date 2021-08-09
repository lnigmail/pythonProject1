'''11. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'''

lista="abc"
listb="xyz"

list= (listb[:2] + lista[2]),(lista[:2] + listb[2])
print(list)
# xyc abz
my_string: str =' '.join(list)
print(my_string)
