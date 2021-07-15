#Where a string will start with a specific number

import re
def findMatch(str):
    pattern = r'^5'
    text = re.compile(pattern)
    if text.match(str):
        return True
    else:
        return False

print(findMatch('5-2345861'))
print(findMatch('6-2345861'))
print(findMatch('1232432'))
print(findMatch('51232432'))


'''

=> re.compile(pattern, flags=0)
    Compile a regular expression pattern into a regular expression object, 
    which can be used for matching using its match(), search() and other methods,

'''