# MAP FUNCTION 

# syntax  map(function , iteratable )

def add(n):
    return n+n

numbers = (1,2,3,4)
y = map(add , numbers)   # -> map funtion
print(y)


# LAMBDA IN PYTHON

# syntax 

lambda x,y : x+y

# function (variables) : operation 


numbers = (1,2,3,4)
y = map(lambda x:x+x,numbers)

# map ( function , iterators )
print(list(y))



# example 2


numbers = (1,2,3,4)
numbers2 = (1,2,3,4)
y = map(lambda x,y:x+y,numbers,numbers2)

# map ( function , iterators )
print(list(y))


# map reduce

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
y = filter(lambda s:s[0] == 'A',fruit)
print(list(y))

# this return the list values as apple and apricot


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
y = map(lambda s:s[0] == 'A',fruit)
print(list(y))


# in this code , it returns bool value for the output