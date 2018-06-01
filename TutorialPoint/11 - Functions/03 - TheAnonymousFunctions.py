#!/usr/bin/python3

# lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total: ", sum(10,20))
print("Value of total: ", sum(14,37))
print()
mult = lambda  arg1, arg2, arg3: arg1 + arg2 * arg3
print("Value of total: ", mult(2,2,30))
print()

#The return Statement
def sumtwo(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function: ", total)
    return total
total = sumtwo(10,20)
print("Outside the function: ", total)
total = sumtwo(153,207)
print("Outside the function: ", total)