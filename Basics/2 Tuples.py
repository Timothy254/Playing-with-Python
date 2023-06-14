#Tuples are ordered and immutable. Similar to list but it only cannot be changed/modified. 
#Oftenly used for objects that belong together.
#a tuple is smaller than a list(uses less bytes), and faster hence it is more efficient

mytuple = ("banana", "apple", "maembe", "avoc") 
mytuple2=tuple(["Max", 30, "Boston"])  #this creates a tuple from a list
mytuple3=(5, True, "apple",  "apple")
mytuple4=(101, 22, 2, 0, 34, -10, 2, 330, 1000, 200, 1)
mytuple5= ("a", "c", "p", "a", "z", "x", "h", "y", "s", "e", "q", "f", "z", "p", "c", "c", "c", "p")

"""
print(mytuple5.count("p"))  #counts how many ps are in the tuple
print(mytuple5.index("p")) #checksfor the first position of p
print(mytuple2[::-1]) #reversing

"""

#packing of a tuple.
""" 
name, age, city = mytuple2
print(mytuple2)
print(name)
print(age)
print(city)

#or you can use the star method. *i2 will take anything between first and last position as a list

i1, *i2, i3 = mytuple4
print(i1)
print(i2)
print(i3)

"""

#OTHER FUNCTIONS ARE SIMILAR TO LISTS