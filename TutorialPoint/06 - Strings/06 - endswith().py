#!/usr/bin/python3
# It returns True if the string ends with the specified suffix, otherwise return False optionally
# restricting the matching with the given indices start and end.

Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='exam'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))
