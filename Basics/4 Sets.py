#mutable but unlike lists and tuples it doesnt allow duplicate elements.  eg if we print myset4 it will remove the second 2

myset = {"banana", "apple", "maembe", "avoc"} 
myset2=tuple(["Max", 30, "Boston"])  #this creates a set from a list
myset3={5, True, "apple",  "apple"}
myset4={101, 22, 2, 0, 34, -10, 2, 330, 1000, 200, 1}

#adding and deleting elements
"""
myset.add(3)
myset.add(3000)
myset.add(88)
myset.add(5)
myset.add(7)
myset.remove(3)
myset.discard(88)
myset.pop(7)
myset.clear()
print(myset)
"""

#union and intersection
"""
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes ={2, 3, 5, 7, 23}

u = odds.union(evens)           #just joins
u2 = odds.union(primes)
i1 = odds.intersection(evens)   #just returns similar items
i2 = odds.intersection(primes)

print(u)
print(u2)
print(i1)
print(i2)
"""

#difference 

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
"""
diff = setA.difference(setB) #will return all elements in 1st set not there in second set
print(diff)

diff1 = setA.symmetric_difference(setB) #will return everything except elements that are in both set
print(diff1)
"""

#note if you want these intersection/union changes to stay permanent on the sets use the following fucntions
"""
setA.intersection_update(setB)
setA.difference_update(setB)
setA.symmetric_difference_update(setB)
"""
 

#subset and superset and disjoint 
"""
setC = {1,2,3,4,5}
setD = {1,2,3}
setE = {100,200,300}
print(setC.issubset(setD), setD.issubset(setC))      #checks if all values in first are all in last
print(setC.issuperset(setD), setD.issuperset(setC))  #opposite of subset

print(setC.isdisjoint(setE), setE.isdisjoint(setC), setD.isdisjoint(setC))  # checks if there are no same elements
"""


#To make a set immutable we use this function
a = frozenset([1,2,3,4,5,6,7,8,9,0])


#OTHER FUNCTIONS ARE SIMILAR TO previous datatypes