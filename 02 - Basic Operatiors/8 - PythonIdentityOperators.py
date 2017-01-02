#!/usr/bin/python3
a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))
# here is results in 1 if id(a) equals id(b)
if ( a is b ):
    print ("Line 2 - a and b have same identity")
else:
    print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
    print ("Line 3 - a and b have same identity")
else:
    print ("Line 3 - a and b do not have same identity")

b = 30
print('Line 4', 'a=', a, ':', id(a), 'b=', b, ':', id(b))
# here is not results in 1 if id(a) is not equal to id(b)
if (a is not b):
    print("Line 5 - a and b do not have same identity")
else:
    print("Line 5 - a and b have same identity")
