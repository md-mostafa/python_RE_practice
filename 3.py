#matches a string that has an a followed by one or more b's.

import re
def text_match(text):
    patterns = 'ab+?'

    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'


print(text_match('abbabb'))
print(text_match('abc'))



'''
    
    --> + Causes the resulting RE to match 1 or more repetitions of the preceding RE.
    ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
    
    --> ? Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.
    
    --> re.search(pattern, string, flags=0)
    Scan through string looking for the first location where the regular expression pattern produces a match, 
    and return a corresponding match object. 
    Return None if no position in the string matches the pattern; 
    note that this is different from finding a zero-length match at some point in the string

'''