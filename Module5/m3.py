'''
3) One common problem when prompting for numerical input occurs when people provide text instead of numbers.
 When you try to convert the input to an int, you'll get a ValueError. Write a program that prompts 
for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, 
and print a friendly error message. Test your program by entering two numbers and then by entering some text 
instead of a number.
 '''
number1=input('first number: ')
number2=input('second number: ')
if number1.isdigit() and number2.isdigit():
    print("Sum is : ", int(number1)+int(number2))
else:
    print('Enter digits only! ')