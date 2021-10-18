# simple try and excepet

a = 2
try:
    print(a/2)
except:
    print("sorry we can't")


# example

try:
    x = int(input("enter a number 1"))
    y = int(input("enter a number 2"))
    result = x+y

except:
    print("no values")

print("the values is",result)