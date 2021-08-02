'''Create a Dictionary with 5 names & money
then sum the money of the first & last names and print it to the screen
after, add a new name with the sum of the money you calculated before
in the end, print the number of the entries and check if "idan" is inside
'''

dict_names={"idan":10000, "ben":20000, "avi":30000, "shimon":40000, "ayala":50000}
print("Dictionary of 5 names & money: " + str(dict_names))

summery=(dict_names["idan"]+dict_names["ayala"])
print("\nThe sum of 1st & last is: " + str(summery))

dict_names.update({"idanayala":summery})
print("The updated Dictionary: " + str(dict_names))
print("The updated number of entries: " + str(len(dict_names)))

print("\nIs idan in the Dictionary?:")
print("idan" in str(dict_names))





