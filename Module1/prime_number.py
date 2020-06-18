num=int(input("Input: "))
if num > 0:
    for value in range(2, num):
        if(num%value==0):
            print(str(num) +" is not a prime number")
            break
    else:
        print(str(num)+ " is a prime number")