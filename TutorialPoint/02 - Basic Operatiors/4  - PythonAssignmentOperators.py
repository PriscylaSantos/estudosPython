#!/usr/bin/python3
a = 21
b = 10
c = 0
c = a + b #assigns value os a + b into c
print ("Line 1 - Value of c is ", c)

c += a #is equivalent to c = c + a
print ("Line 2 - Value of c is ", c )

c -= a #is equivalent to c = c - a
print ("Line 3 - Value of c is ", c )

c *= a # is equivalent to c = c * a
print ("Line 4 - Value of c is ", c )

c /= a # is equivalent to c = c / a
print ("Line 5 - Value of c is ", c )

c = 2
c %= a # is equivalent to c = c % a
print ("Line 6 - Value of c is ", c)

c **= a #is equivalent to c = c ** a
print ("Line 7 - Value of c is ", c)

c //= a # is equivalent to c = c // a
print ("Line 8 - Value of c is ", c)
