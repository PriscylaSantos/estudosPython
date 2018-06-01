#!/usr/bin/python3

# def functionname( parameters ):
#   "function_docstring"
#   function_suite
#   return [expression]

def printme (str):
    print("This printd a passed string into this function")
    print(str)
    return
printme("This is first call to the user defined function")
printme(str = "My string")#Keyword Arguments
#printme()# Error. Required Arguments
print()

def changeme(myList):
    print("Values: ", myList)
    myList[2] = 40
    print("Values: ", myList)
    return
myList = [10,20,30]
changeme(myList)
print()

def changemetwo(myList):
    myList = [1,2,3,4]
    print("Values: ", myList)
    return
myList = [10,20,30,40]
changemetwo(myList)
print("Values: ", myList)
print()

#Keyword Arguments
def printinfo(name, age):
    print("Name: ", name)
    print("Age: ", age)
    return
printinfo(age=25, name="Priscyla")
printinfo("Priscyla",25)
printinfo(25,"Priscyla")#Error, Name: 25 and Age : Priscyla
print()

#Default Arguments
def printinfotwo(name, age = 35):
    print("Name: ", name)
    print("Age: ", age)
    return
printinfotwo(age = 25, name = "Priscyla")
printinfotwo(name="Renata")





