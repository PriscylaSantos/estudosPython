#!/usr/bin/python3
#The list() method takes sequence types and converts them to lists. This is used to convert  a given tuple into list
#list(seq)

aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print ("List elements : ", list1)
str="Hello World"
list2=list(str)
print ("List elements : ", list2)
print()

#The append() method appends a passed obj into the existing list.
list1 = ['C++', 'Java', 'Python']
list1.append('C#')
print ("updated list : ", list1)
print()

#The count() method returns count of how many times obj occurs in list.
aList = [123, 'xyz', 'zara', 'abc', 123];
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))
print()

#The extend() method appends the contents of seq to list.
list1 = ['physics', 'chemistry', 'maths']
print('List: ', list1)
list2=list(range(5)) #creates list of numbers between 0-4
list1.extend(list2)
print ('Extended List: ', list1)
print()

#The index() method returns the lowest index in list that obj appears.
# list1 = ['physics', 'chemistry', 'maths']
# print ('Index of chemistry', list1.index('chemistry'))
# print ('Index of C#', list1.index('C#'))
# print()

#The insert() method inserts object obj into list at offset index.
list1 = ['physics', 'chemistry', 'maths']
print('List: ', list1)
list1.insert(1, 'Biology')
print ('Final list : ', list1)
print()

#The pop() method removes and returns last object or obj from the list.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print('List: ', list1)
list1.pop()
print ("list now : ", list1)
list1.pop(1)
print ("list now : ", list1)
print()

#Removes object obj from list
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print('List: ', list1)
list1.remove('Biology')
print ("list now : ", list1)
list1.remove('maths')
print ("list now : ", list1)
print()

#The reverse() method reverses objects of list in place.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print('List: ', list1)
list1.reverse()
print ("list now : ", list1)
print()

# The sort() method sorts objects of list, use compare function if given.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print('List: ', list1)
list1.sort()
print ("list now : ", list1)




