'''
Menu:
----
1.Printing 100 numbers
2.Check fibonachi
3.randint numbers untill we get 12 or the count is of 10 times
'''
from random import randint
from time import sleep

while(True):

    choice=input("Menu:\n----\n1.Printing 100 numbers\n2.Check fibonacci\n3.randint numbers untill we get 12 or the "
                 "count is of 10 times\n")

    if (choice=="1"):
        for i in range(1,101):
            print(i)

    elif (choice=="2"):
        #fibonacci = [1, 2, 3, 5, 8, 13, 21]
        fibonacci=[]
        for i in range(7):
            fibonacci.append(int(input("Enter a number: ")))
        boolean = "True"
        for i in range(2, len(fibonacci)):
            print(fibonacci[i])
            print(fibonacci[i - 1])
            print(fibonacci[i - 2])
            print("\n")
            if fibonacci[i] != (fibonacci[i-1] + fibonacci[i-2]):
                boolean = "False"
                break
        if boolean == "True":
            print("It is fibonacci series")
        else:
            print("It isn't fibonacci series")

    elif (choice=="3"):
        counter=1
        num=randint(1,12)
        while (num!=12 and counter<11):
            print("counter:" + str(counter) + "  num:" + str(num) + "\n")
            counter=counter+1
            num=randint(1,12)

    else:
        print("Enter 1-3 only!\n")
        continue

    exit=input("\nDo you want to exit? yes/no\n")
    if(exit=="yes"):
        print( "\nAlwase a pleasure, Bye Bye...\n" )
        break

'''
1
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100

Do you want to exit? yes/no
n
Menu:
----
1.Printing 100 numbers
2.Check fibonacci
3.randint numbers untill we get 12 or the count is of 10 times
2
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 5
Enter a number: 8
Enter a number: 13
Enter a number: 21
3
2
1


5
3
2


8
5
3


13
8
5


21
13
8


It is fibonacci series

Do you want to exit? yes/no
n
Menu:
----
1.Printing 100 numbers
2.Check fibonacci
3.randint numbers untill we get 12 or the count is of 10 times
3
counter:1  num:2

counter:2  num:9

counter:3  num:7

counter:4  num:8

counter:5  num:2

counter:6  num:8

counter:7  num:2

counter:8  num:7

counter:9  num:7

Do you want to exit? yes/no
yes

Alwase a pleasure, Bye Bye...
'''