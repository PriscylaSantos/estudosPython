#!usr/bin/python3
import sys
list=[6,21,33,64]
it = iter(list) # this builds an iterator object
print(next(it)) #prints next available element in iterator

print()
#Iterator object can be traversed using regular for statement
for x in it:
   print (x, end=" ")
#or using next() function
print()
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit() #you have to import sys module for this

print()
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
    #   yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()