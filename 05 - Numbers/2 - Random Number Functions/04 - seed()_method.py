#!/usr/bin/python3
#The seed() method initializes the basic random number generator. Call this function before calling any other random module function.
# seed ([x], [y])
import random

random.seed()
print ("random number with default seed", random.random())
random.seed(10)
print ("random number with int seed", random.random())
random.seed("hello",2)
print ("random number with string seed", random.random())
