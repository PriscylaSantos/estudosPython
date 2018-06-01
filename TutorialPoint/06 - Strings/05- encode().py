#!/usr/bin/python3
# The encode() method returns an encoded version of the string. Default encoding is the
# current default string encoding. The errors may be given to set a different error handling
# scheme.
import base64

Str = "this is string example....wow!!!"
Str=base64.b64encode(Str.encode('utf-8',errors='strict'))
print ("Encoded String: " , Str)