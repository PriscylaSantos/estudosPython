#!/usr/bin/python3
#The method hypot() return the Euclidean norm, sqrt(x*x + y*y). This is length of vector from origin to point (x,y)
#hypot(x,y)

import math

x = 3
y = 5
# sqrt(x*x + y*y)
# a = x*x
# b = y*y
# print(a, b)
# c = a+b
# d = math.sqrt(c)
# print(c, d )
d = math.hypot(3,5)
print(d)
print()
print ("hypot(3, 2) : ", math.hypot(3, 2))
print ("hypot(-3, 3) : ", math.hypot(-3, 3))
print ("hypot(0, 2) : ", math.hypot(0, 2))
