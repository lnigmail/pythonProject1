###While loops

#While = if + for

'''num=int(input("Enter a number: "))
while(num!=7):
    print(num*100)
    #the above is an endless loop from one stroke, therefore it needs something more:
    num=int(input("Enter a number: "))
    #the above loop will end only when the number is 7

counter=10
while(counter>0):
    print("ainshtein")
    #the above is endless since the counter will alwase be more then 0
    #should have done counter=counter-1 (next rounds the counter will be 9,8,7,6,5,4,3,2,1,0)
    counter=counter-1'''

while (True):
    name=input("Enter a name: ")
    if (name=="idan"):
        print("Hello idan")
        break
    elif (name=="ben"):
        continue
    else:
        print("Where is idan?")
    number=int(input("Enter a number: "))
    print(number*4)
print("Bye Bye..")

