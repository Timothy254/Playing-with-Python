#Raising or asserting exceptions

'''
x = -5 
if x < 0:
    raise Exception('x should be positive')

#or 
a = -5
assert(a>=0), 'x is not possitive'
'''

#handling/cathing exceptions

'''

try:
    a = 5/0
except:
    print('Cannot be divided by 0')

                #OR

try:
    a = 5/1
    b = 1 + 'a'
except Exception as e:
    print(e)

except Exception as er:
    print(er)

else:
    print('ok')

finally:
    print('Cleaning up...')
'''

#definig exceptions

class ValueTooHighError(Exception):
    pass

class toosmall(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test(x):
    if x > 100:
        raise ValueTooHighError('Values is too high!!')
    if x < 5:
        raise toosmall('Value too small!!', x)
    
try:    
    test(2)
except ValueTooHighError as e:
    print(e)

except toosmall as e:
    print(e.message, e.value)