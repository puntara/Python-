sq=[]
for i in range (1,11):
    if i%2==0:
        sq.append(i*i)
print(sq)

s=[i*i for i in range(1,11) if i%2==0]
print(s)




#-------------------------------------------------
l=[]
for c in 'city u 1':
    if c.islower()==True:
        l.append(c)
print(l)
letters=[c for c in 'Tara 1' if c.isdigit()==True]
print(letters)

#-----------------------------------------------------------

import random
for x in range(9):
    print(random.randint(0,8))

#------------------------------
while(True):
    try:
        x=int(input('Enter: '))
        #break
    except ValueError:
        print("wrong")