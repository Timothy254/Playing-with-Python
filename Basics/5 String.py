#Ordered Immutable datatype

mystring = 'Hello world, Tim, Bob, Steve'

'''
print (mystring.strip())  
print (mystring.upper())
print (mystring.lower())
print (mystring.startswith('World'))
print (mystring.endswith('d'))
print (mystring.count('o'))
print (mystring.find('o'))
print (mystring.find('ll'))
print (mystring.replace('world', 'universe'))

'''


#convert to a list

mylist = mystring.split()
mylist1 = mystring.split('o')
mylist2 = mystring.split(',')
'''
print (mylist)
print (mylist1)
print (mylist2)
'''


#converting list to string 
'''
newstring = ' '.join(mylist)  #joins every element from our list into a string seperating them with '' or ''
print(newstring)
'''

#formating strings
a = 'Ted'
var = 'Tom'
s = 'the variable is %s' % var
print(s)

# or

s = 'the variable is {}' .format(var)

print(s)

#or

s = f'the variable is {var} and {a}'   #best way
print(s)