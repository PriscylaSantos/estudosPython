#!/usr/bin/python3
#The randrange() method returns a randomly selected element from range(start, stop, step).
#import random
# randrange ([start,] stop [,step])

import random
start = 1
stop = 200
step = 5
a = random.randrange(start, stop, step)
print(a)
print()
# randomly select an odd number between 1-100
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# randomly select a number between 0-99
print ("randrange(100) : ", random.randrange(100))
