#!/usr/bin/python3
a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))

c = 0
c = a & b; # 12 = 0000 1100 ; Binary AND
print ("result of AND is ", c,':',bin(c))

c = a | b; # 61 = 0011 1101 ;  Binary OR
print ("result of OR is ", c,':',bin(c))

c = a ^ b; # 49 = 0011 0001 ;  Binary XOR
print ("result of EXOR is ", c,':',bin(c))

c = ~a; # -61 = 1100 0011 ; Binary Ones Complement
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2; # 240 = 1111 0000 ;  Binary Left Shif
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2; # 15 = 0000 1111 ;  Binary Right Shift
print ("result of RIGHT SHIFT is ", c,':',bin(c))
