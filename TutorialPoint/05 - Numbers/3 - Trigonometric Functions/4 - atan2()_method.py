#!/usr/bin/python3
#The atan2() method returns atan(y / x), in radians.
#atan2(y,x)

import math

y = 30
x = 10
a = math.atan2(y,x)
print(a)
print ("atan2(-0.50,-0.50) : ", math.atan2(-0.50,-0.50))
print ("atan2(0.50,0.50) : ", math.atan2(0.50,0.50))
print ("atan2(5,5) : ", math.atan2(5,5))
print ("atan2(-10,10) : ", math.atan2(-10,10))
print ("atan2(10,20) : ", math.atan2(10,20))