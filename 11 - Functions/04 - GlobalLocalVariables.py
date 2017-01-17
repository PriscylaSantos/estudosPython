#!/usr/bin/python3

total = 0 #GLOBAL VARIABLE

def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1+arg2 # Here total is local variable.
    print("Inside the function local total: ", total)
    return total
sum(10,20)
print("Outside the function global total: ", total)
print()
total = sum(23,32)
print("Outside the function global total: ", total)