
d={}
d={'name':'david','choice':(2,3,4)}         #1
d=dict({'name':'david','choice':(2,3,4)})   #2
d=dict([('name','david'),('choice',(2,3,4))]) #3


d['name']='John'
d.pop("choice")
print(d)
print(d.values())

set1={110, 20, 12}
print(set1)

d3 = {'f': 6, 'g': 11, 'a': 10, 'b': 8, 'd': 6, 'e': 11}

str1="I am From Nepal"
print(str1[2])
str2=str1.replace('Nepal','USA')

print(str1)
x=10
print(hex(id(x)))
x=20
print(hex(id(x)))
#print(str1[0].alphanumeric())


a="abc"
d="ne"
a+=d
print(a)