#It is unordered and mutable. Consists of a collection of key value pairs

mydict={"name": "Timo", "age" : 24, "City" : "Nairobi"}
mydict2= dict(name='Sewe', age=25, city='Kisumo')
mydict3 = dict(name='Ogode', age=26, city='siaya', email='ogd@gmail.com')

#printing specific dictionary values
"""
value=mydict["name"]
print(value)
"""

#adding items to dictionary
"""
 mydict['Email'] = ['tim@gmail.com']
"""
 

#deleting items
"""
del mydict['Email'] #use del or pop("<enter_your_item>") or popitem() which removes the last item in the dictionary
mydict.pop('Email')
mydict.popitem()
"""
 
 #Traversing dictionarriess
"""
 
for i in mydict.keys():   #prints all the keys
    print(i)

for i in mydict.values(): #prints all the values
    print(i)

for i in mydict.items():  #prints all the items together as a list of key and values
    print(i)

"""
 
#copying
"""
 
cpy1 = mydict #this means that any change affect each of them
cpy2 = dict(mydict) #any changes will only affect the changed dictionary
cpy1.popitem()
print(mydict)
print(cpy1)
print(cpy2)

"""
 
 #update function literally updates the old(first mentioned dictionary in the function) with none existing keys in the last mentioned dictionary
"""
 mydict.update(mydict3)
print(mydict)

"""
 
 #we can also use a tuple as a key or value

tpl=("Max", 30, "Boston")
mydict4 = dict(details=tpl)
print(mydict4)

#OTHER FUNCTIONS ARE SIMILAR TO LISTS AND TUPLES