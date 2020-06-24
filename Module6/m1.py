'''
) Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a
 restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces 
 of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
 '''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurent_name=restaurant_name.title()
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        message= self.restaurent_name + ' has '+ self.cuisine_type
        print('\n'+message)


    def open_restaurant(self):
        message=self.restaurent_name + ' is open now!'
        print('\n'+message)

myRest=Restaurant('Great Cuisine of India', 'Fish Curry')
print(myRest.restaurent_name)
print(myRest.cuisine_type)

myRest.describe_restaurant()
myRest.open_restaurant()

'''
2) Update the above program by creating three different instances from the class, and call 
describe_restaurant() for each instance.
'''
myRest_2=Restaurant('McDonald', 'Burger')
myRest_2.describe_restaurant()
myRest_2.open_restaurant()

myRest_3=Restaurant('Lancer Dining Facility', 'Yakisoba')
myRest_3.describe_restaurant()
myRest_3.open_restaurant()
