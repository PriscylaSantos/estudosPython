#!/usr/bin/python3
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

#a in list, here in results in a 1 if a is a member of sequence list
if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")

#b not in list, here not in results in a 1 if b is not a member of sequence list.
if ( b not in list ):
    print ("Line 2 - b is not available in the given list")
else:
    print ("Line 2 - b is available in the given list")

c=b/a
print(c)
if ( c in list ):
    print ("Line 3 - a is available in the given list")
else:
    print ("Line 3 - a is not available in the given list")