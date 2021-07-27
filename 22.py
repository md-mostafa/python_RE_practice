#find the occurrence and position of the substring within a string


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'


for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' %(text[s:e], s, e))



'''
=> re.finditer(pattern, string, flags=0)
    Return an iterator yielding match objects 
    over all non-overlapping matches for the RE pattern in string. 
    The string is scanned left-to-right, and matches are returned in the order found. 
    Empty matches are included in the result.
'''