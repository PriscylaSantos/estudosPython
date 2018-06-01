#!/usr/bin/python3
#round() is a built-in function in Python. It returns x rounded to n digits from the decimal point.
# round(x, [,n])
import math

# number = math.pi
# digits = 5
# print(number)
# value = round(number, digits)
print(math.pi)
value = round(math.pi, 5)
print(value)
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print ("round(-100.000056, 3) : ", round(-100.1288956, 3))
