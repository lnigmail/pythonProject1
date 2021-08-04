fruits=["apple", "banana", "cherry"]
for x in fruits:
    print (x)
    for x in "banana":
        print(x)
fruits=["app", "ban", "chair"]
for x in fruits:
    print(x)
    if x == "ban":
        break
for x in range (10):
    print(x)
for x in range (5, 10):
    print(x)
fruits=["apple", "banana"]
for x in fruits:
    print(x)
    if x == "banana":
        continue
for x in range (2, 30, 3):
    print(x)

'''
apple
b
a
n
a
n
a
banana
b
a
n
a
n
a
cherry
b
a
n
a
n
a
app
ban
0
1
2
3
4
5
6
7
8
9
5
6
7
8
9
apple
banana
2
5
8
11
14
17
20
23
26
29
'''