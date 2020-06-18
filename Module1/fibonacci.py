n=int(input("What position of Fibonacci number you want to see? "))
if n<=2:
    print(n)
Pos01=0
Pos02=1
Pos03=1
position=3
while(Pos03<n):
    Pos03=Pos01+Pos02

    position =position +1
    Pos01=Pos02
    Pos02=Pos03

print(position)