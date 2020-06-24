'''
Write a Python function that accepts a string and calculate the number 
of upper case letters and lower case letters. 
'''
def calculate_case(myString):
    upper=0
    lower=0
    for c in myString:
        if c.islower():
            lower=lower+1
        elif c.isupper():
            upper=upper+1
    print('No. of Upper case characters: ', upper)
    print('No. of Lower case characters: ', lower)

str1='The Quick Brown Fox'
calculate_case(str1)