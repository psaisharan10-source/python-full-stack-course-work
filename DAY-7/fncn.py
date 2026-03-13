'''
function
'''
'''
def wish(name):
    print(f'Hello {name} , Welcome to "python 100 days of program"')

wish('sai')
wish('venu')
wish('teja')
wish('sharan')
wish('rahul')  

'''

'''
def display(username,email,password):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)

display('sharan','sharan@gmail.com','sai@123')
display('rahul','rahul@gmail.com','rahul@123')
display('palash','palash@gmail.com','palash@123')

'''
'''

def display(username,email,password):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)

display(username='sharan',email='sharan@gmail.com',password='sai@123')
display(email='rahul@gmail.com',username='rahul',password='rahul@123')
display(password='palash@123',email='palash@gmail.com',username='palash')


'''
'''

def display(username,email,password,phoneno='+91'):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)
    print("Phone no:",phoneno)



display('sharan','sharan@gmail.com','sai@123','7989716494')
display('rahul','rahul@gmail.com','rahul@123','9876543210')
display('palash','palash@gmail.com','palash@123','5287496310')


'''

'''

def display(*names):
    print(names)

display('sai','venu','teja')
display('sai','venu')
display('sai')

'''

def display(**names):
    print(names)

display(n1='sai',n2='venu',n3='teja')
display(n1='sai',n2='venu')
display(n1='sai')

































