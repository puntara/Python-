#3) Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d1:
    if key in d2:
        d1[key]=d1[key]+d2[key]
    for key2 in d2:
        if key2 not in d1:
            d1={**d1, **d2}
print(d1)
