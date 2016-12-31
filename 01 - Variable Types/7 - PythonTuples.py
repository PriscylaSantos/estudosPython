#!/usr/bin/python3
tuple = ( 'Anne', -7.86 , 2.23, 'Jorge', 70.2 )
tupleTwo = (23, 'Lures', 90)
print (tuple)             # Prints complete tuple
print (tuple[0])          # Prints first element of the tuple
print (tuple[1:3])        # Prints elements starting from 2nd till 3rd
print (tuple[2:])         # Prints elements starting from 3rd element
print (tupleTwo * 2)      # Prints tuple two times
print (tuple + tupleTwo)  # Prints concatenated tuple
print()
tuple = ( 'Anne', -7.86 , 2.23, 'Priscyla', 70.2 )
list = [ 'Anne', -7.86 , 2.23, 'Priscyla', 70.2 ]
tuple[2] = 1000 # Invalid syntax with tuple
list[2] = 1000 # Valid syntax with list