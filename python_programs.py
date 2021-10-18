#calc program

def add(x,y):
    return x + y

choice = input("enter a choice (add/sub/mul/div) : ").lower()
num1 = int(input("enter a num 1 :"))
num2 = int(input("enter a num 2 :"))
if choice == "add":
    print("num1 + num2 ",add(num1,num2))


#fizz buzz program 

for i in range(1,100):
    if i % 5 ==0 :
        print("fizz")
    elif i % 3 == 0:
        print("buzz")
    else:
        print(i)


#anagram 

a = list(input("enter a string 1 :"))
b = list(input("enter a string 2 :"))
a.sort()
b.sort()
for i in range(len(a)):
    if a[i] != b[i]:
        print("not a anagram")
        break
else:
    print("anagram")


#sum no.of elements in a list

a = [1,2,4,5,32,34,54,23]
count  = 0 
for i in a:
    count += i
print(count)


#leap year

year = int(input("enter a year : "))
if year %4 == 0 and year %100!=0 or year %400 ==0:
    print("leap year")
else:
    print("not a leap year")


#palindrome

a = input("enter a string : ")
if a == a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")


#max number in a list

a=[44,56,12,78,34,55]
count = a[0]
for i in a:
    if i > count :
        count = i
print(count)


#duplication deletion in a list

a = [1,2,3,4,5,5,6,7,7,8,9,9,10]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)


# way simple

a = [1,2,3,4,5,5,6,7,7,8,9,9,10]
b = list(set(a))
print(b)

#check given number is prime or not

num = int(input("enter a number "))
for i in range(2,num):
    if num % i == 0:
        print("prime number")
        break
else:
    print("not a prime number")


#factorial number 

a = int(input("enter a number : "))
x,y = 0,1
for i in range(a):
    print(y)
    x , y  = y ,x+y


# factorial sum 

a=int(input("enter a number :"))
sum=1
for i in range(1,a+1):
	sum=sum*i
print("the factorial of {} , is {}").format(a,sum)


#second largest number 


a = [1,23,42,34,24]
count1 = a[0]
count2 = 0
for i in a:
    if i > count1:
        count2 = count1
        count1 = i
    elif count1 > count2 < i:
        count2 = i
print(count2)


    
#missing number in list

a=[2,4,5,6,8,9]
a.sort()
for i in range(a[0],a[-1]):  
    if i not in a:
        print(i,end=',')


#pattern printing

a = int(input("enter a number : "))
for i in range(a+1):
    for j in range(i):
        print(i,end='')
    print('\r')