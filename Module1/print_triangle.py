i=5
for val in range(i):
    print(' '*(i-val-1),end="")
    for j in range(val+1):
        print("* ",end="")
    print()