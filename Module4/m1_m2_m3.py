def make_shirt(size='Large', message='I Love Python'):
#summarizing the size of the shirt and the message printed on it

    print('Size of the Shirt: '+ size)
    print('Message! :'+ message)
#Call the function once using positional arguments to make a shirt. 
make_shirt('Medium', 'I Love Python')
#Call the function a second time using keyword arguments.
s='Small'
m='I Love Python'
make_shirt(s,m)

# default
make_shirt()
make_shirt(size='Medium')
make_shirt('Small','I like Pizza')