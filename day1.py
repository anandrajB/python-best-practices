#simple function to change first and last element in a list

def update(a):
    a[0] , a[-1]  = a[-1] , a[0]
    return a

A = [1,2,3]
print(update(A))


#swapping function in python

def saves(list , pos1 , pos2):
    list[pos1] , list[pos2] = list[pos2] , list[pos1]
    return list

List = [23, 65, 19, 90]
pos1 , pos2 = 1,3
print(saves(List,pos1-1,pos2-1))


#length of a list

def length(a):
    return len(a)

A = [1,23,4,6,1]
print(length(A))


#max of a given number in a list

def max(a,b):
    if a >= b:
        return a
    else:
        return b

A , B = 2,3
print(max(A,B))


#check whether element is present or not

def check(a,b):
    if a in b:
       return "element found"
    else:
        return "element not found"
B = [1,2,3,4,5,6,7]
A = int(input("enter a number : "))
print(check(A,B))


#to clear all elements in a list 

list1 = [1,2,3,4,5,5,56]
list1.clear()
print("the empty list is" ,list1)

list1 *= 0


#reverse a list with method
list2 = [1,23,3,4,5,5,67]
list2.reverse()
print(list2)


#reverse a list without method

def reverse_func(a):
    b = a[::-1]
    return b
list3 = [1,2,3,4,5,6,7]
print(reverse_func(list3))


#cloning or copying a list
a = [1,2,3,4,5,6,7]
a.copy()
b = a
print(b)


#count occurances in a list

def counter(a,X):
    b = a.count(X)
    return b
list1 = [1,2,3,4,5,10,23,10,11,14,54,10]
x = 10
print(counter(list1,x))



#simple leap year program
year = int(input("enter a number :"))
if year%4==0 and year%100==0 or year%400==0:
    print("{} is a leap year".format(year))
else:
    print("it is not a leap year")



#check palindrome
x = input("enter a string")
if x==x[::-1]:
    print("{} is a palindrome".format(x))
else:
    print("{} it is not a palindrome".format(x))


#simple count operation

a = [1,2,3,4,5,6,7,89,9]
count = 0 
for i in a:
    count = count + i
print(count)


#simple program for increase marks in a given list if mark between 40 to 50 --> add 10 

a = [35,45,47,50,55,44,48]
for i in range(len(a)):
    if 40 <= a[i] <50:
        a[i] += 10
print(a)


#duplication delete in a list

a = [1,2,2,3,4,5,5,6,7,8,8]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)


#anagram 

a = input("enter first string : ")
b = input("enter second string : ")
a.sort()
b.sort()
print(a,b)
for i in range(len(a)):
    if a[i] != b[i]:
        print("not a anagram")
        break
    else:
        print("anagram")

#factorail number series

a = int(input("enter a range required  : "))
x , y = 0 , 1
for i in range(a):
    x,y = y , x+y


#simple sort algorithm

a = [1,5,6,7,8,2,3,4,9,10]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i] , a[j] = a[j] , a[i]
print(a)



#anagram
a = list(input("enter a string 1 : "))
b = list(input("enter string 2  :"))
a.sort()
b.sort()
for i in range(len(a)):
    if a[i] != b[i]:
        print("not a anagram")
        break
else:
    print("anagram")


#calc program
def add(x,y):
    return x + y

choices = input("enter a choice : ").lower()
num1 = int("enter a number")
num2 = int("enter a number 2")
if choices == "add":
    print("add is ",add(num1,num2))


