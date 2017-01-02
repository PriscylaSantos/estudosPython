# !/usr/bin/python3
#You can use one if or else if statement inside another if or else if statement(s).
# if expression1:
#     statement(s)
#     if expression2:
#         statement(s)
#     elif expression3:
#         statement(s)
#     else
#         statement(s)
# elif expression4:
#     statement(s)
# else:
#     statement(s)
num=int(input("enter number: ")) #Ex: 88
if num%2==0:
    if num%3==0:
        print ("Divisible by 3 and 2")
    else:
        print ("divisible by 2 not divisible by 3")
else:
    if num%3==0:
        print ("divisible by 3 not divisible by 2")
    else:
        print ("not Divisible by 2 not divisible by 3")
