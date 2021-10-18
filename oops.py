#UNDERSTANDING OOPS IN PYTHON 


# SYNTAX for defining a class . all three are same


class student(object):
    pass

class student():
    pass

class student:
    pass



# CONSTRUCTOR IN A CLASS 

class student:

    def __init__(self):
        pass

#### the __init__() is the constructor class for student 



# METHODS IN CLASS 

class student:

    def __init__(self):
        print("this is a statement")

    # instance method
    def myfunc(self):
        print("this is second statement")



# ACCESSING THE CLASS USING OBJECTS

class student:

    def __init__(self):
        print("this is a statement")


    def myfunc(self):
        print("this is second statement")

#creating an object 
s1 = student()  # -> accessing the class using object s1
s1.myfunc()    # -->  accessing the method using s1



# ARGUMENTS INSIDE A CONSTRUCTOR

class student:
    def __init__(self,name,age,city):

        #instance variables 

        self.name = name
        self.age = age
        self.city =  city
        print("the user name",name)

    def myfunc(self):
        print("the user age",self.age)

s1 = student("anand","22","chennai")
s1.myfunc()



# ACCESSING CLASS / STATIC VARIABLE IN CLASS

class student:

    #class variable
    a = "username"

    def __init__(self):
       print("this is a statement 1 ") 


    def myfunc(self):
        print("this is statement 2 ")


s1 = student()
s1.myfunc()
print(s1.a)    #  -->  using object references to access the class variable



# VARIBLES IN PYTHON -  INSTANCE , LOCAL , CLASS / STATIC VARIABLES



# EXAMPLE OF ALL VARIABLES


#local variable outside class
a = "new_user"

class student:

    #class variable
    a = "username"

    def __init__(self,name):

        #instance variable 
        self.name = name

        print("this is a statement 1 ") 


    def myfunc(self):
        print("this is statement 2 ")


s1 = student()
s1.myfunc()
print(s1.a)  



#  A COMPLETE OVERVIEW

#local variable 
a = "new user"

#class name student
class student:

    # class variable b
    b = "admin_user"

    #constructor

    def __init__(self,name,age):

        #instance variables

        self.name = name
        self.age = age
        print("the name is ",name,"user type",a)

    # instance method
    def getage(self):
        print("the age is ",self.age)


s1 = student("anand","45")   # --> student("nams","age")  -## passing arguments 
s1.getage()
print(s1.b)    #  -->  objects reference to class variable




# EXAMPLE 

class bank:
    bank_name = "DBS"
    branch = "chennai"

    def __init__(self,acnumber,amount):
        self.acnumber = acnumber
        self.amount = amount

        print("account number is " , acnumber)
        print("the amount to debit",amount)

    
    def bankdetails(self,cname,cid):
        self.cname = cname
        self.cid = cid

        print("the customer name is",cname)
        print("the customer id is",cid)

    
    def withdraw(self):
        print("the withdraw amount is ",self.amount, "from account number" , self.acnumber)


print(bank.bank_name)    #if u want to access class varible use { classname.variablename }
print(bank.branch)
s1 = bank("123AC23","50000")  # acnumber , amount
s1.bankdetails("ANAND","312")  
s1.withdraw()




# METHODS IN PYTHON

# instance 
# class method
# utility / static



# EXAMPLE

class employee():

    # constructor
    def __init__(self):
        pass

    # instance method
    def emp_name(self):
        pass

    #class method
    @classmethod
    def employeeeducation(cls):
        pass

    #static method
    @staticmethod
    def employeesalary(self):
        pass




# CLASS METHOD

class employee():

    employeename = "lokesh"

    # constructor
    def __init__(self):
        pass

    # instance method
    def emp_name(self):
        pass

    #class method  -  accessed by class name
    @classmethod
    def employeeeducation(cls):
        cls.education = "B.e"
        print("the education is ",cls.education)
        print("the employee name is",employee.employeename)

    #static method  -- accessed by class name or object reference
    @staticmethod
    def employeesalary(self):
        a = [1,2,3,3,4,5,5,6,7,7,8,9]
        b = []
        for i in a:
            if i not in b:
                b.append(i)
        print(b)

#only for @class method
employee.employeeeducation()   # { classname.methodname }

# or
s1 = employee()
s1.employeeeducation()
s1.employeesalary



# class inside a class

class student:

    def __init__(self,name):
        self.name = name

    def new_student(self):
        print("new student ")

    
    class name:
        def __init__(self):
            pass


        def old_student(self):
            print("thsi is a statement")

a = student()
a.name()



