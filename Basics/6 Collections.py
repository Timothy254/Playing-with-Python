#are containers used for storing data and are commonly known as data structures, such as lists, tuples, arrays, dictionaries

#counter It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
# Counts are allowed to be any integer value including zero or negative counts.
'''
from collections import Counter
a = "aaaabbbcccc"
mycounter = Counter(a)
print(mycounter)
print(mycounter.most_common(1))
print(list(mycounter.elements()))

'''


#namedtuple Python's namedtuple() is a factory function available in collections . 
# It allows you to create tuple subclasses with named fields.

'''

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

'''


#OrderedDict is a dict subclass that preserves the order in which key-value pairs, commonly known as items, are inserted into the dictionary. 
#When you iterate over an OrderedDict object, items are traversed in the original order. 
#If you update the value of an existing key, then the order remains unchanged.

'''
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

'''

#defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created. 

'''
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d['g'])
'''

#deque is a double-ended queue that's useful for implementing elegant, efficient, and Pythonic queues and stacks


from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
d.append(4)

d.pop()
d.popleft()
#d.clear()
d.extend([5,6,7])
d.extendleft([8,9,10])
d.rotate(1)
d.rotate(-2)
print(d)