
my_list=[('452', 10), ('256', 5), ('100', 20), ('135', 15)]
length=len(my_list)
for i in range(0,length):
    for j in range(0,length-i-1):
        if(my_list[j][1] > my_list[j+1][1]):
            bucket=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=bucket
print(my_list)