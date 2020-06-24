
'''def function1():
    function2(name)


def function2(name):
    for n in name:
        print(f"Good afternoon {n}")


name=["Tara", "aj", "david"]

function1()

def addnum(myl):
    s=0
    for i in myl:
        s=s+i
    return(s)

L=[1,2,10]
s=addnum(L)
print(s)

#Local and Global variable
x=10
y=20
#----------------------------------------
def addnum(a,b):
    global x
    x=5
    print(x,id(x))  #can access global variable inside local function addnum
   
    s=a+b
    return (s)
#-----------------------------------------
print(x,id(x))
total=addnum(x,y)
print(x,id(x))


x=10
y=20
#----------------------------------------
def addnum(a,b):
    print(x,id(x))  #can access global variable inside local function addnum
    s=a+b
    
    #-----------------------------
    def subnum(c,d):
        x=5
        print(x,id(x))  #can access global variable inside local function addnum
        e=c-d
        return (e)
    #----------------------------
    return (s)
#-----------------------------------------

print(x,id(x))
total=subnum(x,y)

print(x,id(x))

def f1():
    x=10
    def f2():
        nonlocal x
        x=x+1
        return x
    f2()
    return x
print(f1())


# complex function
complex(real=3, imag =8)
x=[1,5] ## List same with list tuple set
a=complex(*x) ## give 1+5j 
print(a)

#dictionary 
d={1:5}
c=complex(*d) ## two stars for dict
print(c)
'''
def f():
    m="1"
    def f2():
        print(m)
    return(f2())

