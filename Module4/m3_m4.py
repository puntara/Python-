'''
Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland.
 Give the parameter for the country a default value. Call your function for three different
  cities, at least one of which is not in the default country.
'''
def describe_city(name, country='United States'):
    print(name+" is in "+country)

describe_city('Baltimore')
describe_city('Atlanta')
describe_city('Kathmandu', 'Nepal')

'''
Make a list containing a series of short text messages. Pass the list to a function called 
show_messages(), which prints each text message.
'''
def show_messages(myList):
    for i in myList:
        print(i)

messages=['Hi','Hello','How are you!']

show_messages(messages)