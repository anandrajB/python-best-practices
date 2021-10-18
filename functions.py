# UNDERSTANDING FUNCTION IN PYTHON 

# GENERAL SYNTAX
def func_name(object):
    print("hello world")



# SIMPLE EXAMPLE

def add(x,y):
    return x+y

A = int(input("enter a number : "))
B = int(input("enter a number : "))

print(add(A,B))   # accessing the function --> add ( passing arguments )


# * IN FUNCTION { VARIABLE LENGTH ARGUMENT }

def getemployee(*names):
    print(names)

getemployee("anand","arjun","aravind")



# A FUNCTION SHOULD RETURN A VALUE 

def func_name(object):
    return object  
x = 5
print(func_name(x))

# if there is no return is displays None in terminal 


# SUPPOSE IF WE HAVE 2 RETURNS IN A FUCNTION


def func_name(object):
    return 13
    return 14

print(func_name(x))


# return is a control statement so the first return is only displayed 

# for instance 

x =5
x = 6
print(x)

# in this code , the lastest value for x will be taken 