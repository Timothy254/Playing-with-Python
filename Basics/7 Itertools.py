#Itertools is used to iterate over data structures that can be stepped over using a for-loop. 
#Such data structures are also known as iterables. This module works as a fast, 
#memory-efficient tool that is used either by themselves or in combination to form iterator algebra

#product

'''
from itertools import product

a = [1,2]
b = [3,4]
#prod = product(a,b)
print(list(product(a,b)))
'''


#permutations returns all the possible orders 

'''

from itertools import permutations

a = [1,2,3]
print(list(permutations(a)))
'''

#combinations makes all possible combinations of a certain length

'''

from itertools import combinations

a = [1,2,3,4]
print(list(combinations(a,2)))
'''

#accumulate by default does the sums of elements. can also multiply instead

'''
from itertools import accumulate
import operator

a = [1,2,3,4]
b = [1,2,10,3,4]

print(list(accumulate(a))) #this adds the elements
print(list(accumulate(a, func=operator.mul)))  #this multiplies each element
print(list(accumulate(b, func=max))) #compares for the largest value
'''


#groupby

'''
from itertools import groupby

def smallerthan3(x):
    return x < 3


a = [1,2,3,4]
groupobject = groupby(a, key=smallerthan3)  #instead of using a function we can use the lambda as shown bellow after the or comment
print( groupby(a, key=smallerthan3))
for key,value in groupobject:
    print(key, list(value))

         #OR

a = [5,6,7,8]
groupobject2 = groupby(a, key= lambda x: x<7)
for key, value in groupobject2:
    print(key, list(value))


        #EXAMPLE 2

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

groupobject3 =groupby(persons, key=lambda x: x['age'])
for key, value in groupobject3:
    print(key, list(value))

    '''

#infinite iterators


from itertools import count, cycle, repeat


for i in count(10):
    print(i)
    if i == 15:
        break

a = [1,2,3,4]

for i in cycle(a):
    print(i)
    

for i in repeat(a, 4):
    print(i)