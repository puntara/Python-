'''
4) Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names 
of dogs in the second file. Write a program that tries to read these files and print the contents of the file
 to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly 
 message if a file is missing.
 '''
record_files=['C:\CS160\python-160\Module5\\cats.txt', 'C:\CS160\python-160\Module5\\dogs.txt']

for animals in record_files:
    print('Contents of files: ', animals)
    try:
        with open(animals) as f:
            list_values=f.read()
            print(list_values)
    except FileNotFoundError:
        print('No such file in the database.')
