#!/usr/bin/python3

#An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.
# if expression:
#     statement(s)
# else:
#     statement(s)
#
amount = int(input("Enter amount: ")) #Ex: 466

if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)

print("Net payable:", amount - discount)

print("***********")
# if expression1:
#     statement(s)
# elif expression2:
#     statement(s)
# elif expression3:
#     statement(s)
# else:
#     statement(s)
amount=int(input("Enter amount: ")) #Ex: 790
if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
elif amount<5000:
    discount=amount*0.10
    print ("Discount",discount)
else:
    discount=amount*0.15
    print ("Discount",discount)
print ("Net payable:",amount-discount)

