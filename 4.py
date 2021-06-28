#matches a string that has an a followed by zero or one 'b'.

import re

def match_text(text):
    patterns = 'ab?'

    if re.search(patterns, text):
        return 'Match Found!'
    else:
        return 'No Match!'


print(match_text('abb'))
print(match_text('ac'))
print(match_text('mo'))


'''
    
    --> ? Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab
    
    
    --> re.search(pattern, string, flags=0)
    Scan through string looking for the first location where the regular expression pattern produces a match,
    and return a corresponding match object. 
    Return None if no position in the string matches the pattern; 
    note that this is different from finding a zero-length match at some point in the string.
    
    
'''