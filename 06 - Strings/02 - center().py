#!/usr/bin/python3
#The method center() returns centered in a string of length width. Padding is done using the specified fillchar. Default filler is a space.
#str.center(width[, fillchar])

str = "this is string example....wow!!!"
print ("str.center(40, 'a') : ", str.center(40, 'b'))

str2 = "priscyla"
str2 = str2.capitalize()
print(str2)
y = len(str2)
print(y)
a = str2.center(y + 10, 'K')
print(a)