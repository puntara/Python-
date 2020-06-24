#1) Write a Python script to concatenate following dictionaries to create a new one. 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

result1={**dic1, **dic2, **dic3}
print(result1)

#2) Write a Python script to generate and print a dictionary that contains a number 
# (between 1 and n) in the form (x, x*x). 

number =int(input('enter a number: '))
my_dict =dict()

for val in range(1,number+1):
    my_dict[val]=val*val
print(my_dict)

