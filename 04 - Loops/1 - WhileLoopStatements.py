#!/usr/bin/python3
#while loop Repeats a statement or group of statements while a given condition is TRUE.
# It tests the condition before executing the loop body.
#while expression:
#    statement(s)

count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1
print()

#The Infinite Loop : A loop becomes infinite loop if a condition never becomes FALSE
# var = 1
# while var == 1 : # This constructs an infinite loop
#     num = int(input("Enter a number :"))
#     print ("You entered: ", num)
# print()

#Python supports having an else statement associated with a loop statement.
count = 0
while count < 5:
    print (count, " is less"
                  " than 5")
    count = count + 1
else:
    print (count, " is not less than 5")
print()

#Here is the syntax and example of a one-line while clause
flag = 1
while (flag): print ('Given flag is really true!')
# press CTRL+C keys to exit
print ("Good bye!")
