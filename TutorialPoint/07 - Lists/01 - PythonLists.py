#!/usr/bin/python3
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# Accessing Values in Lists
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#Updating Lists
print(list1)
print ("Value available at index 2 : ", list1[2])
list1[2] = 2001
print ("New value available at index 2 : ", list1[2])
print()

#Delete List Elements
print (list3)
del list3[2]
print ("After deleting value at index 2 : ", list3)
print()

#Basic List Operations
print(len([1,2,3])) #Length
print([1,2,3]+[4,5,6]) #Concatenation
print(['hi!'] * 4) #Repetition
print( 3 in [1,2,3,4]) #Membership
for x in [1,2,3,4,5] : #Iteration
    print (x,end=' ')
print()

#Indexing, Slicingand Matrixes
l=['C++', 'Java', 'Python']
print(l[2]) #Offsets start at zero
print(l[-2]) #Negative: count from the right
print(l[1:]) #Slicing fetches sections



