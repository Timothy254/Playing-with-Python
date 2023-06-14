mylist = ["banana", "apple", "maembe", "avoc"]  #LISTS ARE MUTABLE, THEY CAN BE CHANGED
#print(mylist)

mylist2=list()     #prints an empty Lists
#print(mylist2)

mylist3=[5, True, "apple",  "apple"]    #Lists can contain booleans, integers, strings etc
#print(mylist3)

item=mylist[0]   #this is the first item in the list
#print(item)

"""for i in mylist:   #how to traverse a list
    print(i) """

"""if "maembe" in mylist:
    print(True)
else:
    print(False)"""

#print(len(mylist))  #this tells the list length

mylist.append("cherry")
#print(mylist)

mylist.insert(2, "seeds") #at the position 2, cherry will be inserted
#print(mylist)

"""popitem=mylist3.pop() #pop automatically removes the last item, in the -1 position
print(mylist3)
print(popitem)"""

""""popitem=mylist.clear()  #clear() generally empties the list
print(mylist) """""

mylist4=[101, 22, 2, 0, 34, -10, 2, 330, 1000, 200, 1]
"""popitem=mylist4.sort() #This changes the original List so instead you can use sorted() method
print(mylist4)
srtlist=sorted(mylist4)
print(srtlist)  """


# creating a list with a same character multiple times
mylist5=[0] * 5
#print(mylist5)

#we can join 2 lists together
joined=mylist4 + mylist3
#print(joined)

#slicing helps to pick certain chctr
"""slcd=mylist4[1:5] #this will print xctrs starting from 1 to 5 position excluding 5th position
slcd1=mylist4[1:5:2] #this instructs it to jump 2steps
print(slcd)
print(slcd1)"""

#how to make a copy of a list
cpylst=mylist[::-1]
cpylst.append("This is the copy list")
#print(cpylst, "\n", mylist)

#