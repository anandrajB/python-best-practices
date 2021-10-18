# ELIMINATE REPEATED TERMS IN LIST

def removes(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

A = [1,1,2,2,3,4,2,32,2]
print(removes(A))


# REVERSE A STING IN 2 WAYS

a = "python"
print(a[::-1])

# 2nd way

a = "python"
b = ''.join(reversed(a))
print(b)


# FIND LARGEST NUMBER IN A LIST

a = [1,3,213,4,4,534,2,32]
count = a[0]
for i in a:
    if i > count:
        count = i
print(count)


# SECOND LARGEST NUMBER IN A LIST

a = [1,3,213,4,4,534,2,32]
count = a[0]
count2 = 0
for i in a:
    if i > count:
        count2 = count
        count = i
    elif count2 > count < i :
        count2 = i
print(count)
print(count2)


# find pos of min and max numbers in a list

a = [1,3,213,4,4,534,2,32]
max1 = a.index(max(a))
min2 = a.index(min(a))
print("the max number is",max1+1)
print("the min num is ",min2+1)



# ADD 2 NUMBERS WITHOUT USING OPERATOR

def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(add_without_plus_operator(2, 10))



# COUNT NO OF OCCURANECE IN STRING

a = "hey this is admin from chennai"
b = set(list(a))
for i in b:
    print(i,a.count(i))


# COUNT THE OCCURANCES IN THE STRING 

a = "hey this is admin from chennai"
c = input("enter a input : ")
res = 0
for i in range(len(a)):
    if a[i] == c:
        res = res+1
print(res)