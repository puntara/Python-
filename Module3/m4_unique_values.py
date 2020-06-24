#Write a Python program to print all unique values in a dictionary. 

#Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
my_list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
{"V":"S009"},{"VIII":"S007"}]
#print(list(my_dict.values()))

y=set()
for dictionary in my_list:
    for value in set(dictionary.values()):
        if value not in y:
            y.add(value)

print(y)