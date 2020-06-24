'''
grid_x=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def board(grid_x):
    print('%c | %c | %c ' % (grid_x[0],grid_x[1],grid_x[2]))
    print('%c | %c | %c ' % (grid_x[3],grid_x[4],grid_x[5]))
    print('%c | %c | %c ' % (grid_x[6],grid_x[7],grid_x[8]))

board(grid_x)



s=['Appe', 'ball', 'Cat']
print(sorted(s, key=lambda x: x.lower()))
'''
import datetime

x=datetime.datetime.now()
print(int(x.hour))

x = 50 

def func(): 

    global x 

    print('x is', x) 

    x = 2 

    print('Changed global x to', x) 

func() 

print('Value of x is', x) 
f = None  

for i in range (5):  

   with open("data.txt", "w") as f:  

        if i > 2:  

            break  

print(f.closed) 
class Dog: 

    def walk(self): 

        return "*walking*" 

    def speak(self): 

        return "Woof!" 

 

class JackRussellTerrier(Dog): 

    def speak(self): 

        return "Arff!" 

bobo = JackRussellTerrier() 

print(bobo.walk()) 