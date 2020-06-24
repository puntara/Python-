'''
Write a Python program that takes a text file as input and returns the number of words of a given text file
'''
file=open('C:\CS160\python-160\\textfile.txt')
data=file.read()
words=data.split()
print(len(words))
'''
2) Write a while loop that prompts users for their name. When they enter their name, print a greeting to the 
screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on 
a new line in the file.
'''
RecordBook='C:\CS160\python-160\\record.txt'
print('Enter 1 to exit')
while True:
    name=input('\n Your name: ')
    if(name=='1'):
        break
    else:
        with open(RecordBook,'a') as f:
            f.write(name +'\n')
        print(name, ' is added to the record.')