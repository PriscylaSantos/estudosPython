#!/usr/bin/python3
#The choice() method returns a random item from a list, tuple, or string.
#import random
#random.choice(seq)
import random

seq = range(100)
a = random.choice(seq)
print(a)
print()
print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1,2, 3, 5, 9]))
print ("returns random character from string 'Hello World' : ",
random.choice('Hello World'))
