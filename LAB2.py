#input of the following & calculation of cost (ils):
print("pricelisting:\n-----------\ntomatoes=3 NIS\ncucumbers=2 NIS\ncolas=5 NIS\nchickens=20 NIS\n")

tomatoes=int(input("Enter how many tomatoes?"))
cucumbers=int(input("Enter how many cucumbers?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))

"""
print("\nSummary of your order:\n-----------\ntomatoes: " + str(tomatoes) + "\ncucumbers: " + str(cucumbers) + 
"\ncolas: " + str(colas) + "\nchickens: " + str(chickens))
"""

summary=(tomatoes*3)+(cucumbers*2)+(colas*5)+(chickens*20)
print("\nYou have to pay: " + str(summary) + " NIS without tax")
print("\nYou have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with tax")


sum1=tomatoes*3
sum2=cucumbers*2
sum3=colas*5
sum4=chickens*20