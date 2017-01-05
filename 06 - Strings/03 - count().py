#!/usr/bin/python3
#The count() method returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
#str.count(sub, start= 0,end=len(string))

str = "this is string example....wow!!!"
sub = 'i'
print ("str.count('i') : ", str.count(sub))
sub = 'exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))
print()
str2 = "Priscyla Cristhina dos Santos"
a = len(str2)
sub1 = 'a'
print("is:", str2.count(sub1))
print("is:", str2.count(sub1,0,8))
print("is:", str2.count(sub1,9,a))
print()

