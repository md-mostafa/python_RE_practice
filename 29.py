#separate and print the numbers and their position of a given string.


import re

text = "The following example creates an ArrayList with a capacity of 50 elements.\
 Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."


pattern = "\d+"

for word in re.finditer(pattern, text):
    print(word.group(0))
    print('Index position : ', word.start())


'''
=> re.finditer(pattern, string, flags=0)
    Return an iterator yielding match objects over all non-overlapping matches for the RE pattern in string. 
    
=> \d
    For Unicode (str) patterns:
    Matches any Unicode decimal digit (that is, any character in Unicode character category [Nd]). 
    This includes [0-9], and also many other digit characters. If the ASCII flag is used only [0-9] is matched.
    
=> Match.group([group1, ...])
   Returns one or more subgroups of the match. 
   If there is a single argument, the result is a single string
   if there are multiple arguments, the result is a tuple with one item per argument.
   
    >>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    >>> m.group(0)       # The entire match
    'Isaac Newton'
    >>> m.group(1)       # The first parenthesized subgroup.
    'Isaac'
    >>> m.group(2)       # The second parenthesized subgroup.
    'Newton'
    >>> m.group(1, 2)    # Multiple arguments give us a tuple.
    ('Isaac', 'Newton')
'''
