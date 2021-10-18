# ELIMINATE REPEATED TERMS IN A LIST

# 1 
def eliminate(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
            return b

a = [1,2,42,45,54,54,1,2,3,4]
print(eliminate(a))


# 2nd way 

a = [1,2,42,45,54,54,1,2,3,4]
b = list(set(a))
print(b)


# 3rd way

a = [1,2,42,45,54,54,1,2,3,4]
b = []
for i in a:
    if a.count(i) > 1:
        if i not in b:
            b.append(i)
print(b)


# REVERSE A STRING IN 2 WAYS

# 1 

a = "this is a test"
print(a[::-1])

#2

a = "this is a test"
b = ''.join(reversed(a))
print(b)



# find 1st , 2nd and 3rd biggest element in a list

a = [1,21,4,42,42,42,23,1,41,566]
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


# smallest and largest number

a = [1,21,4,42,42,42,23,1,41,566]
count = a[0]
count2 = 0
for i in a:
    if i < count:
       count = i
    elif i > count:
       count2 = i
print(count)
print(count2)


# find position of a element in a list

a = [1,2,4,24,1,54,53,2,12]
max1 = a.index(max(a))
min1 = a.index(min(a))
print("the max is ",max1+1)

# without in-build function

a = [1,21,4,42,42,42,23,1,41,566]
count = a[0]
for i in range(1,len(a)):
    if a[i] > count:
        count = i
print(count+1)



# CHECK OCCURANCES OF GIVEN ELEMENT IN A LIST

# 1 way

a = "python"
b = list(set(a))
count = 0
for i in b:
    print(i,a.count(i))


# 2nd way

def add(a,c):
    res = 0
    for i in range(len(a)):
        if a[i] == c:
            res = res+1
    return res
    
C = input("enter a word to check occurances ")
A = "this is a test "
print(add(A,C))


# FIND AND REPLACE 

st = list('this is a test sentence')
res = []
for i in st:
    if i == 't':
        i = 'j'
    res.append(i)
print(''.join(res))



# FACTORIAL OF A NUMBER 

a = int(input("enter a number"))
sum = 1
for i in range(1,a+1):
    sum = sum*i
print(sum)



# FACTORIAL RANGE BASE

a = int(input("enter a number "))
x , y = 0,1
for i in range(a):
    x , y = y , x+y
    print(y)



# ARMSTRONG NUMBER 

a = input("enter a number : ")
sum = 0
for i in range(len(a)):
    sum += int(a[i]) ** len(a)

if int(a) == sum:
    print("{} is a armsting".format(a))
else:
    print("{} is not a armstrong".format(a))





# EVEN NUMBER AT EVEN INDEX AND ODD AT ODD INDEX

x = [3, 2, 5, 6, 4, 7, 8, 9, 10, 11]
even_pos = []
odd_pos = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        even_pos.append(i)
    else:
        odd_pos.append(i)

print(even_pos)
print(odd_pos)


even_pos_with_odd = []
odd_pos_with_even = []

for j in range(len(even_pos)):
    if even_pos[j] % 2 != 0:
        even_pos_with_odd.append(j)
    if odd_pos[j] % 2 == 0:
        odd_pos_with_even.append(j)


print(even_pos_with_odd)
print(odd_pos_with_even)

for n in range(len(even_pos_with_odd)):
    temp =  x[odd_pos[odd_pos_with_even[n]]]
    x[odd_pos[odd_pos_with_even[n]]] = x[even_pos[even_pos_with_odd[n]]]
    x[even_pos[even_pos_with_odd[n]]] = temp

print(x)




# join list
test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1, 3], [9, 3, 5, 7], [8]]

c = [ i + j for i , j in zip(test_list1,test_list2)]
print(c)