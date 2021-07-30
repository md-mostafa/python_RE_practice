# find all words starting with 'a' or 'e' in a given string.

import re
text = "The following example creates an ArrayList with a capacity of 50 elements. /" \
       "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.""The following example creates/" \
       " an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

list = re.findall("[ae]\w+", text)
print(list)



'''
=> \w
    For Unicode (str) patterns:
    Matches Unicode word characters; 
    this includes most characters that can be part of a word in any language, 
    as well as numbers and the underscore. 
    If the ASCII flag is used, only [a-zA-Z0-9_] is matched.
'''