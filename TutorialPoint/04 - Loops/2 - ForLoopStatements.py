#!/usr/bin/python3
# for loop: Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable
# for iterating_var in sequence:
#     statements(s)

#The range() function : range() is the right function to iterate over a sequence of numbers
print(range(5))
#list object of the sequence
print(list(range(5)))
print()

a = range(5)
# b = list(range(5))
b = (list(a))
#for var in list(range(5))
for var in b:
    print(var)

print()
for letter in 'Python': # traversal of a string sequence
    print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # traversal of List sequence
    print ('Current fruit :', fruit)

print()
#Iterating by Sequence Index
fruits = ['banana', 'apple', 'mango']
print("Total number of elements in  fruits: ", len(fruits))
for index in range(len(fruits)):
    print ('Current fruit :', fruits[index])

print()
#Python supports having an else statement associated with a loop statement
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num%2==0:
        print ('the list contains an even number')
        break
else:
    print ('the list doesnot contain even number')

print()
print ("Good bye!")

