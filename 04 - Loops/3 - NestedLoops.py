#!/usr/bin/python3

#Nested loops: You can use one or more loop inside any another while, or for loop.

# for iterating_var in sequence:
#     for iterating_var in sequence:
#         statements(s)
#     statements(s)
#
# while expression:
#     while expression:
#         statement(s)
#     statement(s)

#b= range(1,11)
#for i in b
#   for i in b
for i in range(1,11): #for i in b
    for j in range(1,11):
        k=i*j
        print (k, end=' ')
    print()

print("*************")

i = 1
a = len(range(1,11))
while (i <= a):
    j = 1
    while (j <= a):
        k = i * j
        print(k, end=' ')
        j = j + 1
    print()
    i= i + 1
