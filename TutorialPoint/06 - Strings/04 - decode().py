#!/usr/bin/python3
#The decode() method decodes the string using the codec registered for encoding. It defaults to the default string encoding
#Str.decode(encoding='UTF-8',errors='strict')
Str = "this is string example....wow!!!"
Str = Str.encode('base64','strict')
print ("Encoded String: " + Str)
print("Decoded String: " + Str.decode('base64','strict'))
