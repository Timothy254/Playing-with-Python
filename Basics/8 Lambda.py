#lambda function  for defining the anonymous function. Instead of using def to make a function. Best to use when you need a function only once
'''
add10 = lambda x: x+10
print(add10(5))


mult = lambda x,y: x*y
print(mult(2,4))
'''

'''

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2Dsorted = sorted(points2D) #sorts by value in x or value in oth position
points2Dsorted1 = sorted(points2D, key=lambda x: x[1])  #sorts by value in y or value in 1st position
points2Dsorted2 = sorted(points2D, key=lambda x: x[0] + x[1])  #sorts according to sum of x and y / (x+y)

print(points2D)
print(points2Dsorted)
print(points2Dsorted1)
print(points2Dsorted2)
'''


# map function. map(func, seq), transforms each element with the function.

a =[1,2,3,4,5,6]
'''
b = map(lambda x: x*2, a) #each element in list a will be multiplied by 2
print(list(b))
                #OR
c = [x*2 for x in a] #this is easier
print(c)
'''

#filter function. filter(func, seq), returns all elements for which func evaluates to True

'''

b = filter(lambda x: x%2 == 0, a)  #will filter a and give us only even nos in a
print(list(b))

            #OR

C = [x for x in a if x%2 == 0]
'''


#reduce. reduce(func, seq), repeatedly applies the func to the elements and returns a single value. func takes 2 arguments.

from functools import reduce
prod = reduce(lambda x,y: x*y, a)
print(prod)